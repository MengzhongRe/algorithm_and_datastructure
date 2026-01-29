# 手撕多头自注意力机制
import torch
import torch.nn as nn
import math

class MultiHeadAttention(nn.Module):
    def __init__(self,d_model,num_heads):
        super().__init__()
        # 1.考点1:维度检查
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads

        self.W_q = nn.Linear(d_model,d_model)
        self.W_k = nn.Linear(d_model,d_model)
        self.W_v = nn.Linear(d_model,d_model)

        self.fc_out = nn.Linear(d_model,d_model)

    def forward(self,q,k,v,mask=None):
        batch_size = q.size(0) # 先获取批量大小
        # q,k,v形状通常为[batch,seq_length,d_model]
        # 我们需要用view先分头[batch_size,seq_length,d_model] -> [batch_size,seq_length,num_heads,d_k]
        # 然后再调换seq_length与num_heads维度，实现每个注意力头分开计算
        # [batch_size,seq_length,num_heads,d_k] -> [batch_size,num_heads,seq_length,d_k]
        Q = self.W_q(q).view(batch_size,-1,self.num_heads,self.d_k).transpose(1,2)
        K = self.W_k(k).view(batch_size,-1,self.num_heads,self.d_k).transpose(1,2)
        V = self.W_v(v).view(batch_size,-1,self.num_heads,self.d_k).transpose(1,2)

        # 2.缩放点积注意力
        # 除以d_k,防止因为Q,K相乘之后数值过大再经过softmax使得概率值过于尖锐，导致梯度消失
        # scores的形状为[B,H,L,L]
        scores = torch.matmul(Q,K.transpose(-2,-1)) / math.sqrt(self.d_k)

        #考点：需要把Mask标记为0的Logits输出值设为负无穷,1e-9这样经过softmax归一化处理后,那么改词分到的注意力就会很小
        if mask is not None:
            scores = scores.masked_fill(mask==0,-1e9)
        
        attention = torch.softmax(scores,dim=-1)

        # 加权求和
        # out：[B,H,L,d_k]
        out = torch.matmul(attention,V)

        # 考点拼接前必须加contiguous函数，开辟新的内存空间存在数据以供view函数调整维度，否则会报错
        # [B,H,L,d_k] -> [B,L,H,d_k] -> [B,L,d_model]
        out = out.transpose(1,2).contiguous().view(batch_size,-1,self.d_model)

        return self.fc_out(out)
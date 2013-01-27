# Lottery!
import math as mt
import sys

# import data
inData = sys.stdin.read().split()

m=int(inData[0])
n=int(inData[1])
t=int(inData[2])
p=int(inData[3])

# calculates Chu-Vandermonde probabilities nCi*(m-n)C(p-i)/mCp
def vanderPr(m_, n_,p_,i_):
    
    m_ = float(m_)
    n_ = float(n_)
    p_ = float(p_)
    i_ = float(i_)
    
    Pr = 1
    
    for j in range(0,int(i_)):
        a = ((n_-j)/(i_-j))
        b = ((p_-j)/(m_-n_+i_-j))
        Pr = Pr*a*b
    
    for k in range(0,int(n_-i_)):
        c = ((m_-p_-k)/(m_-k))
        Pr = Pr*c
    
    return Pr

# Pr{entire group gets tix}= Pr(winners >= k)
k=int(mt.ceil(float(p)/float(t)))

# pdf -> cdf
prob = 0

for i in range(k,int(p+1)):
    prob += vanderPr(m,n,p,i)
    
sys.stdout.write(str(prob))
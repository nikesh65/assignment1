def gcd(p,q):
    if(q==0):
        return p
    else:
        return gcd(q,p%q)
p=int(raw_input())
q=int(raw_input())
GCD=gcd(p,q)
print GCD

def binex(base, pow):
    ans=1
    while pow>0:
        if pow&1:
            ans*=base
        base*=base
        pow//=2
    return ans

def binexmod(base, pow, mod):
    base%=mod
    ans=1
    while pow>0:
        if pow&1:
            ans=(ans*base)%mod
        base=(base*base)%mod
        pow//=2
    return ans%mod

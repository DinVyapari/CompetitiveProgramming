def binex(base, pow):
    ans=1
    while pow>0:
        if pow&1:
            ans*=base
        base*=base
        pow//=2
    return ans

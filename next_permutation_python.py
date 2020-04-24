def next_perm(strr):
    strr=list(str(strr))
    n=len(strr)
    ck=0
    for i in range(-2, -1*(n+1), -1):
        for i2 in range(i+1, 0, 1):
            if strr[i2]>strr[i]:
                tmp=strr[i]
                strr[i]=strr[i2]
                strr[i2]=tmp
                ck=1
                strr[i+1::]=sorted(strr[i+1::])
                strr=''.join(strr)
                break
        if ck:
            break
    return strr

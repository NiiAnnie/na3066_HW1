def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = m*ppy
    bondPrice = 0
    pvcft = 0
    for i in range (1,n+1):
            if i == n:
                pvcf = (face*(1+couponRate/ppy)/((1+y/ppy) ** i))
            else:
                pvcf = (face*couponRate/ppy)/((1+y/ppy) ** i)
            pvcft = pvcft + pvcf * i
            bondPrice = bondPrice + pvcf
            bondDuration = pvcft / bondPrice
    return(bondDuration)
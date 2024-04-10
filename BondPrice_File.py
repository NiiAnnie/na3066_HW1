def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m*ppy
    bondPrice = 0
    for i in range (1,n+1):
            if i == n:
                pmt = (face*(1+couponRate/ppy)/((1+y/ppy) ** i))
            else:
                pmt = (face*couponRate/ppy)/((1+y/ppy) ** i)
            bondPrice = bondPrice + pmt
    return(bondPrice)
def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    for index,value in enumerate(yc):
        if index == (m-1):
            pvcf = face*(1+couponRate)/((1+value) ** (index+1))
        else:
            pvcf = face*couponRate/((1+value) ** (index+1))
        bondPrice = bondPrice + pvcf
            
    return(bondPrice)
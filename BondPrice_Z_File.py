def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0
    m = len(times)
    for index,value in zip(times,yc):
        if index == times[m-1]:
            pvcf = face*(1+couponRate)/((1+value) ** (index))
        else:
            pvcf = face*couponRate/((1+value) ** (index))
        bondPrice = bondPrice + pvcf
            
    return(bondPrice)
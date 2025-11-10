def ipw(T, Y, p):
    w = T/p + (1-T)/(1-p)
    return (w * Y).mean()
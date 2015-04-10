def z_naive(s):
    #The string itself always match itself
    Z = [len(s)]
    for k in xrange(1,len(s)):
        n = 0
        while n+k < len(s) and s[n] == s[n+k]:
            n +=1
        Z.append(n)
    return Z


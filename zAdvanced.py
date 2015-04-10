def z_advanced(s):
    lt = 0
    rt = 0
    Z = [len(s)]
    for k in xrange(1,len(s)):
        if k > rt:
            i = 0
            while s[i] == s[i+k] and i+k < len(s):
                i +=1
            Z.append(i)
            if i > 0:
                lt = k
                rt = i+k-1
        else:
            p = k-lt
            if Z[p] < rt-k+1:
                Z.append(Z[p])
            else:
                j = rt+1
                while s[j]== s[j-k] and j<len(s):
                    j+=1
                Z.append(j-k)
                lt = k
                rt = j-1
    return Z

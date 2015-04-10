class Solution:
    def strStr(self,haystack,needle):
        if len(needle) > len(haystack) or (needle and not haystack):
            return -1
        elif (not needle and not haystack) or (haystack and not needle):
            return 0
        else:
            patternLen = len(needle)
            s = needle + haystack
            rt = 0
            lt = 0
            Z = [0] * len(s)
            Z[0] = len(s)
            for k in xrange(1,len(s)):
                if k > rt:
                    n = 0
                    while n+k < len(s) and s[n] == s[n+k]:
                        n+=1
                    Z[k] = n
                    if n >0:
                        lt = k
                        rt = k+n-1
                else:
                    p = k-lt
                    right_part_len = rt-k+1
                    if Z[p] < right_part_len:
                        Z[k] = Z[p]
                    else:
                        i = rt+1
                        while i<len(s) and s[i] == s[i-k]:
                            i +=1
                        Z[k] = i-k

                        lt = k
                        rt = i-1
                Z[k] = min(patternLen,Z[k])

                if Z[k] == patternLen and k>=patternLen:
                    return k-patternLen
            return -1
s = Solution()
print 'input: "",""', s.strStr("","")
print 'input:mississippi,mississippi', s.strStr('mississippi','mississippi')
print 'inpust:"a",""', s.strStr("a","")
print 'inpust:"mississippi","issip"', s.strStr("mississippi","issip")


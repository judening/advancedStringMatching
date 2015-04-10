class Solution:
    def strStr(self,haystack,needle):
        if len(needle) > len(haystack) or (needle and not haystack):
            return -1
        elif (not needle and not haystack) or (haystack and not needle):
            return 0
        else:
            patternLen = len(needle)
            textLen = len(haystack)
            searchString = needle+haystack
            print searchString
            for k in xrange(patternLen,len(searchString)):
                n = 0
                while n+k < len(searchString) and searchString[n] == searchString[n+k]:
                    n +=1
                if n == patternLen:
                    return k-patternLen
            return -1

s = Solution()
print 'input: "",""', s.strStr("","")
print 'input:mississippi,mississippi', s.strStr('mississippi','mississippi')
print 'inpust:"a",""', s.strStr("a","")
print 'inpust:"mississippi","issip"', s.strStr("mississippi","issip")

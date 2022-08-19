class Solution(object):
    # https://leetcode.com/problems/roman-to-integer/
    def Romantointeger(self,str):
        self.st = str
        if not len(self.str):
            return -1
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        stack=[]
        res=0
        for c in self.st:     
            v=dic.get(c,-1)
            if stack and dic[c] > dic[stack[-1]]:
                v=dic.get(c)-(2*dic.get(stack[-1]))
            res+=v
            stack.append(c)
        return res
    # https://leetcode.com/problems/longest-common-prefix/
    def longestCommonPrefix(self, strs):
        self.strs = strs
        if len(self.strs) == 0:
            return ''
        elif len(self.strs) == 1:
            return self.strs[0]
        k = min(self.strs,key=len)
        m = len(k)
        i = 0
        reference = k
        while i < m:
            for st in self.strs:
                if st[i] != reference[i]:
                    return reference[:i]
            i += 1
        return reference[:m]
    # https://leetcode.com/problems/string-to-integer-atoi/submissions/
    def myAtoi(self, s):
        if not len(s):
            return 0
        ls = list(s.strip())
        if len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+']:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret*10 + int(ls[i])
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))

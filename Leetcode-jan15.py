class Solution(object):
    def countSymmetricIntegers(self, low, high):
        # https://leetcode.com/problems/count-symmetric-integers/
        li = []
        for i in range(low, high+1):
            if len(str(i))%2 == 1:
                continue
            st = []
            ln = len(str(i))//2
            for j in str(i):
                st.append(int(j))
            sm1 = st[ln:]
            sm2 = st[:ln]
            if sum(sm1) == sum(sm2):
                li.append(i)
        return len(li)
        
    def sumBase(self, n, k):
        # https://leetcode.com/problems/sum-of-digits-in-base-k/
        res = ""
        while n:
            res =str(n%k) + res
            n = n//k
        sm = 0
        res = int(res)
        while res:
            sm += res%10
            res = res//10
        return sm

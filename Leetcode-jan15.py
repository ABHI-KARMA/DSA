class Solution(object):
    def countSymmetricIntegers(self, low, high):
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

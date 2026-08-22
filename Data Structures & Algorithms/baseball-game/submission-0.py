class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st=[]

        for op in ops:
            if op=="C": #cancel so pop it
                st.pop()
            elif op=="D": #double the top in stack and append
                score=st[-1]
                st.append(score*2)
            elif op=="+": #add the  top two and append it in stack
                last=st[-1]
                sec_last=st[-2]
                st.append(last+sec_last)
            else: #new string in number, convert into into and append it in stack
                score=int(op)
                st.append(score)
        #return sum of all from stack        
        return sum(st)
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        st=[]
        #for storing days
        ans=[0] * len(temp)

        for i in range(len(temp)):
            #if len>0 and temp > greatehr than stack temp then pop and store it inold
            #then find ans[old]
            while len(st) > 0 and temp[i] > temp[st[-1]]:
                old=st.pop()
                ans[old] = i-old
            #append i into stack
            st.append(i)
        return ans

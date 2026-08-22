class Solution:
    def isValid(self, s: str) -> bool:
        #for storing the chars
        st=[]
        pairs= {
            ')' : '(', ']':'[', '}' : '{'
        }

        for ch in s:
            #push the opening brackets
            if ch in '([{':
                st.append(ch)
            
            else:
                #if empty then false
                if len(st)==0:
                    return False
                #pop if get same closing brakcet on top else return False

                if st[-1] != pairs[ch]:
                    return False
                st.pop()
        return len(st)==0
                
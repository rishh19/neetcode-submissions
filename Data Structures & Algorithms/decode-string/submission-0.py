class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        current=""
        n=0

        for ch in s:
            if ch.isdigit():
                n=n*10 + int(ch)

            elif ch == "[":
                st.append((current,n))
                current=""
                n=0
            elif ch == "]":
                prev_str, repeat_number = st.pop()
                current = prev_str + current * repeat_number
            else:
                current+=ch
        return current 
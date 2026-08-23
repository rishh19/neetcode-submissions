class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]

        for current in asteroids:
            #current is postive, push it
            if current > 0:
                st.append(current)
                continue
            #if negative current then check it and pop
            while len(st)>0 and st[-1]>0 and st[-1] < -current:
                st.pop()
            #if stack top = current then pop
            if len(st) > 0 and st[-1] == -current:
                st.pop()
            #push current on to stack , if there is no element in stack present
            elif len(st) == 0 or st[-1] < 0:
                st.append(current)
        return st
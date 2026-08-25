class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=[]

        for i in range(len(position)):
            car.append((position[i],speed[i]))

        car.sort(reverse=True)
        st=[]

        for position,spd in car:
            time= (target-position)/spd

            if len(st)==0 or time > st[-1]:
                st.append(time)
        return len(st)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=[] 

        for i in range(len(position)):
            car.append((position[i],speed[i]))
#sort in desceding order
        car.sort(reverse=True)
        st=[]
#check time , if more time taken then append in st, else leave it 
        for position,spd in car:
            time= (target-position)/spd

            if len(st)==0 or time > st[-1]:
                st.append(time)
        return len(st)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i],speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        max_time = 0
        fleet = 0
        for car in cars:
            pos, spd = car
            current_time = (target - pos) / spd
            if current_time > max_time:
                fleet+=1
                max_time = current_time
        return fleet
        
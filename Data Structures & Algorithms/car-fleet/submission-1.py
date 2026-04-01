class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        curTime = 0.0
        fleets = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > curTime:
                fleets += 1
                curTime = time
        return fleets
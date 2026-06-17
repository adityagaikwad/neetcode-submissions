class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position in ascending order
        cars = sorted([(pos, s) for pos, s in zip(position, speed)])

        # times taken for each car starting from the closest one to reach target
        carReachingTimes = [(target - pos)/s for pos, s in cars]

        fleets = 0

        # to ensure we have at least two cars to compare
        # if its just one car then fleet is only one car
        while len(carReachingTimes) > 1:
            leadingCarTime = carReachingTimes.pop()

            # if lead car reaches before the one behind it,
            # then they can't form a fleet, it counts as it's own fleet
            if leadingCarTime < carReachingTimes[-1]:
                fleets += 1
            else:
                # else, since lead car is slower to reach the car behind it joins it
                # to form a fleet. So time for car behind lead  = time taken by lead
                carReachingTimes[-1] = leadingCarTime
        
        # fleets has individual cars which do not combine with other cars
        # carReachingTimes arr has cars which joined up with other cars
        return fleets + len(carReachingTimes)

"""
Sort cars by position ascending. For each car, compute time to reach
target as (target - pos) / speed.

Iterate from the car closest to target backward:
- If the lead car's time < the car behind it, the lead car arrives first
  and the trailing car can never catch it, so the lead is its own fleet.
- Otherwise the trailing car catches up, so they merge into one fleet
  traveling at the lead car's speed (replace trailing car's time with
  the lead car's time).

Answer is the number of distinct fleets formed.

Time: O(n log n)
Space: O(n)
"""
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
        
        # fleets counts front fleets that are too fast to be caught
        # the 1 remaining element is the rearmost fleet(may be multiple merged cars)
        return fleets + len(carReachingTimes)

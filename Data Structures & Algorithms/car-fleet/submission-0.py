class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0 
        cars = sorted(zip(position, speed))
        time = [ float(target - p) / s for p, s in cars ]

        while len(time) > 1:
            lead = time.pop()
            # Cannot catch lead  
            if lead <  time[-1] : 
                ans += 1
            else: 
                # Catch lead, but will be slowed down by lead
                time[-1] = lead

        return ans + bool(time)





        
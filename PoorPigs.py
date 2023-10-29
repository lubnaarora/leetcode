class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:

        tests_possible = minutesToTest//minutesToDie+1
        pigs = 0

        while tests_possible ** pigs < buckets:
            pigs += 1

        return pigs
        

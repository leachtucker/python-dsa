class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.helper(target, nums[0], 0, nums[1:])
    
    def helper(self, target, currNum, currIdx, restNums):
        for idx, num in enumerate(restNums):
            if currNum + num == target:
                return [currIdx, currIdx + 1 + idx]
        
        nextNum = restNums[0]
        newRestNums = restNums[1:]
        return self.helper(target, nextNum, currIdx + 1, newRestNums)
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for idx, num in enumerate(nums):
            if num not in seen:
                seen[num] = [idx]
            else:
                seen[num].append(idx)
            
        for num in seen:
            targetDiff = target - num
            numIdx = seen[num].pop(0)
            
            if targetDiff in seen:
                if len(seen[targetDiff]) >= 1:
                    targetDiffIdx = seen[targetDiff].pop(0)
                    return [numIdx, targetDiffIdx]
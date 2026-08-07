class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                #need a coppy to continue modifying
                res.append(cur.copy())
                return 
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            #non restricted call (includes duplicate canidates)
            dfs(i, cur, total+nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0,[],0)
        return res
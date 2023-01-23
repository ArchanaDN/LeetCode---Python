class Solution:
    
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
        if total % 2 != 0:
            return False
        
        W = int(total / 2)
        matrix1 = [0]*(W + 1)
        matrix2 = [0]*(W + 1)
        for i in range(W + 1):
            if nums[0] <= i:
                matrix1[i] = nums[0]
        print(matrix1)
        j = 0
        while j < len(nums):
            for i in range(1, W + 1):
                if nums[j] > i:
                    matrix2[i] = matrix1[i]
                else:
                    matrix2[i] = max(nums[j] + matrix1[i - nums[j]], matrix1[i])
                    print(nums[j] + matrix1[i - nums[j]])
            print(matrix2)
            if(matrix2[W] == W):
                return True
            
            matrix1 = matrix2
            j += 1
        
        return True if matrix2[W] == W else False


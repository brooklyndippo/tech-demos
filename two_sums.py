class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        
    def find_match (self):
        for index1, num1 in enumerate(self.nums):
            for index2, num2 in enumerate(self.nums):
                sum = num1 + num2
                if self.target_match(sum) and index1 != index2:
                    print(f'  num1: {num1}\n+ num2: {num2}\n= sum: {sum}\nindex array: [{index1},{index2}]')
                    return [index1, index2]

    def target_match (self, sum):
        if self.target == sum:
            return True


#----------------------------
#-------PROBLEMS-------------
#----------------------------

problem = Solution()

# EXAMPLE 1 
# input
nums = [2,7,11,15]
target = 9
# output 
# --> [0,1]

problem.twoSum(nums, target)
problem.find_match()

# EXAMPLE 2
# input
nums = [3,2,4]
target = 6
# output 
# --> [1,2]

problem.twoSum(nums, target)
problem.find_match()

# EXAMPLE 3
# input
nums = [3,3]
target = 6
# output 
# --> [0,1]

problem.twoSum(nums, target)
problem.find_match()

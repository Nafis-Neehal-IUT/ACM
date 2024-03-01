def twoSum(self, nums, target):
        hashtable = {}
        for (index, value) in enumerate(nums):
            complement = target - value 
            if complement in hashtable.keys():
                return [hashtable[complement], index]
                break
            hashtable[value] = index 
        return []
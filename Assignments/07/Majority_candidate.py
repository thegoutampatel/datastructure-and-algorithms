def findCandidate(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate == num
        count += (1 if num == candidate else -1)
        return candidate

def isMajority(nums, candidate):
    cnt = 0
    size = len(nums)

    for i in range(size):
        if nums[i] == candidate:
            cnt += 1
        
        if cnt > size/2:
            return 1
        else:
            return 0
    
def printMajorityElement(nums):
    cand = findCandidate(nums)
    if isMajority(nums,cand):
        print("majory element is ", cand)
    else:
        print("no majority element found")

#driver code 
nums = [2,2,1,1,1,2,2,2,2,2,2]

printMajorityElement(nums)

# Given a sorted integer array, which might have duplicated values, and also given a target integer number, find the first appearance of the target value in the array, return the index of the first appearance. If the target value can't be found, return -1. 
# example: given array [2,3,4,4,4,5,5,5,6,7,8,8,8,9], given target number 4, expected return is 2. Given same array, given target number 6, expected return is 8. Given same array, given target number 0, expected return is -1.

def finding_target(nums, target):
    l = 0
    r = len(nums)-1
    while l < r:
        mid = ((r-l)//2) + l
        print(f"l: {l}, r: {r}, mid: {mid}")
        if target > nums[mid]:
            print("taking right window")
            l = mid + 1
        elif target < nums[mid]:
            print("taking left window")
            r = mid - 1
        else:
            r = mid
            # if nums[l] < target:
            #     l += 1
            # if nums[r] > target:
            #     r -= 1
    if nums[r] == target:
        return r 
    else:
        return -1

sortedArrayString = input("Enter comma seperated list of integers: ")
sortedArray = sorted([int(x) for x in sortedArrayString.split(",")])
target = input("Enter target: ")
print(finding_target(sortedArray, int(target)))
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    
    # Use two pointers, one for the current element and one for the next unique element
    i = 0
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

# Example usage:
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
length = removeDuplicates(nums)
print("Array after removing duplicates:", nums[:length])
class solution:
    def remove_element(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

numbers = [0, 1, 2, 2, 3, 0, 4, 2]
print(f"Original Array: {numbers}")
target = int(input("Enter the number you want to remove: "))
sol = solution()
k = sol.remove_element(numbers, target)
print(f"\nResult")
print(f"Count of remaining elements: {k}")
print(f"Updated Array: {numbers[:k]}")

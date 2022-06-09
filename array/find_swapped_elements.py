def find_two_swapped(nums):
    n = len(nums)
    x = y = None # Initialize x and y as a value that cannot be the value of a node.
    for i in range(n - 1):
        if nums[i + 1] < nums[i]:
            y = nums[i + 1]
            # first swap occurrence
            if x is None:     
                x = nums[i]
            # second swap occurrence
            else:           
                break
    return x, y


if __name__ == "__main__":
    print(find_two_swapped([1,4,3,2]))
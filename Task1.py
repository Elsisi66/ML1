nums = [int(x) for x in input("Enter numbers \n").split(",")]

if nums[0] == nums[1] == nums[2]:
    if nums[0] > 0:
        print("It's positive")
    else:
        print("It's negative")
else:
    print("Minimum is", min(nums), "and Maximum is", max(nums))


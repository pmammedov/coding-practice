# two sum problem, returning the indices of the two numbers such that they add up to a specific target

def two_sum(nums, target):
    seen = {} # is an empty dictionary. It will map each number to its index: {value: index}

    for index, value in enumerate(nums): # enumerate gives you the position and the number together on each pass, so for [3, 2, 4] you get (0, 3), then (1, 2), then (2, 4).
        complement = target - value # The number you need to pair with value to hit the target.
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    return []
print(two_sum([2, 7, 11, 15], 9))
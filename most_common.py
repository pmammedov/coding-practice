def most_common(s):
    char_count = {}
    
    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the most common character
    most_common_char = None
    max_count = 0
    
    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            most_common_char = char
    
    return most_common_char


print(most_common("swiss"))  # Output: "s"
print(most_common("aabb"))  # Output: "a"
print(most_common("leetcode"))  # Output: "e"
print(most_common("aaA"))  # Output: "a"

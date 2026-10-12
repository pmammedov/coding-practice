def first_unique(s):
    char_count = {}
    
    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first unique character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

print(first_unique("swiss"))  # Output: "w"
print(first_unique("aabb"))  # Output: "None"
print(first_unique("leetcode"))  # Output: "l"
print(first_unique("aaA"))  # Output: "A"
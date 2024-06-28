def find_content_children(g, s):
    # Sort both lists
    g.sort()
    s.sort()
    
    # Initialize pointers
    g_pointer = 0
    s_pointer = 0
    
    # Iterate through both lists to find the maximum number of content children
    while g_pointer < len(g) and s_pointer < len(s):
        if s[s_pointer] >= g[g_pointer]:
            g_pointer += 1
        s_pointer += 1
    
    # The number of content children is equal to the g_pointer
    return g_pointer

g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child

find_content_children(s, g) 
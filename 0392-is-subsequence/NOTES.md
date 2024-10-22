Time Complexity: O(n + m), where n is the length of s and m is the length of t, since you only traverse each string once.
Space Complexity: O(1), as you are only using two pointers and no additional data structures.
​
2 ptrs: one for s and one for t - iterating through t (whileloop only dependent on pos of t_ptr). Each time a char in t matches current char in s, advance s_ptr by 1. If all chars in s are matched (ie: s_ptr == len(s), return True. Otherwise, if first we 'exhaust' t (ie; whilelooop completes and we exit it), return False.
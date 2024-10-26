- slow vs fast pointers: update slow only if unique elt found; update fast every time.
- "in-place" update array by setting NEW list value AT THE NEW slow idx (after incrementing upon finding new unique elt) to the value at the CURR fast idx ---- then update fast idx as normal.
- start fast idx at one pos AFTER the slow one.
​
Time: O(N) since we only have 2 pointers, and both the pointers will traverse the array at most once.
​
Space: O(1), since we are not using any extra space.
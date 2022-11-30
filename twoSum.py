def twoSum(lst: list, target: int) -> list:
    """
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.
    You can return the answer in any order.
    """
    for i in range(len(lst)):
        j=i+1
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return [i, j]



# def twoSum(lst: list, target: int) -> list:
"""
2) Hashmap is the second solution.

This issue can be solved in linear time. The concept is to utilise a hashmap to record the indices of previously visited items. The “key” of a hashmap is the number in the specified input array (You add this to the hashmap as you visit each element). The index of the number in the array represented by the hashmap key is the hashmap “value.”
Advertisements

This method performs the following stages for a given input array:

    Make a hashmap with integer datatypes as keys and values.
    Iterate through each element in the specified array, beginning with the first.
    Check the hashmap for the presence of the needed number (required number = goal sum – current number) in each iteration.
    If present, return the result necessary number index, current number index.
    Otherwise, add the current iteration number as a key to the hashmap and its index as a value. Repeat until you discover the answer.
"""
#     for i in range(len(lst)):
#         if filter(lst[i],lst[i+1:])

print(twoSum([3, 2, 4], 6))

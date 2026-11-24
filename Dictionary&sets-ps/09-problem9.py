# 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
# s[4][0]=9
# No we cannot change the list in teh set s bcz sets are unindexed and unordered even you cannot use the lists as the element in the sets
'''
 Output:
     s = {8, 7, 12, "Harry", [1,2]}
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: cannot use 'list' as a set element
'''
# print("List")
# arr = [1, 2, 3]
# arr.append(4)

# print(arr)
# arr.pop()
# print(arr)

# print(arr[0])
# print(arr[-1])
# print("-----------------")
# print("Tuple")
# t = (1, 2 ,3)
# print(t[0])

# print(t)
# print("-----------------")
# print("Set")
# s = set([1, 2, 3, 3])
# print(s)
# # s.add(4)
# # print(s)
# s.remove(2)
# print(s)
# print("-----------------")
# print("Dictionary")
# d = {"a": 1, "b": 2}
# print(d)
# print(d["a"])
# d['c']=566
# print(d)

# a = [1, 2, 3]
# print(a)
# print(a[:1])
# print(a[::-1])

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# print("----lambda----")
# node1 =ListNode(5)
# print(node1)
# node2 = ListNode(10, node1)

# print(node2)

# print("----lambda----")
# L = lambda x, y: x * y

# print(L(2, 4))

# print("----map----")
# nums = [1, 2, 3]
# M = list(map(lambda x: x*2, nums))
# print(M)

# print("----filter----")
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# F = list(filter(lambda x: x%2 != 0, nums))
# print(F)

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
    
#     if 
    # filter(lambda x: )

# 2025/08/07 Two Sum, Python
# --------------------------------------------------------------------------
nums = [2, 7, 11, 15]
# nums = [3, 2, 4]
# nums = [3, 3]


target = 9
# target = 6

solution = [0, 0]
done = False

for i in range(len(nums)):
    for j in range(len(nums)):
        print("i= %d, j= %d, done= %s"% (i, j, done))
        print("nums[i]= %d, nums[j]= %d\n" % (nums[i], nums[j]))
        if (i != j) and ((nums[i] + nums[j]) == target) and done == False:
            solution[0] = i
            solution[1] = j
            done = True
            break
            
print(solution)
# --------------------------------------------------------------------------







# iterate way
import math
def productSum(array):
    # Write your code here.
    level_of_detail={}
    level = 1
    while array:
        current_level_sum = 0
        for element in array:
            if type(element) == list:
                level_of_detail[level + 1] = level_of_detail.get(level + 1, []) + element
            else:
                current_level_sum = current_level_sum + element
        level_of_detail[level] = current_level_sum
        level += 1
        if level_of_detail.get(level, None) is not None:
            array = level_of_detail[level]
        else:
            array = None 

    return sum([math.factorial(key) * value for key, value in level_of_detail.items()])


array1 = [5,2,[7,-1],3,[6,[-13,8],4]] # expect 12
array2 = [1, 2, 3, 4, 5] # expect 15
array3 = [[1, 2],3,[4, 5]] # expect 27

array4 = [
  [
    [
      [
        [5]
      ]
    ]
  ]
] # expect 600
print(productSum(array1))
print(productSum(array2))
print(productSum(array3))
print(productSum(array4))
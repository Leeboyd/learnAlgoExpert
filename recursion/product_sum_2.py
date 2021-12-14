def productSum(array, level=1, sum=0):
    for element in array:
        if type(element) is list:
            sum += productSum(element, level + 1)
        else:
            sum += element

    return sum * level

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
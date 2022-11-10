# def a_sum(*args): #args are for entering as many arguemtns as possible
#   for num in args:
#     print(num)

# print(a_sum(1))
# print(a_sum(1,3,5,7))


# def my_sum(*args):
#   print(args)
# print(my_sum(3,4,5))
list = [3,4,5,6,7,8,9,12,32,46]
def sum_numbers(list):
  sum = 0
  for num in list:
    sum += num
  return sum

print(sum_numbers(list))


# args 
def a_sum(*args):
  # total = 0
  # for num in args:
  #   total += num
  # return total
  return sum (args)
print(a_sum(4,2,3))
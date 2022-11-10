def a_sum(*args): #args are for entering as many arguemtns as possible
  for num in args:
    print(num)

print(a_sum(1))
print(a_sum(1,3,5,7))


def my_sum(*args):
  print(args)
print(my_sum(3,4,5))
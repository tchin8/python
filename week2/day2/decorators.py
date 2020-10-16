# def exponent_function_decorator(exponent_function_to_wrap):
#   def wrapper_function(base_number, exponent):
#     return base_number ** exponent_function_to_wrap(exponent)
#   return wrapper_function


# def exponent_function(exponent):
#   return int(exponent)

# # print(exponent_function)
# # print(exponent_function(2.1214))

# exponent_function = exponent_function_decorator(exponent_function)

# # print(exponent_function)
# # # print(exponent_function.__closure__)
# # print(exponent_function.__closure__[0].cell_contents)
# print(exponent_function(4, 2.1214))


def exponent_function_decorator(exponent_function_to_wrap):
  def wrapper_function(*args, **kwargs):
    print(args)
    print(kwargs)
    base_number, exponent = args
    return base_number ** exponent_function_to_wrap(exponent)
    # return kwargs['base_number'] ** exponent_function_to_wrap(kwargs['exponent'])
  return wrapper_function

@exponent_function_decorator
def exponent_function(exponent):
  return int(exponent)

print(exponent_function(4, 2.1214))  #args
# print(exponent_function(base_number=4, exponent=2.1214))  #kwargs, keyword args

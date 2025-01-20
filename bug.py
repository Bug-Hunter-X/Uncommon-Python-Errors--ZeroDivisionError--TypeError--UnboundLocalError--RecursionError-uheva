def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Unsupported type"

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Division by zero
print(function_with_uncommon_error(10, "hello"))  # Output: Unsupported type

# Example of a less common error (UnboundLocalError):

def uncommon_error():
    x = 10  # x is in the local scope
    if True:
        x += 1  # This is modifying the local x
    return x  #This return the local x

print(uncommon_error())  # Output 11

# Another example of a less common error (RecursionError):

def recursive_function(n):
    if n == 0:
        return 0
    else:
        return recursive_function(n - 1)  #This is a stack overflow, increase n and you will get this error

print(recursive_function(1000)) #Output: RecursionError: maximum recursion depth exceeded

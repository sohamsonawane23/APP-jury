def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func() # Call the original function
        print("Something after the function runs.")
    return wrapper
def say_hello():
    print("Hello!")
# Manually decorate
decorated_function = my_decorator(say_hello)
decorated_function()
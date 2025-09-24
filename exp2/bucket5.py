print("soham sonawane")
def square_numbers():
    for i in range(1, 6):
        yield i * i

# Iterate and print squared numbers
for square in square_numbers():
    print(square)

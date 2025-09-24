print("soham sonawane")
def count_up_to(max_number):
    current = 1
    while current <= max_number:
        yield current
        current += 1

# Use the generator to count up to 7
for number in count_up_to(7):
    print(number)

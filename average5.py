
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Number {i + 1}: "))
    numbers.append(num)

average = calculate_average(numbers)

print(f"The average of the numbers {numbers} is: {average}")

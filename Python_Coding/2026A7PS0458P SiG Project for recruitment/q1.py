user_input = input("Enter a few numbers, please: ")
numbers = [int(num)for num in user_input.split()]

if numbers:

    x = numbers[0]
    y = numbers[0]
    total_sum = [0]
    even_count = [0]
    odd_count = [0]

for item in numbers:
    n = item

    if n > x:
        x = n

    if n < y:
        y = n

    total_sum[0] += n

    if n % 2 == 0:
        even_count[0] += 1
    else:
        odd_count[0] += 1

    mirror_list = []
    for i in range(len(numbers)):
        mirror_list.append(numbers[-1 -i])

print("The largest number is:", x)
print("The smallest number is:", y)
print("The sum of all numbers is:", total_sum[0])
print("The count of even numbers is:", even_count[0])
print("The count of odd numbers is:", odd_count[0])
print("The mirror list is:", mirror_list)


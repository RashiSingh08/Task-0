# First we define our list processing function and what all we will do.
# We could have written copied_list stuff after taking input too but here, question specifies that we need to use functions.

def process_list(numbers):

    copied_list = numbers.copy()

    copied_list = [term for term in copied_list if term >= 0]

    copied_list.append(0)

    copied_list.sort()

    return copied_list


original = [int(x) for x in input("Enter a few numbers, please: ").split()]

result = process_list(original)

print("Original:", original)
print("Result:", result)
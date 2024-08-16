# Sample list of numbers
numbers = [34, 7, 23, 32, 5, 62]

# Bubble Sort algorithm
n = len(numbers)
for i in range(n):
    # Track whether any swapping occurred in this pass
    swapped = False
    for j in range(0, n - i - 1):
        # Swap if the element found is greater than the next element
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
    # If no two elements were swapped in the inner loop, then the list is sorted
    if not swapped:
        break

# Display the sorted list
print("Sorted list:", numbers)


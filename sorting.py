def sort(num):
    for i in range(len(num)):
        for j in range (i+1, len(num)):
            if num [i] > num [j]:
                num [i], num[j] = num[j], num[i]
num = list(map(int, input("Enter the set of numbers to be sorted: ").split()))
b = sorted(num)
print("Sorted numbers are: ", b)
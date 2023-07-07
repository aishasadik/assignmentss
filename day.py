list = []
nums = int(input("Enter the number of Elements :"))
sum = 0
for i in range(0,nums):
        elements = int(input("Nos :"))
        list.append(elements)
        sum += elements
        average = sum/nums
print(list)
print("Average :",average)
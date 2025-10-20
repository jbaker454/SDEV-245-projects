total: float = 1
num_count: int = 1
num: float = 1


num_count = int(input("How many numbers do you want to add? "))


for i in range(num_count):
    num = float(input("Enter number {}: ".format(i+1)))
    
    total += num


print("The sum of the numbers you entered is:", total)

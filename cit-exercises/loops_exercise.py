# Aheebwa Rodrick

# number 1
print("Number 1")
i = 1
while i < 11:
    print(i, end='  ')
    i+=1
print("\n")

# number 2
print("Number 2")
n = int(input("Enter a number up to which you want to sum numbers: "))
sum = 0
for i in range(n+1):
    sum+=i
print(sum)

# number 3
print("Number 3")
n = int(input("Enter a number whose multiples you want: "))
for i in range(1,13):
    print(i*n, end='  ')
print("\n")

# number 4
print("Number 4")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num%5 == 0:
        if num > 500:
            break
        if num > 150:
            continue
        print(num, end='  ')
print("\n")

# number 5
print("Number 5")
n = 4673453
i = 0
while n > 0:
    n//=10
    i+=1
print(i)

# number 6
print("Number 6")
n = -10
while n < 0:
    print(n, end='  ')
    n+=1
print('\n')

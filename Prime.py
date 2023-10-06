def is_prime(num):
    if num <= 1:
        return True
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print ("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)
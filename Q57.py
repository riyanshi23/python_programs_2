def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True
print(isprime(7))
print(isprime(8))

def prime():
    n = int(input("Enter a number:  "))
    if n < 2:
        print(n,"is not a prime")
        return
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            print(n,"is not a prime")
            break
    else:
        print(n,"is prime")
prime()
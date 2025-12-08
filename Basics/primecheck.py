def prime(n):
    if n <= 1:
        return "neither prime nor composite"
    
    for i in range(2, n):
        if n % i == 0:
            return "composite"
    
    return "prime"

def nprime():
    for n in range(2, 1100):  
        is_prime = True
        for i in range(2, n):  
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n, "is prime")

nprime()




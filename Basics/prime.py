def prime(n):
    if n <= 1:
        return "neither prime nor composite"
    
    for i in range(2, n):
        if n % i == 0:
            return "composite"
    
    return "prime"

print(prime(3000))
n = int(input("Enter prime number (n): "))

k = int(input("Enter number of following primes (k): "))

def is_prime(num):

    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_kth_prime_after_n(n, k):
    """Find the k-th prime number after n"""
    if not is_prime(n):
        raise ValueError(f"{n} is not a prime number!")
    
    current = n + 1
    count = 0
    
    while count < k:
        if is_prime(current):
            count += 1
            if count == k:
                return current
        current += 1
        
try:
    result = find_kth_prime_after_n(n, k)
    print(f"The {k}-th prime after {n} is: {result}")

except ValueError as e:
    print(f"Error: {e}")
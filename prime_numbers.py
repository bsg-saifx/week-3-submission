import math

def prime_generator():
    yield 2 
    num = 3
    while True:
        is_prime = True
        limit = int(math.sqrt(num)) + 1
        for p in range(2, limit):
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 2 


if __name__ == "__main__":
    gen = prime_generator()
    for _ in range(20):
        print(next(gen), end=" ")


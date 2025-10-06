import time


def current_milli_time():
    return round(time.time() * 1000)


def is_prime(x):
    prime = True
    if x == 1:
        return False
    else:
        for i in range(2, x-1):
            if (x % i) == 0:
                prime = False
    return prime


rs = 1000
re = 40000

start = current_milli_time()
for i in range(rs, re):
    if is_prime(i):
        print(i, "is prime")
end = current_milli_time()

print((re-rs), "numbers searched in", end-start, "milliseconds")

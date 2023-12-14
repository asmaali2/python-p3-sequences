#!/usr/bin/env python3

def print_fibonacci(length):
    size=[0,1]
    while len(size)<length:
        next_number= size[-1] + size[-2]
        size.append(next_number)
    print(size[:length])
    pass
print_fibonacci(9)
def func (n):
    return n and (func(n - 1) + n);

print(func(100));
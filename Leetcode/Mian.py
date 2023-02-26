def fibbonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)
def getFibonacciNumbers(num):
    if(num < 0):
        return [0]
    list = [0,1]
    while True:
        next_fib = list[-1] + list[-2]
        if next_fib == num:
            break
        list.append(next_fib)
    return list if num >=1 else [0]

print(getFibonacciNumbers(5))


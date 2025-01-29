def isPrimeNumber(number):
    # check if number is positive and not one
    #     if the number has any divisors from 2 to number-1 then its not prime
    if number < 0 or number == 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    # loop through the numbers and use the isPrime function to check whether the function is prime or not, and append the appropriate number to the list
    return[i for i in range(2, n+1) if isPrimeNumber(i)]

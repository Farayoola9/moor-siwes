# A function that tajes an argument and returns "Fizz" or "Buzz" or "FizzBuzz"
def FizzBuzz(num):
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    return(num)
print(FizzBuzz(10))
print(FizzBuzz(18))
print(FizzBuzz(32))
print(FizzBuzz(75))
print(FizzBuzz(81))

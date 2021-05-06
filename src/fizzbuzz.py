def fizzbuzz(number):
    if number == 0:
        raise ValueError("Number must not be zero")
    message = ""
    if number % 3 == 0:
        message += "Fizz"
    if number % 5 == 0:
        message += "Buzz"
    if message == "":
        message = str(number)
    return message

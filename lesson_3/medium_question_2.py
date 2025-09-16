# Alan wrote the following function, which was intended to return all of the factors of number:

def factors(number):
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. 
# How can he make this work? Note that we're not looking to find the factors for negative numbers, 
# but we want to handle it gracefully instead of going into an infinite loop.

# i first made a if statement checking if the number was less than zero then returning a print statement asking for a non negative number
# i then looked at the solution and it was much better just by swithing it to a greater symbol achives the same thing
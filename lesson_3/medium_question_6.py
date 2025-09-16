# What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# it will print 34 because the print statemt was focusing on subracting 8 from answer and the variable was not mutated in any way
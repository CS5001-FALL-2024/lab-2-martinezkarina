'''
    CS 5001
    Lab 1
    Exercise 3
    Name: Karina Martinez
'''

'''
Replace the # YOUR CODE HERE markers below with
code that will calculate the correct values for
difference, product, and average. Complete the
print statements to output correctly formatted  
results.

Note: the code below is not syntactically correct and will not run until
you replace the # YOUR CODE HERE with the correct solution.
'''


def main():
    x = 5
    y = 10

    # Assign values to the variables below to calculate the difference, product, and average of the values in x and y.
    difference = x - y
    product = x * y
    average = (x + y) / 2

    # Replace the # YOUR CODE HERE text in the statement below so that the statement will print
    # The difference between x and y is difference.
    # where x, y, and difference are replaced with the values stored in the corresponding variables.    
    print (f'the difference between {x} and {y} is {difference}')
    # Write a statement to print the product of x and y.
    print (f'the product of {x} and {y} is {product}')
    # Write a statement to print the average of x and y. Make sure this prints 7.5!
    print (f'the average of {x} and {y} is {average}')

if __name__ == '__main__':
    main()


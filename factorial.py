'''
1. Input validation
2. Check termination conditions for loops / recursions
'''
from unittest import TestCase, main

# Find factorial of a number
def factorial(number: int) -> int:
    if(number is None):
        raise ValueError('Invalid base.')
    
    elif(number < 0):
        raise ValueError('Undefinded')
    
    elif(number == 0):
        return 1

    else:
        factorial = 1
        while(number > 1):      # -- Termination condition
            factorial *= number
            number -= 1

        return factorial


class TestCase(TestCase):
    def test1(self):
        self.assertRaises(ValueError, factorial(-1))
    
    def test2(self):
        self.assertEqual(factorial(0), 1)

    def test3(self):
        self.assertEqual(factorial(5), 120)


if __name__ == '__main__':
    main()
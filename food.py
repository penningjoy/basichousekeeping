'''
1. Remove unused imports
2. Order your imports correctly
3. Meaningful function and variable names
4. Maintain the character length of each statement
5. Put comments at places that can be inconspicuous at first sight
6. Keep functions / methods short, simple and DRY
7. Follow good scoping principles and access specifications.
'''

from abc import abstractmethod
from collections import defaultdict
from typing import List

class Food:
    def __init__(self):
        self.__is_edible = True

    @property
    def isedible(self):
        return self.__is_edible

    @abstractmethod
    def get_ingredients(self):
        pass
    
    @abstractmethod
    def calorie_calculator(self):
        pass

class Biriyani(Food):
    def get_ingredients(self) -> List:
        return ["rice","meat","egg","spices"]

    ''' the calorie calculator formula
    Total calories = 4 cal * each gram of protein +
                     4 cal * each gram of carbohydrates +
                     9 cal * each gram of fat
    '''
    def calorie_calculator(self) -> int:
        protein = 10
        carbs = 25
        fat = 10
        
        return (4 * 10 + 4 * 25 + 9 * 10)
 

class Pizza(Food):
    def get_ingredients(self) -> List:
        return ["bread","vegetables","cheese","condiments"]

    def calorie_calculator(self) -> int:
        protein = 13
        carbs = 36
        fat =  12

        return (4 * 13 + 4 * 36 + 9 * 12) 


foods = [Biriyani(), Pizza()]

for item in foods:
    if item.isedible:
        print((type(item).__name__ ) + 
            ' has ' + ",".join(item.get_ingredients()) + 
            ' with ' + str(item.calorie_calculator()) +' calories.'
            )




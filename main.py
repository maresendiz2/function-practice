#functions printing and returning
#print something in a function, its only for displaying
#some data, you are doing nothing with the data
#when you return in a function, you are going to use it
# in another part of your program
from addfruit import AddFruit
from dividefruit import DivideFruit
from subtractfruit import SubtractFruit
from displayfruit import DisplayFruit
apples = int(input("how many apples?"))
oranges = int(input("how many oranges?"))

# add fruit
#whenever you return items, you must put the
#returned value inside of a variable
fruitAdded = AddFruit(apples,oranges)
print(fruitAdded)
# subtract fruit

fruitSubtracted = SubtractFruit(apples,oranges)
print(fruitSubtracted)

# divide fruit

fruitDivided = DivideFruit(apples,oranges)
print(int(fruitDivided))
# display the added fruit, subtracted fruit, and divided fruit
fruitDisplayed = DisplayFruit(fruitAdded,fruitSubtracted,fruitDivided)
print(fruitDisplayed)
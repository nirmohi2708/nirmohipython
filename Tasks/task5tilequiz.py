
print("Number of tiles for the part one are 9 tiles are wide and 7 tiles long")
print("Number of tiles for the part two are 5 tiles are wide and 7 tiles long")

'''
To find the no of tiles we need to find area
After adding both the areas of part one and part two we can find the total area 
'''

#No. of tiles

area=9*7

print("Area of tile of part one ", area)

area2=5*7

print("Area of tile of part two ", area2)

sum=area+area2

print("Addition",sum)

Total=print("Total area of both part is ",sum)

#Part two of question

"""
Given : 17 packages are bought and each tile contain 6 tiles
Find : leftover tiles
"""

print("The number of leftover tiles are ",17*6-(sum))


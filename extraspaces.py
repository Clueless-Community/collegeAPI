Python | Remove unwanted spaces from string

# Python3 code to demonstrate working of
# remove additional space from string
# Using re.sub()
import re

# initializing string
test_str = "GfG is good		 website"

# printing original string
print("The original string is : " + test_str)

# using re.sub()
# remove additional space from string
res = re.sub(' +', ' ', test_str)

# printing result
print("The strings after extra space removal : " + str(res))


Output : 
The original string is : udemy      is   good           website
The strings after extra space removal : udemy is good website

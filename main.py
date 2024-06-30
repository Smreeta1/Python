import demo                                                  # Importing the demo module
from demo import *                                           # From demo module,importing specific functions greet() and sum()
from string_modify.reverse_str import reverse_string        # Importing the reverse_string function from the string_modify.reverse_str module


# Calling greet() function from the demo module
print(greet())

# Call sum() function from the demo module with arguments 10 and 20,
result=demo.sum(10, 20)
print("The sum is:", result)
 
#print reverse string
reversed_string = reverse_string("hello")
print(reversed_string)

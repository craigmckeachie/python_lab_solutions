


import math


side1 = input("What is the name of the first side or your triangle? ").strip().capitalize()
side1_length = float(input("What is the length of the first side or your triangle? "))
side2 = input("What is the name of the second side or your triangle? ").strip().capitalize()
side2_length = float(input("What is the length of the second side or your triangle? "))
hypotenose = math.sqrt(side1_length ** 2 + side2_length ** 2)
print(f""" 
          {side1:15}{side1_length}    
          {side2:15}{side2_length}
          HYPOTENUSE     {hypotenose:.2f}
    """)
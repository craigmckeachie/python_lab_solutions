"""
A script that uses list comprehentions for simple math between 1-10
"""
import math

X_AXIS = list(range(1, 10))
Y_AXIS = list(math.log2(x) for x in X_AXIS)

print(X_AXIS)
print(Y_AXIS)


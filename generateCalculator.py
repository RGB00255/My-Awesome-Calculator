# My first calculator generator
__author__ = "Ryan Bergeron"

import os

start = 0
end = 101 # Up to but not including

# Initialize
f = open("calculator.py", 'w')
f.write("# My first calculator\n")
f.write("__author__ = \"{a}\"\n\nimport os".format(a=__author__))
f.write("\n\n# THE FUNCTION\n")
f.write("def Calculate(a, s, b):\n")

signs = ["+", "-", "*", "/"]

for i in signs:
    for j in range (start, end):
        for k in range (start, end):
            if i == "/" and k == 0: # Check for division by 0
                ans = "inf"
            else:
                ans = eval("j {s} k".format(s=i))
            f.write("\tif a == \"{j}\" and s == \"{i}\" and b == \"{k}\":\n".format(j=j, i=i, k=k))
            f.write("\t\tprint (\"{j} {i} {k} = {a}\")\n".format(a=ans,j=j, i=i, k=k))

f.write("\nnum1 = input(\"Enter your first number: \")")
f.write("\nsign = input(\"Enter your sign (+, -, *, /): \")")
f.write("\nnum2 = input(\"Enter your second number: \")")

f.write("\nCalculate(num1, sign, num2)")
# My first calculator generator
__author__ = "Ryan Bergeron"

import os

# Initialize
f = open("calculator.py", 'w')
f.write("# My first calculator\n")
f.write("__author__ = \"Ryan Bergeron\"\n\nimport os")
f.write("\n\n# THE FUNCTION\n")
f.write("def Calculate(a, s, b):\n")

signs = ["+", "-", "*", "/"]

for i in signs:
    for j in range (1, 101):
        for k in range (1, 101):
            ans = eval("j {s} k".format(s=i))
            f.write("\tif a == \"{j}\" and s == \"{i}\" and b == \"{k}\":\n".format(j=j, i=i, k=k))
            f.write("\t\tprint (\"{j}\" + \" {i} \" + \"{k}\" + \" = \" + \"{a}\")\n".format(a=ans,j=j, i=i, k=k))

f.write("\nnum1 = input(\"Enter your first number: \")")
f.write("\nsign = input(\"Enter your sign (+, -, *, /): \")")
f.write("\nnum2 = input(\"Enter your second number: \")")

f.write("\nCalculate(num1, sign, num2)")
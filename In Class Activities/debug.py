###
# Python Debugging Exercise
# Author: Zach Fechko
# Version: 1.0
###

# Identify compile or run-time errors and correct them



def main():
  foo(122, '10')
  bar('cpts')

# The function should return sum of the two input values
def foo(a, b):
  x = int(a)
  y = int(b)

  # Output the sum of inputs 'a' and 'b'
  # Expected output: 132
  print(x + y)

# The function should generate console output as described in the line comments
def bar(s):

  # Concatenate input variable 's', literal '_' and literal '215', and assign it to a variable 'result'
  result = s + '_' + '215'
  # Output the value of 'result' string object to the console
  # Expected output: cpts_215
  print(result)
  # Access each character of 'result' string object and output it to the console. Seperate the charaters using space ('\s')
  # Expected output: c p t s _ 2 1 5
  for x in result:
    print(x, end = ' ') # using '\s' just prints \s instead of an actual space so I used the space character instead

main()

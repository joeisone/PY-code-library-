import argparse


# Two types of arguments
# 1.Positional
# 2.Optional

# Positional arguments

if __name__=='__main__':
  parser=argparse.ArgumentParser()
  parser.add_argument('number1',help="first number")
  parser.add_argument("number2", help="second number")
  parser.add_argument("operation", help="operation",choices=["add","subtract","multiply"])


  args=parser.parse_args()

  print(args.number1)
  print(args.number2)
  print(args.operation)


  n1=int(args.number1)
  n2=int(args.number2)
  result=None

  if args.operation=="add":
    result=n1+n2
  elif args.operation=="substract":
    result=n1-n2
  elif args.operation=="multiply":
    result=n1*n2

  print("Result :",result)

# With positional arguments all the arguments
# are required to be in place.


# Optional argument
# For an optional argument
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--number1', help="first number")
  parser.add_argument("--number2", help="second number")
  parser.add_argument("--operation", help="operation")

  args = parser.parse_args()

  print(args.number1)
  print(args.number2)
  print(args.operation)

  n1 = int(args.number1)
  n2 = int(args.number2)
  result = None

  if args.operation == "add":
    result = n1 + n2
  elif args.operation == "substract":
    result = n1 - n2
  elif args.operation == "multiply":
    result = n1 * n2
  else:
    print("Unsupported operation")
  print("Result :", result)







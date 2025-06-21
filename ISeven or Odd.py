# ISeven or Odd
def isEven(number: int)-> bool:

    if number % 2 == 0:
        return True
    else:
        return False
    
# invocation code
result = isEven(4)

if(result):
    print("number is even")
else:
    print("number is odd")
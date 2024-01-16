from model import *
from template import *


if __name__=="__main__":
    result=eval(f"{num1}{all_arithmetic_operations[operator]}{num2}")
    print(f"{num1} {all_arithmetic_operations[operator]} {num2} = {result}")
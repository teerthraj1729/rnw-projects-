import math

def factorial(n: int)->int:
    if n<0:
        raise ValueError("n must be >=0")
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

def compound_interest(principle:float, rate_pct:float,years: float,comp_per_year:int =1)->float:
     r = rate_pct/100.0
     amount = principle*((1+r/comp_per_year)**(comp_per_year*years))
     return round(amount,2)

def area_circle(radius:float)->float:
    return math.pi*radius*radius

def trig_values(x_radians:float)->float:
    return{
        "sin":math.sin(x_radians),
        "cos":math.cos(x_radians),
        "tan":math.tan(x_radians)
        }



    

#ques 1
num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
sum = num1 + num2
difference = num1 - num2
product = num1*num2
quotient = num1/num2
print(f"sum:",{sum},"difference:",{difference},"product:",{product},"quotient:",{quotient})

#ques2
Celsius = int(input("enter the temperature in celsius?"))
faren = Celsius*(9/5)+32
print("fahrenheit:",faren)

#ques3
r = int(input("enter the radius?"))
pi = 3.14
area = pi*r*r
circumference = 2*pi**r
print("area:",area, "circumference: ",circumference)

#ques4
num = int(input("enter the number: "))
if (num%2==0):
    print("even number")
else:
    print("odd number")
    
#ques5
sentence = input("enter any sentences?")
print(len(sentence))

#간단한 계산기

#함수선언

def add (x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def involution(x,y):
    return x**y
def quotient_remainder(x,y):
    return x//y,x%y
    
#몸체
while True:
    print('=====select operation=====')
    print('0.Exit')
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
    print('5.involution')
    print('6.quotient & remainder')
    

#숫자 입력
    choice= input('Enter choice(0/1/2/3/4/5/6): ')

    if choice == '0':
        break

    if (choice< '0') or (choice > '6') :
        print('Invalid input')
        continue

    num1=float(input('Enter first number: '))
    num2=float(input('Enter second number: '))

    if choice == '1':
        print(num1,'+',num2,'=',add(num1,num2))
    elif choice == '2':
        print(num1,'-',num2,'=',subtract(num1,num2))
    elif choice == '3':
        print(num1,'*',num2,'=',multiply(num1,num2))
    elif choice == '4':
        print(num1,'/',num2,'=',divide(num1,num2))
    elif choice == '5' :
        print(num1,'**',num2,'=',involution(num1,num2))
    else:
        x,y = quotient_remainder(num1,num2)
        print(num1,'/',num2,'=','몫:',x,'&','나머지:',y)


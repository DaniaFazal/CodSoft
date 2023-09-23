class Calculator:
    def add(self ,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def remainder(self,a,b):
        return a%b
    
cal = Calculator()
while True:
    operator = int(input("\nEnter operator number from the following:\n1-ADD\n2-SUBTRACTION\n3-MULTIPLY\n4-DIVISION\n5-MODULUS\n6-EXIT\n"))
    if(operator==6):
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    if(operator==1):
        print("Addition of ",a,"+",b,"is = ",cal.add(a,b))
    elif(operator==2):
        print("Subtraction of ",a,"-",b,"is = ", cal.sub(a,b))
    elif(operator==3):
        print("Multiplication of ",a,"*",b,"is = ", cal.multiply(a,b))
    elif(operator==4):
        if(b==0):
            print("Divion not possible")
        else:
            print("Divison of ",a,"/",b,"is = ", cal.div(a,b))
    elif(operator==5):
        print("Modulus of ",a,"%",b,"is = ", cal.remainder(a,b))
    
    else:
        print("Invalid Operator")
class Calculator:
    def calculate():
        n=1
        while n == 1:
            print(" This is a menu driven program")
            print("1- Division num2- Multiplication num3- Addition num4- Subtraction ")
            num=int(input("Enter your choice: "))
            if num == 1:
                a=float(input("Enter first value :"))
                b=float(input("Enter second value :"))
                print("Division is : ",(a/b))
            elif num==2:
                a=float(input("Enter first value :"))
                b=float(input("Enter second value :"))
                print("Multiplication is : ",(x*y))
            elif num==3 :
                x=float(input("Enter first value :"))
                y=float(input("Enter second value :"))
                print("Addition is : ",(x+y))
            elif num==4:
                x=float(input("Enter first value :"))
                y=float(input("Enter second value :"))
                print("Subtraction is : ",(x-y))
            else:
                print("The given choice is incorrect!!")
            n=input("For continuation press1 \n else press any key ")
            if n!="1":
                exit()
            n1=int(n)
            
    
c=Calculator
c.calculate()


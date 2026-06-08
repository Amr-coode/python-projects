num1 = float(input("Enter Your First Number : " ))
oper = input("choose your operation(+,-,*,%,/,) :" )
num2 = float(input("Enter Your Second Numbwe : " ))


if oper == "+" :
    result = num1+num2
    print (num1, "+", num2,"=",result)

elif oper == "-" :
    result = num1+num2
    print (num1, "-", num2,"=",result)
 
elif oper == "*" :
    result = num1+num2
    print (num1, "*", num2,"=",result)

elif oper == "%" :
    result = num1+num2
    print (num1, "%", num2,"=",result)

elif oper == "/" :
    if num2 != 0 :
        result = num1+num2
        print (num1, "/", num2,"=",result)
    else : 
        print ("can't division by zero")  

else :
    print ("Invaild operation ", oper)

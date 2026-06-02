num1 = float(input("أول رقم: "))
   num2 = float(input("تاني رقم: "))
   op = input("اختار العملية + - * / : ")
   
   if op == "+":
       print("الناتج:", num1 + num2)
   elif op == "-":
       print("الناتج:", num1 - num2)
   elif op == "*":
       print("الناتج:", num1 * num2)
   elif op == "/":
       print("الناتج:", num1 / num2)
   else:
       print("عملية غلط")

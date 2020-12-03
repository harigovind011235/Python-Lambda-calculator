a = True
while a:


    add = lambda a,b:a+b
    sub = lambda a,b:a-b
    mul = lambda a,b:a*b
    div = lambda a,b:a/b


    o1 = int(input("enter the first operand"))
    o2 = int(input("enter the second operand"))

    o = input("enter the operation")

    if o =="":

        print("enter a valid operation")
        break

    if o == "add":

         print(add(o1,o2))

    if o =="sub":

        print(sub(o1,o2))

    if o =="mul":

        print(mul(o1,o2))

    if o =="div":

        print(div(o1,o2))


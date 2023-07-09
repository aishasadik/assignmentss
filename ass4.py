username = str(input("Enter UserName : "))
print(f"WELCOME  {username} ")


def fbreak(x):  #FOR LOOP WITH BREAK cmd
    print("For Loop with using BREAK ")
    for i in d:
     if(i==b):
       break
     else:
       print(i)

def fpass(x):  #FOR LOOP WITH PASS 
    print("For Loop with using PASS ")
    for i in d:
     if(i==b):
       pass
     else:
       print(i)

def fcontinue(x):  #FOR LOOP WITH CONTINUE 
    print("For Loop with using CONTINUE ")
    for i in x:
     if(i==b):
       continue
     else:
       print(i)

def wbreak(a):  #WHILE LOOP WITH BREAK 
    print("While Loop with using BREAK ")
    while a<=5:
     if a==4:
        break
     else:
        print(a)
    a+=1

def wpass(a):  #WHILE LOOP WITH PASS 
    print("While Loop with using PASS ")
    while a<=5:
      if a==4:
        pass
      else:
         print(a)
         a+=1

def wcontinue(a):  #WHILE LOOP WITH CONTINUE 
    print("While Loop with using CONTINUE ")
    while a<=5:
       if a==4:
           a+=1
           continue
       else:
           print(a)
       a+=1

def felsebreak(x):  #FOR LOOP WITH ELSE AND BREAK 
    print("FOR Loop with Else using BREAK ")
    for i in x:
       if(i==b):
          break
       else:
        print(i)
        print(chr(1))
    else:
      print("it has Else block")

def felsepass(x):  #FOR LOOP WITH ELSE AND PASS 
    print("FOR Loop with Else using PASS ")
    for i in x:
        if(i==b):
           pass
        else:
           print(i)
           print(chr(1))
    else:
        print("it has Else block")

def felsecontinue(x):  #FOR LOOP WITH ELSE AND CONTINUE 
    print("FOR Loop with Else using CONTINUE ")
    for i in x:
        if(i==b):
           continue
        else:
           print(i)
           print(chr(1))
    else:
       print("it has Else block")

def welsebreak(a):  #FOR LOOP WITH ELSE AND BREAK 
    print("FOR Loop with Else using BREAK ")
    while a<=5:
        if a==3:
            break
        else:
            print(a)
        a+=1
    else:
        print(chr(2))

def welsepass(a):  #FOR LOOP WITH ELSE AND PASS 
    print("FOR Loop with Else using PASS ")
    while a<=5:
        if a==3:
           a+=1
           pass
        else:
           print(a)
        a+=1
    else:
        print(chr(2))

def welsecontinue(a):  #FOR LOOP WITH ELSE AND CONTINUE 
    print("FOR Loop with Else using CONTINUE ")
    while a<=5:
        if a==3:
           a+=1
           continue
        else:
            print(a)
        a+=1
    else:
       print(chr(2))

print(" ENTER 1 TO SEE FOR LOOP WITH BREAK....! \n ENTER 2 TO SEE FOR LOOP WITH pass....! \n ENTER 3 TO SEE FOR LOOP WITH CONTINUE....! \n ENTER 4 TO SEE WHILE LOOP WITH BREAK....! \n ENTER 5 TO SEE WHILE LOOP WITH PASS....! \n ENTER 6 TO SEE WHILE LOOP WITH CONTINUE....! \n ENTER 7 TO SEE FOR ELSE LOOP WITH BREAK....! \n ENTER 8 TO SEE FOR ELSE LOOP WITH PASS....! \n ENTER 9 TO SEE FOR ELSE LOOP WITH CONTINUE....! \n ENTER 10 TO SEE WHILE ELSE LOOP WITH BREAK....! \n ENTER 11 TO SEE WHILE ELSE LOOP WITH PASS....! \n ENTER 12 TO SEE WHILE ELSE LOOP WITH CONTINUE....!")

ord = int(input("ENTER THE OPERATION NO. TO BE PERFORMED: "))
b = str(input("Enter the String to be passed: "))
c = str(input("Enter the character to break the string: "))
d = int(input("Enter the number to be passed: "))

if ord == 1:
   fbreak(b)
elif ord == 2:
   fpass(b)
elif ord == 3:
   fcontinue(b)
elif ord == 4:
   wbreak(d)
elif ord == 5:
   wpass(d)
elif ord == 6:
   wcontinue(d)
elif ord == 7:
   felsebreak(b)
elif ord == 8:
   felsepass(b)
elif ord == 9:
   felsecontinue(b)
elif ord == 10:
   welsebreak(d)
elif ord == 11:
   welsepass(d)
elif ord == 12:
   welsecontinue(d)
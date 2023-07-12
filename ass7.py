def exceptions(roll_no,name,stud_class, file="data.txt"):
    try:
        f=open(file, "w")
        pass
        f=open(file,"a")
        line=[f"{roll_no}, {name}, {stud_class}"]
        f.writelines(line)
        f=open(file,"r")
        data=f.readlines()
        print("Data is: ")

        print(data)

    except FileNotFoundError:
        print("this is FileNotFound error")

    except Exception:
        print("This is an Exception")
exceptions( "Aisha", "3rd Year")
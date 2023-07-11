#create function named ds with parameters as name and roll no.
name=10
def ds(name="Aisha",roll=44):
    print("name:",name)
    print("roll:",roll)
ds(41)

#adding it in tuple,sets,dict
#tuple
t=()
t1=["name","aisha"]
t2=["roll",44]
print(t1)
print(t2)
#set
s={"roll","name"}
print("set:")
print(s)

#dict
d={"roll:" "roll",
"name:" "name"}
print("dict:")
print(d)

#list
ls=["roll","name"]
print(ls)


#change during run time

#changing list
ls[0]=200
ls[1]="shaikh"
#changing tuple
t=(139,"sara")
#changing set
s.update({"roll":456})
s.update({"name":"welcome"})
#changing dictionary
d.remove("roll")
d.remove("name")
d.add(234)
d.add("python")
#printing updated values
print(ls)
print(t)
print(s)
print(d)
#delete data structures
del ls
del t 
del s
del d
ds(44,"aisha")
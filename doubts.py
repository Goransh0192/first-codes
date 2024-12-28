print(1==2)
print(bool(4>6)==False)
print(bool(True==True==False))
name1=str(input("FIRST NAME"))
name2=str(input("LAST NAME"))        
print(name1+" "+name2)
#major doubt(if else and nested if)
#dont classifying class helps remove errors,instead put the intended result in " "
age=int(input("Enter your age"))
income=int(input("Enter your income"))

if age>=18 or income>=30000:
    print("you are eligble for insurance".title())
    if age<=17:
        print("but grow up first kid".title())
else:
    print("you are not eligble".title())

#dictionary doubt(accessing elements)

dictionary={"name":"goransh","age":18,"city":"jaipur"}
print(dictionary["name"])
print(dictionary["age"])
print(dictionary["city"])

#list doubt(accessing elements) 

   
list1=["apple","banana","orange"]
print(list1[0])
print(list1[1])
print(list1[2])

#tuple doubt(accessing elements)

tuple1=("apple","banana","orange")
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

#set doubt(accessing elements)

set1={"apple","banana","orange"}
print(set1[0])
print(set1[1])
print(set1[2])

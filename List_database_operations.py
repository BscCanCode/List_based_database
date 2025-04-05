print("List_DataBase_Operations")
print("Select what would you like to perform:")
print("1.Insert_Elements\n2.Read_Elements\n3.Update_Elements\n4.Delete_Database\n5.Delete_Elements\n6.Exit")
a=[] #database
while True:
    try:
        n=int(input("Enter your choice: "))
        if n==6:
            print("Exit is success")
            break
        if 0<n<=5:
            if n==1:
                n=int(input("Enter the element to add: "))
                a.append(n)
                print("Element added successfully")
            elif n==2:
                if a:
                    print("Print elements of database: ")
                    print(a)
                else:
                    print("To read elements,first your should add elements")
            elif n==3:
                if a:
                    b=int(input("Enter last updated elements to update: "))
                    if b in a:
                        a.remove(b)
                        print("Elements is removed successfully")
                        c=int(input("Enter new element: "))
                        a.append(c)
                        print("Element is added")
                    else:
                        print("Element not present")
                else:
                    print("Empty:Add something")
            elif n==4:
                d=input("Are you sure you want to delete database? yes/no:")
                if d=="yes":
                    del a
                    print("Database Deleted Successfully")
                elif d=="no":
                    print("Nothing is deleted,chill")
                else:
                    print("Enter proper input")
            elif n==5:
                print("!!!!!!All memory(Elements) will be deleted of database!!!!!!")
                z=input("Are you sure? yes/no: ")
                if z=="yes":
                    a.clear()
                    print("Memory cleared successfully")
                    print(a)
                elif z=="no":
                    print("Nothing Deleted,Chill")
                else:
                    print("Entered input is wrong")
        else:
            print("Enter your choice between 1-6")
    except:
        print("wrong input,try again")
                    
                

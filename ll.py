dis={}
while True:
    print("""
1.add contact
2.change the phonenumber of a contact
3.delete a contact
4.display all contact
5.display all contact in sorted ordr
6.check weather a contact is there r not
7.exit""")
    ch=int(input("Enter a choice : "))
    if ch==1:
        name=input("Enter a name of the friend: ")
        phno=int(input("Enter the phone number of the frend: "))
        dis[name]=phno
        print("Contact added ")
    elif ch==2:
        name=input("Enter the contact name whose phone number to be changed: ")
        if (name in dis):
            phno=int(input("enter the new no of u r friend: "))
            dis[name]=phno
            print("phno changed")
        else:
            print("no contact found in this name")
    elif ch==3:
        name =input("enter the name of the conact to be deleted: ")
        if (name in dis):
            del dis[name]
            print("contact deleted" )
        else:
            print("no contact found in this name")
    elif ch==4:
        print("all contacts")
        for i in dis:
            print(i,"   ",dis[i])
    elif ch==5:
        print("all contact in sorted order")
        for i in sorted(dis.keys()):
            print(i,"   ",dis[i])
    elif ch==6:
        name=input("Enter the name to be searched: ")
        if (name in dis):
           print(dis[name])
        else:
            print("no contact found in this name")
    elif ch==7:
        break
    else:
        print("invalid option selected")
    

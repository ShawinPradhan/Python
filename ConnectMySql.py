import mysql.connector as mc

def add():
    try:
        con=mc.connect(host="localhost",\
                       username="root",database="boot",password="1234")
        name=input("Enter Your Name: ")
        age=int(input("Enter Your Age: "))
        add=input("Enter Your Address: ")
        query="insert into user(name,age,address)\
        values('{0}',{1},'{2}')".format(name,age,add)
        c=con.cursor()
        c.execute(query)
        con.commit()
        print("Data Saved Successfully")
        con.close()
    except:
        con.rollback()
        print("Error Found")
        
def display():
    con=mc.connect(host="localhost",\

                       username="root",database="boot",password="1234")
    query="select * from user"
    c=con.cursor()
    c.execute(query)
    for i in c.fetchall():
        print(i)
    con.close()

def update():
    try:
        con=mc.connect(host="localhost",\
                           username="root",database="boot",password="1234")
        c=con.cursor()
        id = int(input("Enter id to update: "))
        name=input("Enter Your Name: ")
        age=int(input("Enter Your Age: "))
        add=input("Enter Your Address: ")
        query="UPDATE user SET name = %s, age = %s, address= %s WHERE id = %s"
        data = (name,age,add,id)
        c.execute(query,data)
        con.commit()
        print("Data Updated Successfully")
        con.close()
    except:
        con.rollback()
        print("Error Found")

def delete(user_id):
    try:
        con=mc.connect(host="localhost",\
                           username="root",database="boot",password="1234")
        c=con.cursor()
        query = "delete from user where id=%s"
        data = (user_id,)
        c.execute(query,data)
        con.commit()
        print("User details with id "+str(user_id)+" deleted successfully")
        con.close()
    except:
        con.rollback()
        print("Error Found")
    

def main():
    print("1. For Insert record")
    print("2. For Display All Record")
    print("3. To update Record")
    print("4. To delete Record using id")
    print("5. For Quit")
    op=int(input("Select Any Option "))
    if op==1:
        add()
    elif op==2:
        display()
    elif op==3:
        update()
    elif op==4:
        user_id = int(input("Enter user id to delete: "))
        delete(user_id)
    elif op==5:
        exit()
    else:
        print("Invalid Options")

while True:
    main()

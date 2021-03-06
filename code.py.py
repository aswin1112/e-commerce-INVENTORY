from tkinter import *
import mysql.connector
from tabulate import tabulate
import matplotlib as plt
root = Tk()
root.geometry('925x500+200+100')
root.title('L O G I N')
root.configure(bg="#fff")
root.resizable(0,0)

def logintodb(sellerId,passw):
    if passw:
        db = mysql.connector.connect(host='localhost',user= 'root', password='Aswin@123', db='Inventory')
        cursor = db.cursor()
    else:
        db = mysql.connector.connect(host="localhost",user=user, db="College")
        cursor = db.cursor()
    savequery = "SELECT O.ProductId as ProductId , P.Product_name as Product_name, count(O.OrderID) as No_Of_Orders, sum(O.profit) as Profit, P.Availability,P.rating FROM order_details O  INNER Join product P ON O.ProductId = P.Product_ID GROUP BY O.ProductId;"

    try:
        cursor.execute(savequery)
        a=cursor.fetchall()
        table = tabulate(a, headers=['ProductId', 'Product_name', 'No_of_Orders', 'Profit', 'Availability', 'rating'],tablefmt='fancy_grid')
        print(table)


        # Printing the result of the
        # query

    except:
        db.rollback()
        print("Error occured")

def signin():
    sellerId = user.get()
    password = code.get()

    logintodb(sellerId, password)

img = PhotoImage(file='images.png')
Label(root,image=img, bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading = Label(frame,text = 'Sign In', fg='#57a1f8',bg='white',font = ('Microsoft YaHei UI Light',23))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'SellerId')
user = Entry(frame, width=25, fg='black', border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=60,y=65)
user.insert(0,'SellerId')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=60,y=90)

heading2 = Label(frame,text = 'Password', fg='#57a1f8',bg='white',font = ('Microsoft YaHei UI Light',23))
heading2.place(x=90,y=110)

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code = Entry(frame, width=25, fg='black', border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=60,y=160)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=60,y=185)

Button(frame,width=19,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=100,y=210)
label=Label(frame,text="Dont't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=260)

sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=235,y=260)
root.mainloop()



import tkinter
import mysql.connector
from tkinter import ttk
from tkcalendar import DateEntry

import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="homestay_booking")

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

window = tkinter.Tk()
window.title ("Data entry form")

frame = tkinter.Frame(window)
frame.pack()

# Saving Customer Information
user_info_frame = tkinter. LabelFrame (frame, text = "Customer Information", bg='PapayaWhip')
user_info_frame.grid (row= 0, column= 0, padx=30 , pady=30)

title_Label = tkinter.Label(user_info_frame, text= "Title",bg="orange")
title_combobox = ttk.Combobox (user_info_frame, values = ["Mr.", "Mrs.","Miss"])
title_Label.grid(row= 2, column= 0,padx=10,pady=10)
title_combobox.grid(row= 2, column= 1)

name_label= tkinter.Label(user_info_frame, text = "Name",bg="orange")
name_label.grid (row= 3, column=0,padx=10,pady=10 )
name_entry=tkinter.Entry(user_info_frame)
name_entry.grid(row= 3 , column= 1)

phone_Label = tkinter.Label(user_info_frame, text= "Phone Number",bg="orange")
phone_Label.grid(row= 4, column= 0,padx=10,pady=10)
phone_entry=tkinter.Entry(user_info_frame)
phone_entry.grid(row= 4 , column= 1)

#Date Check-in 
date_label= tkinter.Label(user_info_frame, text = "Date Check-In",bg="orange")
date_label.grid (row= 6, column= 0,padx=10,pady=10)

def my_in(*args):
    l1.config(text=ddt.get())
ddt= tkinter.StringVar()

cal1=DateEntry(user_info_frame, selectmode= 'day', textvariable=ddt)
cal1.grid(row=7, column=0)

l1=tkinter.Label(user_info_frame, bg='pink')
l1.grid(row=5,column=0)

ddt.trace('w', my_in)

#Date Check-out
out_label= tkinter.Label(user_info_frame, text = "Date Check-Out",bg="orange")
out_label.grid (row= 6, column= 1,padx=10,pady=10)

def my_date(*args):
    l2.config(text=sel.get())
sel= tkinter.StringVar()

cal2=DateEntry(user_info_frame, selectmode= 'day', textvariable=sel)
cal2.grid(row=7, column=1)

l2=tkinter.Label(user_info_frame, bg='red')
l2.grid(row=5,column=1)

sel.trace('w', my_date)
  
 #Homestay price
homestay_label=tkinter.Label(user_info_frame,text="Homestay",bg="orange")
homestay_label.grid (row= 8, column= 0,padx=10,pady=10)
breakfast_label=tkinter.Label(user_info_frame, text= "Breakfast",bg="orange")
breakfast_label.grid (row= 8, column= 1,padx=10,pady=10)

homestay=tkinter.IntVar()
breakfast=tkinter.IntVar()

homestay_quantity = tkinter.Entry(user_info_frame,textvariable=homestay)
homestay_quantity.grid(row= 9,column= 0)
breakfast_quantity = tkinter.Entry (user_info_frame, textvariable=breakfast)
breakfast_quantity.grid(row= 9,column= 1)

#Calculation 
def total():
    homestay=int (homestay_quantity.get())*155
    breakfast= int(breakfast_quantity.get())*20
    
    if homestay == 'Only homestay':
        price= homestay
    elif breakfast == 'Add breakfast':
        add= homestay + breakfast
        price=add
    else :
        
    #Offer
        if  homestay+ breakfast > 250:
                all_total= (homestay+ breakfast) * 80/100 # 20% discount for price more than 250
        else:
                all_total= (homestay + breakfast)

        print('RM', all_total)
        empty_label.config(text= f"Your Total: RM {all_total}")
        
    # To insert your Data to your database, As for this example, you have 3 attributes. (2 Attributes from your selection (Package, Pack) and another attributes that derived from your attributes (price))
    sql = "INSERT INTO customer_information (Title_Label,Name_label,Phone_Label,Date_label,Out_label,Homestay_quantity,Breakfast_quantity,Total) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
    val = (title_combobox.get(),name_entry.get(),phone_entry.get(),cal1.get(),cal2.get(),homestay_quantity.get(),breakfast_quantity.get(),all_total)
    mycursor.execute(sql, val)
    mydb.commit()

button_submit=tkinter.Button(user_info_frame,text= 'Submit',command=total)
button_submit.grid(row=11,column=0,padx=10,pady=10)

empty_label=tkinter.Label(user_info_frame)
empty_label.grid(row=11,column=1)
    
# Prices List by using textbox
prices_text = tkinter.Text(user_info_frame, height=8, width=20,bg="DarkSalmon")
prices_text.grid(row=1,column= 0)

# The defined list by using pricebox
prices_text.insert(tkinter.END, "Homestay Prices\n\n")
prices_text.insert(tkinter.END, " 1 Homestay \nPrice: RM155\n\n")
prices_text.insert(tkinter.END, " Add your breakfast \nPrice: RM20\n\n")
prices_text.configure(state='disabled')

window.mainloop()


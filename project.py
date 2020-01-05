#!/usr/bin/python3

import sqlite3

def connect():
    conn=sqlite3.connect("1.db")
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name TEXT, email_addr VARCHAR, ph_number INTEGER, num_of_days INTEGER, total INTEGER)''')
    conn.commit()
    conn.close()

def insert(name,email_addr,ph_number, num_of_days):
    conn=sqlite3.connect("1.db")
    cur=conn.cursor()
    cur.execute("insert into test values(null,?,?,?,?,?)",(name, email_addr, ph_number, num_of_days, calculator(num_of_days)))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("1.db")
    cur=conn.cursor()
    cur.execute("select * from test")
    row=cur.fetchall()
    conn.close()
    print(row)

def search(a,b,c):
    conn=sqlite3.connect("1.db")
    cur=conn.cursor()    
    cur.execute("select * from test where name=? or ph_number=? or num_of_days = ?",(a,b,c))
    row=cur.fetchall()
    conn.close()
    print(row)

def edit(a,b,c):
    conn=sqlite3.connect("1.db")
    cur=conn.cursor()    
    cur.execute("select * from test where name = ? or ph_number=? or num_of_days = ?",(a,b,c))
    row=cur.fetchall()
    index=row[0][0]

    x=input("enter your edited name : ")
    y=input("enter your edited number : ")
    z=input("enter edited num_of_days : ")    
    cur.execute("update test set name=?, ph_number = ?, num_of_days=?, total=? where id =?",(x,y,z, calculator(z), index))
    conn.commit()
    conn.close()

def delete(name,ph_number, num_of_days):
    conn=sqlite3.connect("1.db")
    cur=conn.cursor()    
    cur.execute("select * from test where name = ? or ph_number=? or num_of_days = ?",(a,b,c))
    row=cur.fetchall()
    index=row[0][0]
    cur.execute("delete from test where id=?",(index,))
    conn.commit()
    conn.close()

def calculator(num_of_days):
    total=1000*num_of_days
    return total

def show_emails():
    conn=sqlite3.connect("1.db")
    cur=conn.cursor()    
    cur.execute("select email_addr from test")
    while True:
        row=cur.fetchone()

        if row == None:
            break
        print(row[0])

def send_announce_email():
    conn=sqlite3.connect("1.db")
    cur=conn.cursor()    
    cur.execute("select email_addr from test")
    email_addrs=[]
    while True:
        row=cur.fetchone()
        if row == None:
            break
        email_addrs.append(row[0])
    print("Sending email to: ")
    print(email_addrs)
    
    import smtplib
    # list of email_id to send the mail 
    for i in range(len(email_addrs)):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(SENDER_EMAIL_ID,SENDER_EMAIL_PASSWORD)
        message = "This is a test annoncement email."
        s.sendmail(SENDER_EMAIL_ID,email_addrs[i],message)
        s.quit()


if __name__ == "__main__":
    connect()

option=int(input('''what do you want to do: 
1. Add/modify the database.
2. List the email address of students
3. Send announcement email to students.
> '''))

if option==1:
    option2=int(input('''1) insert entity     2) view all     3) edit     4) delete     5) search
    > '''))
    if option2==1:
        a=str(input("enter your name : "))
        b=int(input("enter your number:"))
        c=int(input("enter num_of_days : "))
        d=input("enter your email address:")
        insert(a,d,b,c)

    elif option2==2:
        view()

    elif option2==5:
        a=input("enter your name : ")
        b=input("enter your number : ")
        c=input("enter num_of_days : ")
        search(a,b,c)

    elif option2==3:
        a=input("enter your name : ")
        b=input("enter your number : ")
        c=input("enter num_of_days : ")
        edit(a,b,c)

    elif option2==4:
        a=input("enter your name : ")
        b=input("enter your number : ")
        c=input("enter num_of_days : ")
        delete(a,b,c)
        
elif option==2:
    show_emails()

elif option==3:
    # Enable less secure app access before running here: https://myaccount.google.com/lesssecureapps
    SENDER_EMAIL_PASSWORD='changeme'
    SENDER_EMAIL_ID='changeme@example.com'
    send_announce_email()
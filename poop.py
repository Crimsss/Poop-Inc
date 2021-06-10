from tkinter import *
import sqlite3
import time

found = 0


conn = sqlite3.connect('logins.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS logins (
                user text,
                password text
                )""")


def firstp():
    global myLogin
    global myCreate
    global myWord
    myLogin = Button(root, text="Login", command=pagetwo,justify='center')
    myCreate = Button(root, text="Create An Account", command=pagethree,padx = 40)
    myWord = Label(root, text="Or",padx = 40)

    myLogin.config(anchor=CENTER)
    myLogin.pack()
    myWord.config(anchor=CENTER)
    myWord.pack()
    myCreate.config(anchor=CENTER)
    myCreate.pack()

##    myLogin.grid(row=0,column=2)
##    myCreate.grid(row=2,column=2)
##    myWord.grid(row=1, column=2)



def getInfo():

    userN = str(user.get())
    password = str(passw.get())
    search(userN, password)
    


def search(userN, password):
        c.execute("SELECT * FROM logins WHERE user = ? AND password = ?", (userN, password))
        userPass = c.fetchone()
        if userPass:
            global accFound
            found = 1
            loginW()
            
        else:
            again()


def loginW():
    global passw
    global passwL
    global user
    global userN
    global userL
    global mySignin
    global userpassWarn
    global notFound
    global accnotFound

    if notFound == 1:
        accnotFound.destroy()
    else:
        pass
    
    passw.destroy()
    passwL.destroy()
    user.destroy()
    userL.destroy()
    mySignin.destroy()
    userpassWarn.destroy()

    
    welc = Label(root,text="Account found, login successful")
    welc.config(anchor=CENTER)
    welc.pack()
    welc2 = Label(root,text="Welcome back to")
    welc2.config(anchor=CENTER)
    welc2.pack()
    welc3 = Label(root,text="Poop Incorporated")
    welc3.config(anchor=CENTER)
    welc3.pack()
    
    

def again():
    global accnotFound
    global notFound
    notFound = 0
    accnotFound = Label(root, text ="Account not found, try again")
    notFound = 1
    accnotFound.grid(row=4, column=0, columnspan = 3)
    user.delete(0, END)
    passw.delete(0, END)


def pagetwo():
    root.title("POOP Inc: Login")
    myCreate.destroy()
    myLogin.destroy()
    myWord.destroy()
    global user
    global userL
    global passw
    global passwL
    global mySignin
    global userpassWarn
    

    userpassWarn = Button(root, text="Please beware passwords are case sensitive.", padx=40, pady=3)
    userpassWarn.grid(row=0,column=0,columnspan=3)

    user = Entry(root, width=40, borderwidth = 5)
    userL = Label(root, text="Username:")
    user.grid(row=1,column=1,columnspan = 2)
    userL.grid(row=1,column=0,)

    passw = Entry(root, width=40, borderwidth = 5)
    passwL = Label(root, text="Password:")
    passw.grid(row=2,column=1,columnspan=2)
    passwL.grid(row=2,column=0)

    mySignin = Button(root, text="Sign in", padx=10, pady=10, command= getInfo)
    mySignin.grid(row=3,column=1)

def pagethree():
    root.title("POOP Inc: create an account")
    myCreate.destroy()
    myLogin.destroy()
    myWord.destroy()
    global passw
    global passwL
    global user
    global userL
    global mySignin
    global passReq

    passReq = Button(root, text="Password must be 8 letters/numbers long.", padx=40, pady=3)
    passReq.grid(row=0,column=0,columnspan=3)

    
    user = Entry(root, width=40, borderwidth = 5)
    userL = Label(root, text="Username:")
    user.grid(row=1,column=1,columnspan = 2)
    userL.grid(row=1,column=0,)

    passw = Entry(root, width=40, borderwidth = 5)
    passwL = Label(root, text="Password:")
    passw.grid(row=2,column=1,columnspan=2)
    passwL.grid(row=2,column=0)

    mySignin = Button(root, text="Create Account", padx=10, pady=10, command= usernameSearch)
    mySignin.grid(row=3,column=1)

def usernameSearch():
    global passW
    global checker
    global userPoop
    global userAvail
    userN = str(user.get())
    passW = str(user.get())
    userPoop = 0
    
    
    c.execute("SELECT * FROM logins WHERE user= ?", (userN,)) 
    userExist = c.fetchall()
    if userExist:
        userAvail = Label(root, text="Sorry, that username is unavailable")
        userAvail.grid(row=4,column=0,columnspan=3)
        userPoop = 1
    else:
        passcheck()
        if checker == 1:
            AccountYes()
        else:
            pass

def createW():
    global passw
    global passwL
    global user
    global userN
    global userL
    global mySignin
    global passReq
    global userPoop
    global userAvail
    
    if userPoop == 1:
        userAvail.destroy()
    else:
        pass 
    
    passw.destroy()
    passwL.destroy()
    user.destroy()
    userL.destroy()
    mySignin.destroy()
    passReq.destroy()
    welc = Label(root,text="Account created successfully,")
    welc.config(anchor=CENTER)
    welc.pack()
    welc2 = Label(root,text="Welcome")
    welc2.config(anchor=CENTER)
    welc2.pack()
    welc3 = Label(root,text="Poop Incorporated")
    welc3.config(anchor=CENTER)
    welc3.pack()
    space = Label(root, text="                                                                    ")
    space.config(anchor=CENTER)
    space.pack()
    
def AccountYes():
        global userN
        global passW
        userN = str(user.get())
        passW = str(passw.get())
    
        c.execute("INSERT INTO logins VALUES(?, ?)", (userN, passW))
        conn.commit()
        conn.close()
        createW()

        
def passcheck():
    global checker
    global passW
    global passw
    global check2
    global badPass
    
    passW = str(passw.get())
    print(len(passW))
    if len(passW) < 8:
        badPass = Label(root, text="    Password does not meet the requirements     ")
        badPass.grid(row=4, column=0, columnspan = 3)
        checker = 0
        check2 = 1
    elif len(passW) >= 8:
        if "check2" in globals():
            badPass.destroy()
            print("bruh")
        else:
            pass
            
        checker = 1
        pass
        
        



def logged_in(): 
    pass

root = Tk()
root.geometry("313x150")
root.resizable(False, False)
root.title("POOP Inc")
firstp()
root.mainloop()



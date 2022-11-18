from tkinter import *
root = Tk()

def getvals():
    print("Accepted")

#Size of the Frame
root.geometry("500x300")

Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)

#Creating Field Name
name = Label(root, text="Name", font="ar 10 bold")
phone = Label(root, text="Phone", font="ar 10 bold")
gender = Label(root, text="Gender", font="ar 10 bold")
emergency = Label(root, text="Emergency", font="ar 10 bold")
paymentmode = Label (root, text="Payment Mode", font="ar 10 bold")

#Packing Name Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

#Variable for storing Data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

#Creating Entry Fields
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)
emergencyentry = Entry(root, textvariable = emergencyvalue)
paymentmodeentry = Entry(root, textvariable = paymentmodevalue)

#Packing Entry Fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

#Creating Checkbox
checkbtn = Checkbutton(text="remember me?", font="ar 8 bold", variable = checkvalue)
checkbtn.grid(row=6, column=3)

#Submit Button
Button(text="Submit", command=getvals).grid(row=7, column=3)
root.mainloop() 
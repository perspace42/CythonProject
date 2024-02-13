import tkinter as tk #shorten any calls to tkinter
from CythonApplication import pyValidateNumber as validateNumber #using Cython import the C++ validateNumber function
from tkinter import simpledialog #import the dialog box to enter tips into
from tkinter import messagebox #import the error message box

#Function To Validate Input String From User For Custom Tip Value
def validateInputString(input):
    #First Test If The Input Is A Number
    try:
        value = float(input)
    except:
        messagebox.showerror("Tip Value is Not A Number", "The supplied tip value is not a number please try again")
        return False
    #Next Test If The Input Is A Valid Number
    else:
        if (validateNumber(value)):
            return True
        else:
            messagebox.showerror("Tip Value is Invalid", "The supplied tip value is invalid please try agian")
            return False

#Dialog Box from which user can enter a custom tip value
class CustomTipDialog(simpledialog.Dialog):
    def __init__(self, parent, title = "Tip Value"):
        self.parent = parent
        super().__init__(parent,title)

    def body(self, master):
        tk.Label(master, text="Enter a custom tip $ value:").grid(row=0)
        self.valueEntry = tk.Entry(master)
        self.valueEntry.grid(row=0, column=1)
        return self.valueEntry

    #This method checks the data when ok is pressed (Returning true if valid, and false otherwise)
    def validate(self):
        self.tip = self.valueEntry.get()
        return validateInputString(self.tip)  

    #This method gets called if validate() returns True
    def apply(self):
        #Add Tip To Total
        self.parent.total += float(self.tip)
        #Force Truncation Using Round Function
        self.parent.total = round(self.parent.total,2)
        #Communicate Total To User
        self.parent.resultsLabel.config(text = "Your total is now " + str(self.parent.total))
        
#Class To Draw The Application
class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Set Window Size and Name
        self.geometry("375x200")
        self.title("Tip Application")
        #Set Widgets Variables For Window
        self.messageLabel = tk.Label(text = "Please Select Your Tip Amount")
        self.billLabel = tk.Label(self,text = "")
        self.tipTenPercentBtn = tk.Button(self, text="Tip 10%")
        self.tipFifteenPercentBtn = tk.Button(self,text = "Tip 15%")
        self.tipTwentyPercentBtn = tk.Button(self,text = "Tip 20%")
        self.tipCustomValueBtn = tk.Button(self,text = "Tip Custom")
        self.resultsLabel = tk.Label(text = "")

        #set application example bill and tax amounts
        self.billamount = 112.58
        self.taxamount = 0.05

        #get the total from the bill + tax
        self.total = self.billamount * self.taxamount + self.billamount
        #round to two decimal places
        self.total = round(self.total,2)
        #initialize initial tip value to zero
        self.tip = 0

    #Draw the current bill on the screen
    def showBill(self):
        #Show the bill amount
        message = "The bill of subtotal: " + str(self.billamount) + " + " + " tax of: " + str((self.taxamount * 100)) + '%' + " is: " + str(self.total)
        #Place the amount on the message
        self.messageLabel.config(text = message)

    #Define Custom Tip Entry Button Function
    def onCustomTipBtnClick(self):
        #Create The Dialog
        dialog = CustomTipDialog(self)
        
                  
    #Define Regular Tip Entry Button Function
    def onPercentTipBtnClick(self,percent):
        #find the tip amount
        self.tip = self.total * percent
        #add the tip to the total
        self.total = self.total + self.tip
        #round the tip to 2 decimal places
        self.total = round(self.total,2)
        #communicate the results to the user
        self.resultsLabel.config(text = "Your total is now: " + str(self.total))

    #Initialize the program as it should be on startup
    def setup(self):
        #place the widgets
        self.messageLabel.grid(row = 0, column = 1)
        self.billLabel.grid(row = 1, column = 0, columnspan = 3)
        self.tipTenPercentBtn.grid(row = 2,column = 0)
        self.tipFifteenPercentBtn.grid(row = 2,column = 1)
        self.tipTwentyPercentBtn.grid(row = 2,column = 2)
        self.tipCustomValueBtn.grid(row = 3,column = 0, columnspan = 3)
        self.resultsLabel.grid(row = 4,column = 0 , columnspan = 3)
        #then draw the widgets
        self.showBill()
        #Assign Commands To Buttons
        self.tipTenPercentBtn.configure(command = lambda: self.onPercentTipBtnClick(0.10))
        self.tipFifteenPercentBtn.configure(command = lambda: self.onPercentTipBtnClick(0.15))
        self.tipTwentyPercentBtn.configure(command = lambda: self.onPercentTipBtnClick(0.20))
        self.tipCustomValueBtn.configure(command = lambda: self.onCustomTipBtnClick())
        #start the application llop
        self.mainloop()






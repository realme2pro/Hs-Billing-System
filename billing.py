from tkinter import*
import random
import time
import datetime

width = 1850
height = 750

root = Tk()
root.geometry(str(width)+"x" + str(height) + "+0+0")
root.title("Hs Billing Systems")

Tops = Frame(root, width=width, height=100, bd=8,relief='raise')
Tops.pack(side=TOP)

#main-frame
f1 = Frame(root, width=900, height=650, bd=8,relief='raise')
f1.pack(side=LEFT)
f2 = Frame(root, width=450, height=650, bd=8,relief='raise')
f2.pack(side=LEFT)
#sub-frame
f1a = Frame(f1, width=900, height=330, bd=8,relief='raise')
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=8,relief='raise')
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=430, bd=8,relief='raise')
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=8,relief='raise')
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=8,relief='raise')
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=8,relief='raise')
f2ab.pack(side=LEFT)

lblInfo=Label(Tops, font=('arial',60,'bold'),text ="Hs Billing systems", bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

#============
# CALCULATOR
#============
#I should've defined all of the variables associated with StringVar() here

#calculator's screen
text_Input=StringVar()
operator=""

def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator=''
	text_Input.set('')

def btnEqualsInput():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator=''

#calculator's buttons
txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input,bd=40, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)
#----------------------------------------------------
btn7 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',command=lambda:btnClick(7)).grid(row=1,column=0)
btn8 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',command=lambda:btnClick(8)).grid(row=1,column=1)
btn9 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',command=lambda:btnClick(9)).grid(row=1,column=2)
btnPlus = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='+',command=lambda:btnClick("+")).grid(row=1,column=3)
#----------------------------------------------------
btn4 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',command=lambda:btnClick(6)).grid(row=2,column=2)
btnSub = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='-',command=lambda:btnClick("-")).grid(row=2,column=3)
#----------------------------------------------------
btn1 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',command=lambda:btnClick(1)).grid(row=3,column=0)
btn2 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',command=lambda:btnClick(2)).grid(row=3,column=1)
btn3 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',command=lambda:btnClick(3)).grid(row=3,column=2)
btnMult = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='*',command=lambda:btnClick("*")).grid(row=3,column=3)
#----------------------------------------------------
btn0 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='c',command=btnClearDisplay).grid(row=4,column=1)
btnEqual = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='=',command=btnEqualsInput).grid(row=4,column=2)
btnDiv = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='/',command=lambda:btnClick("/")).grid(row=4,column=3)

#==============
# ORDER's INFO
#==============
PaymentRef=StringVar()
Realme2Pro=StringVar()
Pizza=StringVar()
Mac=StringVar()
MyHomeDelivery=StringVar()

Realme2Pro.set(17990)
Pizza.set(0)
Mac.set(0)
MyHomeDelivery.set(0)

lblRef = Label(f1aa,font=('arial',16,'bold'),text='Sales Reference',bd=16,justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa,font=('arial',16,'bold'),textvariable=PaymentRef,bd=10,insertwidth=2,justify='left')
txtRef.grid(row=0,column=1)

lblRealme2Pro = Label(f1aa,font=('arial',16,'bold'),text='Realme2Pro',bd=16,justify='left')
lblRealme2Pro.grid(row=1,column=0)
txtRealme2Pro=Entry(f1aa,font=('arial',16,'bold'),textvariable=Realme2Pro,bd=10,insertwidth=2,justify='left')
txtRealme2Pro.grid(row=1,column=1)

lblPizza = Label(f1aa,font=('arial',16,'bold'),text='Pizza',bd=16,justify='left')
lblPizza.grid(row=2,column=0)
txtPizza=Entry(f1aa,font=('arial',16,'bold'),textvariable=Pizza,bd=10,insertwidth=2,justify='left')
txtPizza.grid(row=2,column=1)

lblMac = Label(f1aa,font=('arial',16,'bold'),text='Mac',bd=16,justify='left')
lblMac.grid(row=3,column=0)
txtMac=Entry(f1aa,font=('arial',16,'bold'),textvariable=Mac,bd=10,insertwidth=2,justify='left')
txtMac.grid(row=3,column=1)

lblMyHomeDelivery= Label(f1aa,font=('arial',16,'bold'),text='MyHome Delivery',bd=16,justify='left')
lblMyHomeDelivery.grid(row=4,column=0)
txtMyHomeDelivery=Entry(f1aa,font=('arial',16,'bold'),textvariable=MyHomeDelivery,bd=10,insertwidth=2,justify='left')
txtMyHomeDelivery.grid(row=4,column=1)


#==============
# ORDER's COST
#==============
DateofOrder=StringVar()
CostofRealme2Pro=StringVar()
CostofPizza=StringVar()
CostofMac=StringVar()
CostofMyHomeDelivery=StringVar()

DateofOrder.set(time.strftime("%d/%m/%y"))

lblDateofOrder = Label(f1ab,font=('arial',16,'bold'),text='Order Date',bd=16,anchor='w')
lblDateofOrder.grid(row=0,column=0)
txtDateofOrder=Entry(f1ab,font=('arial',16,'bold'),textvariable=DateofOrder,bd=10,insertwidth=2,justify='left')
txtDateofOrder.grid(row=0,column=1)

lblCostofRealme2Pro = Label(f1ab,font=('arial',16,'bold'),text='Carpets Cost',bd=16,anchor='w')
lblCostofRealme2Pro.grid(row=1,column=0)
txtCostofRealme2Pro=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofRealme2Pro,bd=10,insertwidth=2,justify='left')
txtCostofRealme2Pro.grid(row=1,column=1)


lblCostofPizza = Label(f1ab,font=('arial',16,'bold'),text='Pizza Cost',bd=16,anchor='w')
lblCostofPizza.grid(row=2,column=0)
txtCostofPizza=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofPizza,bd=10,insertwidth=2,justify='left')
txtCostofPizza.grid(row=2,column=1)

lblCostofMac = Label(f1ab,font=('arial',16,'bold'),text='Mac Cost',bd=16,anchor='w')
lblCostofMac.grid(row=3,column=0)
txtCostofMac=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofMac,bd=10,insertwidth=2,justify='left')
txtCostofMac.grid(row=3,column=1)

lblMyHomeDelivery= Label(f1ab,font=('arial',16,'bold'),text='Delivery Cost ',bd=16,anchor='w')
lblMyHomeDelivery.grid(row=4,column=0)
txtMyHomeDelivery=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofMyHomeDelivery,bd=10,insertwidth=2,justify='left')
txtMyHomeDelivery.grid(row=4,column=1)

#=================
# ORDER's SUMMARY
#=================
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()

lblPaidTax = Label(f2aa,font=('arial',16,'bold'),text='Paid Tax',bd=8,anchor='w')
lblPaidTax.grid(row=2,column=0)
txtPaidTax = Entry(f2aa,font=('arial',16,'bold'),textvariable=PaidTax,bd=8,insertwidth=2,justify='left')
txtPaidTax.grid(row=2,column=1)

lblSubTotal = Label(f2aa,font=('arial',16,'bold'),text='Sub Total',bd=8,anchor='w')
lblSubTotal.grid(row=3,column=0)
txtSubTotal = Entry(f2aa,font=('arial',16,'bold'),textvariable=SubTotal,bd=8,insertwidth=2,justify='left')
txtSubTotal.grid(row=3,column=1)

lblTotalCost = Label(f2aa,font=('arial',16,'bold'),text='Total Cost',bd=8,anchor='w')
lblTotalCost.grid(row=4,column=0)
txtTotalCost = Entry(f2aa,font=('arial',16,'bold'),textvariable=TotalCost,bd=8,insertwidth=2,justify='left')
txtTotalCost.grid(row=4,column=1)

#=====================
# ORDER's INFO BUTTONS
#=====================
from tkinter import messagebox

def iExit():
	qExit = messagebox.askyesno("Billing system","Do you want to exit the system?")
	if qExit > 0:
		root.destroy()
		return

def Reset():
	PaymentRef.set("")
	Realme2Pro.set(17990)
	Pizza.set()
	Mac.set()
	MyHomeDelivery.set(0)
	PaidTax.set("")
	SubTotal.set("")
	TotalCost.set("")
	CostofRealme2Pro.set("17990")
	CostofPizza.set("0")
	CostofMac.set("0")
	CostofMyHomeDelivery.set("")

def PayReference():
	x = random.randint(10034,699812)
	randomRef = str(x)
	PaymentRef.set("BILL"+randomRef)

def CostOfOrder():
	Realme2ProPrice = float(Realme2Pro.get())
	PizzaPrice = float(Pizza.get())
	MacPrice = float(Mac.get())
	DeliveryCost = float(MyHomeDelivery.get())
	
	Realme2ProCost = "INR " + str("%.2f"%((Realme2ProPrice*15.49)))
	CostofRealme2Pro.set(Realme2ProCost)
	
	PizzaCost = "INR " + str("%.2f"%((PizzaPrice*7.49)))
	CostofPizza.set(PizzaCost)
	
	MacCost = "INR " + str("%.2f"%((MacPrice*5.50)))
	CostofMac.set(MacCost)
	
	Delivery = "INR " + str("%.2f"%((DeliveryCost*4.50)))
	CostofMyHomeDelivery.set(Delivery)
	
	ToC = "INR " + str("%.2f"%((Realme2ProPrice*15.49)+(PizzaPrice*7.49)+(MacPrice*5.50)+(DeliveryCost*4.50)))
	SubTotal.set(ToC)
	
	Tax = "INR " + str("%.2f"%(((Realme2ProPrice*15.49)+(PizzaPrice*7.49)+(MacPrice*5.50)+(DeliveryCost*4.50))*0.2))
	PaidTax.set(Tax)
	
	TaxPay = (((Realme2ProPrice*15.49)+(PizzaPrice*7.49)+(MacPrice*5.50)+(DeliveryCost*4.50))*0.2)
	Cost = (((Realme2ProPrice*15.49)+(PizzaPrice*7.49)+(MacPrice*5.50)+(DeliveryCost*4.50)))
	CostofItems = "INR " + str("%.2f"%(TaxPay+Cost))
	TotalCost.set(CostofItems)
	
	x=random.randint(10034,699812)
	randomRef=str(x)
	PaymentRef.set("BILL"+randomRef)
		

btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Total Cost', command = CostOfOrder).grid(row=0,column=0)

btnRefer=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Sales Reference', command=PayReference).grid(row=0,column=1)

btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Reset',command=Reset).grid(row=1,column=0)

btnExit=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Exit',command=iExit).grid(row=1,column=1)



root.mainloop()

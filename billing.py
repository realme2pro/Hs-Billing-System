from tkinter import*
import random
import time
import datetime

width = 1350
height = 650

root = Tk()
root.geometry(str(width)+"x" + str(height) + "+0+0")
root.title("Billing Systems")

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

lblInfo=Label(Tops, font=('arial',60,'bold'),text ="Billng systems", bd=10,anchor='w')
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
Carpets=StringVar()
Fabric=StringVar()
Blinds=StringVar()
HomeDelivery=StringVar()

Carpets.set(0)
Fabric.set(0)
Blinds.set(0)
HomeDelivery.set(0)

lblRef = Label(f1aa,font=('arial',16,'bold'),text='Sales Reference',bd=16,justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa,font=('arial',16,'bold'),textvariable=PaymentRef,bd=10,insertwidth=2,justify='left')
txtRef.grid(row=0,column=1)

lblCarpets = Label(f1aa,font=('arial',16,'bold'),text='Carpets',bd=16,justify='left')
lblCarpets.grid(row=1,column=0)
txtCarpets=Entry(f1aa,font=('arial',16,'bold'),textvariable=Carpets,bd=10,insertwidth=2,justify='left')
txtCarpets.grid(row=1,column=1)

lblFabric = Label(f1aa,font=('arial',16,'bold'),text='Fabric',bd=16,justify='left')
lblFabric.grid(row=2,column=0)
txtFabric=Entry(f1aa,font=('arial',16,'bold'),textvariable=Fabric,bd=10,insertwidth=2,justify='left')
txtFabric.grid(row=2,column=1)

lblBlinds = Label(f1aa,font=('arial',16,'bold'),text='Blinds',bd=16,justify='left')
lblBlinds.grid(row=3,column=0)
txtBlinds=Entry(f1aa,font=('arial',16,'bold'),textvariable=Blinds,bd=10,insertwidth=2,justify='left')
txtBlinds.grid(row=3,column=1)

lblHomeDelivery= Label(f1aa,font=('arial',16,'bold'),text='Home Delivery',bd=16,justify='left')
lblHomeDelivery.grid(row=4,column=0)
txtHomeDelivery=Entry(f1aa,font=('arial',16,'bold'),textvariable=HomeDelivery,bd=10,insertwidth=2,justify='left')
txtHomeDelivery.grid(row=4,column=1)


#==============
# ORDER's COST
#==============
DateofOrder=StringVar()
CostofCarpets=StringVar()
CostofFabric=StringVar()
CostofBlinds=StringVar()
CostofHomeDelivery=StringVar()

DateofOrder.set(time.strftime("%d/%m/%y"))

lblDateofOrder = Label(f1ab,font=('arial',16,'bold'),text='Order Date',bd=16,anchor='w')
lblDateofOrder.grid(row=0,column=0)
txtDateofOrder=Entry(f1ab,font=('arial',16,'bold'),textvariable=DateofOrder,bd=10,insertwidth=2,justify='left')
txtDateofOrder.grid(row=0,column=1)

lblCostofCarpets = Label(f1ab,font=('arial',16,'bold'),text='Carpets Cost',bd=16,anchor='w')
lblCostofCarpets.grid(row=1,column=0)
txtCostofCarpets=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofCarpets,bd=10,insertwidth=2,justify='left')
txtCostofCarpets.grid(row=1,column=1)


lblCostofFabric = Label(f1ab,font=('arial',16,'bold'),text='Fabric Cost',bd=16,anchor='w')
lblCostofFabric.grid(row=2,column=0)
txtCostofFabric=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofFabric,bd=10,insertwidth=2,justify='left')
txtCostofFabric.grid(row=2,column=1)

lblCostofBlinds = Label(f1ab,font=('arial',16,'bold'),text='Blinds Cost',bd=16,anchor='w')
lblCostofBlinds.grid(row=3,column=0)
txtCostofBlinds=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofBlinds,bd=10,insertwidth=2,justify='left')
txtCostofBlinds.grid(row=3,column=1)

lblHomeDelivery= Label(f1ab,font=('arial',16,'bold'),text='Delivery Cost ',bd=16,anchor='w')
lblHomeDelivery.grid(row=4,column=0)
txtHomeDelivery=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofHomeDelivery,bd=10,insertwidth=2,justify='left')
txtHomeDelivery.grid(row=4,column=1)

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
	Carpets.set(0)
	Fabric.set(0)
	Blinds.set(0)
	HomeDelivery.set(0)
	PaidTax.set("")
	SubTotal.set("")
	TotalCost.set("")
	CostofCarpets.set("")
	CostofFabric.set("")
	CostofBlinds.set("")
	CostofHomeDelivery.set("")

def PayReference():
	x = random.randint(10034,699812)
	randomRef = str(x)
	PaymentRef.set("BILL"+randomRef)

def CostOfOrder():
	CarpetPrice = float(Carpets.get())
	BlindsPrice = float(Blinds.get())
	FabricPrice = float(Fabric.get())
	DeliveryCost = float(HomeDelivery.get())
	
	CarpetsCost = "$ " + str("%.2f"%((CarpetPrice*15.49)))
	CostofCarpets.set(CarpetsCost)
	
	BlindsCost = "$ " + str("%.2f"%((BlindsPrice*7.49)))
	CostofBlinds.set(BlindsCost)
	
	FabricCost = "$ " + str("%.2f"%((FabricPrice*5.50)))
	CostofFabric.set(FabricCost)
	
	Delivery = "$ " + str("%.2f"%((DeliveryCost*4.50)))
	CostofHomeDelivery.set(Delivery)
	
	ToC = "$ " + str("%.2f"%((CarpetPrice*15.49)+(BlindsPrice*7.49)+(FabricPrice*5.50)+(DeliveryCost*4.50)))
	SubTotal.set(ToC)
	
	Tax = "$ " + str("%.2f"%(((CarpetPrice*15.49)+(BlindsPrice*7.49)+(FabricPrice*5.50)+(DeliveryCost*4.50))*0.2))
	PaidTax.set(Tax)
	
	TaxPay = (((CarpetPrice*15.49)+(BlindsPrice*7.49)+(FabricPrice*5.50)+(DeliveryCost*4.50))*0.2)
	Cost = (((CarpetPrice*15.49)+(BlindsPrice*7.49)+(FabricPrice*5.50)+(DeliveryCost*4.50)))
	CostofItems = "$ " + str("%.2f"%(TaxPay+Cost))
	TotalCost.set(CostofItems)
	
	x=random.randint(10034,699812)
	randomRef=str(x)
	PaymentRef.set("BILL"+randomRef)
		

btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Total Cost', command = CostOfOrder).grid(row=0,column=0)

btnRefer=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Sales Reference', command=PayReference).grid(row=0,column=1)

btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Reset',command=Reset).grid(row=1,column=0)

btnExit=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),width=15,text='Exit',command=iExit).grid(row=1,column=1)



root.mainloop()

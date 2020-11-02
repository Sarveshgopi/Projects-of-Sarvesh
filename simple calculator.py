from tkinter import *
root=Tk()
root.geometry("400x310")
root.title("Simple calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,padx=30,pady=10,columnspan=4)
def click(num):
    curr=e.get()
    e.delete(0,END)
    e.insert(0,curr+num)
def clear():
    e.delete(0,END)
def operation(operator):
    firstnumber=e.get()
    global temp1
    temp1=int(firstnumber)
    e.delete(0,END)
    global k
    k=operator
def answer():
    secondnumber=e.get()
    temp2=int(secondnumber)
    e.delete(0,END)
    if k=='+':
        e.insert(0,temp1+temp2)
    elif k=='-':
        e.insert(0,temp1-temp2)
    elif k=='*':
        e.insert(0,temp1*temp2)
    elif k=='/':
        e.insert(0,temp1/temp2)
button1=Button(root,text=1,padx=40,pady=20,command=lambda:click('1'))
button2=Button(root,text=2,padx=40,pady=20,command=lambda:click('2'))
button3=Button(root,text=3,padx=40,pady=20,command=lambda:click('3'))
button4=Button(root,text=4,padx=40,pady=20,command=lambda:click('4'))
button5=Button(root,text=5,padx=40,pady=20,command=lambda:click('5'))
button6=Button(root,text=6,padx=40,pady=20,command=lambda:click('6'))
button7=Button(root,text=7,padx=40,pady=20,command=lambda:click('7'))
button8=Button(root,text=8,padx=40,pady=20,command=lambda:click('8'))
button9=Button(root,text=9,padx=40,pady=20,command=lambda:click('9'))
button0=Button(root,text=0,padx=40,pady=20,command=lambda:click('0'))
button_=Button(root,text='=',padx=40,pady=20,command=answer)
buttonC=Button(root,text='C',padx=40,pady=20,command=clear)
buttonadd=Button(root,text='+',padx=40,pady=20,command=lambda:operation('+'))
buttonsub=Button(root,text='-',padx=40,pady=20,command=lambda:operation('-'))
buttonmul=Button(root,text='*',padx=40,pady=20,command=lambda:operation('*'))
buttondiv=Button(root,text='/',padx=40,pady=20,command=lambda:operation('/'))
button1.grid(row=5,column=1)
button2.grid(row=5,column=2)
button3.grid(row=5,column=3)
button4.grid(row=4,column=1)
button5.grid(row=4,column=2)
button6.grid(row=4,column=3)
button7.grid(row=3,column=1)
button8.grid(row=3,column=2)
button9.grid(row=3,column=3)
button0.grid(row=6,column=1)
button_.grid(row=6,column=2)
buttonC.grid(row=6,column=3)
buttonadd.grid(row=6,column=4)
buttonsub.grid(row=5,column=4)
buttonmul.grid(row=4,column=4)
buttondiv.grid(row=3,column=4)
root.mainloop()

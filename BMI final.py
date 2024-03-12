# BMI calculator
from tkinter import *
import csv
from PIL import ImageTk,Image

root=Tk()
root.configure(bg="#009999")
root.title("BMI Calculator")
root.geometry('620x720')


#frames
frame_weight=LabelFrame(root,bd=1,relief="solid",bg="#CCFF99")
frame_height=LabelFrame(root,bd=1,relief="solid",bg="#CCFF99")
frame_name=LabelFrame(root,bd=1,relief="solid",bg="#CCFF99")


#image
image=Image.open("BMI.jpeg")
resize_image=image.resize((350,250),Image.Resampling.LANCZOS)
img=ImageTk.PhotoImage(resize_image)
label_image=Label(root,image=img)
label_image.grid(row=1,column=1,rowspan=3,columnspan=3)

#functions
def calculate():
    global weight
    global height
    global bmi
    
    weight=entry_weight.get()
    height=entry_height.get()

    
    metres=float(height)*0.3048
    bmi=float(weight)/(metres)**2 #formula
    entry_bmi.insert(0,round(bmi,2))

    if bmi<18.5 :
        label_category1.configure(text="Under Weight",fg="white",bg="#66FFFF")
    if 18.5<=bmi<24.9 :
        label_category1.configure(text="Normal",fg="white",bg="#66FF66")
    if 24.9<=bmi<29.9 :
        label_category1.configure(text="Over Weight",fg="white",bg="#FFFF66")
    if 29.9<=bmi<+34.9 :
        label_category1.configure(text="Obese",fg="white",bg="#FFB266")
    if 35<bmi :
        label_category1.configure(text="Extremely Obese",fg="white",bg="#FF3333")

f=open("bmi_record.csv",'w')
csv_w=csv.writer(f)
heading=['NAME','BMI','CATEGORY']
csv_w.writerow(heading)
f.close()

def clear():
    global bmi
    global category1
    global name
    name=entry_name.get()
    bmi=entry_bmi.get()
    category1=label_category1.cget("text")
    entry_name.delete(0,END)
    entry_weight.delete(0,END)
    entry_height.delete(0,END)
    entry_bmi.delete(0,END)
    
    label_category1.configure(text="",bg="#009999")
    list_1=[name,bmi,category1]
    print(list_1)

    #storing data in csv file
    import csv
    file=open("bmi_record.csv",'a')
    csv_w=csv.writer(file)
    csv_w.writerow(list_1)
    file.close()


def showdata():
    file=open("bmi_record.csv",'r')
    csv_reader=csv.reader(file)
    count=0
    for i in csv_reader:
        print(','.join(i),end='')
        label_record=Label(root,text=','.join(i),bg="#009999")
        label_record.grid(row=7+count,column=0)
        count=count+1
    return
    


# creating widgets
label_title=Label(root,text="BMI CALCULATOR",width=30,height=2,font=(24),bd=1,relief="solid",bg="#FF6666" )
label_weight=Label(frame_weight,text="Weight(Kg)",font=(12),padx=50,bg="#CCFF99")
label_height=Label(frame_height,text="Height(ft)",font=(12),padx=60,bg="#CCFF99")
label_name=Label(frame_name,text="Name",font=(12),padx=60,bg="#CCFF99")
label_category=Label(root,text="category =>",font=(9),bg="#CCFF99",padx=8,pady=7,relief="raised")
label_category1=Label(root,font=(9),width=15,bg="#009999")

entry_weight=Entry(frame_weight,width=20,bd=4,font=(10),bg="#C0C0C0")
entry_height=Entry(frame_height,width=20,bd=4,font=(10),bg="#C0C0C0")
entry_name=Entry(frame_name,width=20,bd=4,font=(10),bg="#C0C0C0")
entry_bmi=Entry(root,font=(9),bd=3,width=10,bg="#C0C0C0")

#label_kg=Label(root,text="Kg",font=(12),borderwidth=1,relief="solid",padx=5,bg="#CCFF99")
#label_feet=Label(root,text="ft",font=(12),borderwidth=1,relief="solid",padx=10,bg="#CCFF99")

button_calculate=Button(root,text="Calculate =>",font=(9),command=calculate,bg="#66B2FF")
button_clear=Button(root,text="clear",font=(9),command=clear,padx=5,bg="#66B2FF")
button_showdata=Button(root,text="Show Data",command=showdata,bg="#66B2FF",font =(7),padx=8)

# placing widgets
label_title.grid(row=0,column=0,padx=80,pady=50,columnspan=4)
label_weight.grid(row=3,column=0,padx=1,sticky=W)
label_height.grid(row=5,column=0,padx=1,sticky=W)
label_name.grid(row=1,column=0,padx=1,sticky=W)
label_category.grid(row=5,column=0,padx=10,pady=10)
label_category1.grid(row=5,column=1,padx=10,pady=10)

#label_kg.grid(row=2,column=1,padx=5)
#label_feet.grid(row=3,column=1,padx=5)

entry_weight.grid(row=4,column=0)
entry_height.grid(row=6,column=0)
entry_name.grid(row=2,column=0)
entry_bmi.grid(row=4,column=1,padx=5)

frame_weight.grid(row=2,column=0,padx=10,pady=15)
frame_height.grid(row=3,column=0,padx=10,pady=15)
frame_name.grid(row=1,column=0,padx=10,pady=15)

button_calculate.grid(row=4,column=0)
button_clear.grid(row=4,column=3,padx=5,columnspan=2)
button_showdata.grid(row=6,column=0)



root.mainloop()


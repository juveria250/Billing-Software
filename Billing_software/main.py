from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import random,os
from tkinter import messagebox
import tempfile



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Billing Software")

        #-------------------VARIABLES-----------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        # product caregories------------
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]

        self.SubCatClothing=["Pant","T shirt","Shirt"]
        self.pant=["Levis","Mufti","spykar"]
        self.price_levis=1500
        self.price_Mufti=1700
        self.price_spykar=2000

        self.T_shirt=["Polo","Roadster","Jack&Jonson"]
        self.price_Polo=980
        self.price_Roadster=600
        self.price_JackJonson=1000

        self.shirt=["Peter England","Louis Phillip","Park Avenue"]
        self.price_Peter=1500
        self.price_Louis=1700
        self.price_Park=2000

        self.SubCatLifeStyle=["Bath Soap","Face Cream","Hair Oil"]
        self.Bath_soap=["LifeBuy","Lux","Santoor","Pearl"]
        self.price_LifeBuy=15
        self.price_Lux=17
        self.price_Santoor=20
        self.price_Pearl=20

        self.Face_cream=["Fair&Lovely","Ponds","Olay","Gernier"]
        self.price_fair=70
        self.price_ponds=60
        self.price_olay=100
        self.price_Gernier=100

        self.Hair_oil=["Parachute","Jasmin","Bajaj"]
        self.price_Para=50
        self.price_jasmin=170
        self.price_bajaj=20

        self.SubCatMobiles=["Iphone","Samsung","Xiome"]
        self.Iphone=["Iphone_X","Iphone_11","Iphone_12"]
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000

        self.Samsung=["Samsung M16","Samsung M17","Samsung M21"]
        self.price_sm16=16000
        self.price_sm17=12000
        self.price_sm21=18000

        self.Xiome=["Red11","Redme-12","RedmePro"]
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000


        img=Image.open("images/img1.jpg")
        # # img=Image.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=150)

        #img2
        img_1=Image.open("images/img8.jpg")
        # # img=Image.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=150)

        # img3
        img_2=Image.open("images/img10.jpg")
        # # img=Image.resize((500,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=500,height=150)



        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1500,height=45)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1500,height=620)


        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=300,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile no.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        #Name------
        self.lbl_CustName=Label(Cust_Frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        self.lbl_CustName.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_CustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
        self.txt_CustName.grid(row=1,column=1)

        #Email

        self.lbl_Email=Label(Cust_Frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Email.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txt_Email=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
        self.txt_Email.grid(row=2,column=1)

        #product frame

        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=320,y=5,width=600,height=140)
       #-------------category-----------

        self.lbl_Category=Label(Product_Frame,text="Select Categories",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Category.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.categories)

     #subcategories-------------------------------

        self.lbl_SubCategory=Label(Product_Frame,text="Sub Categories",font=("times new roman",12,"bold"),bg="white")
        self.lbl_SubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.Combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],font=("times new roman",10,"bold"),width=24,state="readonly")
        self.Combo_SubCategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #ProductName------------------

        self.lbl_ProductName=Label(Product_Frame,text="Product Name",font=("times new roman",12,"bold"),bg="white")
        self.lbl_ProductName.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.Combo_ProductName=ttk.Combobox(Product_Frame,textvariable=self.product,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.Combo_ProductName.grid(row=2,column=1,stick=W,padx=5,pady=2)
        self.Combo_ProductName.bind("<<ComboboxSelected>>",self.price)

        #Price-------------------------------------

        self.lbl_Price=Label(Product_Frame,text="Price",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Price.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.Combo_Price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.Combo_Price.grid(row=0,column=3,stick=W,padx=5,pady=2)

        #Qty----------------------------------------------

        self.lbl_Qty=Label(Product_Frame,text="Qty",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Qty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.Combo_Qty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("times new roman",10,"bold"),width=26)
        self.Combo_Qty.grid(row=1,column=3,stick=W,padx=5,pady=2)

        #Photo Frame---------------------------------------

        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=910,height=350)

        img_5=Image.open("images/img1.jpg")
        # # img=Image.resize((500,130),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        lbl_img_5=Label(MiddleFrame,image=self.photoimg_5)
        lbl_img_5.place(x=0,y=0,width=460,height=350)

        # img3
        img_6=Image.open("images/img8.jpg")
        # # img=Image.resize((500,130),Image.ANTIALIAS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        lbl_img_6=Label(MiddleFrame,image=self.photoimg_6)
        lbl_img_6.place(x=490,y=0,width=460,height=350)


        #search---------------------------
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=970,y=10,width=380,height=30)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("times new roman",12,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,stick=W,padx=1)

    
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",10,"bold"),width=20)
        self.txt_Entry_Search.grid(row=0,column=1,stick=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=10,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        #billing area-----------------------
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=950,y=45,width=400,height=350)

        #SCROLL BAR---------------------------
        scrollbar_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scrollbar_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scrollbar_y.pack(side=RIGHT,fill=Y)
        scrollbar_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter---------------
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=400,width=1350,height=110)


        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("times new roman",12,"bold"),bg="white")
        self.lblSubTotal.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("times new roman",10,"bold"),width=26)
        self.EntrySubTotal.grid(row=0,column=1,stick=W,padx=5,pady=2)

            #-----------------

        self.lbl_tax=Label(Bottom_Frame,text="Gov Tax",font=("times new roman",12,"bold"),bg="white")
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("times new roman",10,"bold"),width=26)
        self.txt_tax.grid(row=1,column=1,stick=W,padx=5,pady=2)
            #--------------------------------------------
        self.lblAmountTotal=Label(Bottom_Frame,text="Total",font=("times new roman",12,"bold"),bg="white")
        self.lblAmountTotal.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.EntryAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("times new roman",10,"bold"),width=26)
        self.EntryAmountTotal.grid(row=2,column=1,stick=W,padx=5,pady=2)

        #----------------------------------------------------
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)            

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)


        self.BtnPrint=Button(Btn_Frame,height=2,command=self.iprint,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,height=2,command=self.Clear,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,height=2,command=self.root.destroy,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
        #---------------------------------------------
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

        
        #--------------------------------------------
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Add to Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n --------------------------------------------------------------")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n--------------------------------------------------------------")
            
            #--------------------------------------

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

        #---------------------------------------------- 
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Mobile No:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n E mail:{self.c_email.get()}")

        self.textarea.insert(END,"\n------------------------------------------------------------------")
        self.textarea.insert(END,f"\n Products\t\t\tQTY\tPrice")
        self.textarea.insert(END,"\n----------------------------------------------------------------\n")

        #----------------------------------------------
    def save_bill(self):
        op=messagebox.askyesno("save Bill","Do you want to save bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("saved",f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()

        #-----------------------------------
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
            if found=='no':
                messagebox.showerror("Error","Invalid Bil No.")

    #--------------------------------------------

    def Clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()
    




        #----------------------------------------------

    def categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.Combo_SubCategory.config(value=self.SubCatClothing)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.Combo_SubCategory.config(value=self.SubCatLifeStyle)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.Combo_SubCategory.config(value=self.SubCatMobiles)
            self.Combo_SubCategory.current(0)

    def Product_add(self,event=""):
        if self.Combo_SubCategory.get()=="Pant":
            self.Combo_ProductName.config(value=self.pant)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get()=="T shirt":
            self.Combo_ProductName.config(value=self.T_shirt)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get()=="shirt":
            self.Combo_ProductName.config(value=self.shirt)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get()=="Bath Soap":
            self.Combo_ProductName.config(value=self.Bath_soap)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get()=="Face Cream":
            self.Combo_ProductName.config(value=self.Face_cream)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get()=="Hair Oil":
            self.Combo_ProductName.config(value=self.Hair_oil)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get()=="Iphone":
            self.Combo_ProductName.config(value=self.Iphone)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get()=="Samsung":
            self.Combo_ProductName.config(value=self.Samsung)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get()=="Xiome":
            self.Combo_ProductName.config(value=self.Xiome)
            self.Combo_ProductName.current(0)

    def price(self,event=""):
        if self.Combo_ProductName.get()=="Levis":
            self.Combo_Price.config(value=self.price_levis)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Mufti":
            self.Combo_Price.config(value=self.price_Mufti)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="spykar":
            self.Combo_Price.config(value=self.price_spykar)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Polo":
            self.Combo_Price.config(value=self.price_Polo)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Roadster":
            self.Combo_Price.config(value=self.price_Roadster)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Jack&Jonson":
            self.Combo_Price.config(value=self.price_JackJonson)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Peter England":
            self.Combo_Price.config(value=self.price_Peter)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Louis Phillip":
            self.Combo_Price.config(value=self.price_Louis)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Park Avenue":
            self.Combo_Price.config(value=self.price_Park)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Fair&Lovely":
            self.Combo_Price.config(value=self.price_fair)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Ponds":
            self.Combo_Price.config(value=self.price_ponds)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Olay":
            self.Combo_Price.config(value=self.price_olay)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Gernier":
            self.Combo_Price.config(value=self.price_Gernier)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Parachte":
            self.Combo_Price.config(value=self.price_Para)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Jasmin":
            self.Combo_Price.config(value=self.price_fair)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Ponds":
            self.Combo_Price.config(value=self.price_jasmin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Bajaj":
            self.Combo_Price.config(value=self.price_bajaj)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Iphone_X":
            self.Combo_Price.config(value=self.price_ix)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Iphone_11":
            self.Combo_Price.config(value=self.price_i11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Iphone_12":
            self.Combo_Price.config(value=self.price_i12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Samsung M16":
            self.Combo_Price.config(value=self.price_sm16)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Samsung M17":
            self.Combo_Price.config(value=self.price_sm17)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Samsung M21":
            self.Combo_Price.config(value=self.price_sm21)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Red11":
            self.Combo_Price.config(value=self.price_r11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Redme-12":
            self.Combo_Price.config(value=self.price_r12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="RedmePro":
            self.Combo_Price.config(value=self.price_rpro)
            self.Combo_Price.current(0)
            self.qty.set(1)





        



        

    

if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
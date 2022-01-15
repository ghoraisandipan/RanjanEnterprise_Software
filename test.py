#Ghorai Enterprise (Billing Software)

# import modules
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import datetime
import time
import os
import csv
import re
import qrcode
import mysql.connector
import TESTING as tsk


# Bill_App Class create
class Bill_App:
    
    # define python constructor in class
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")   # base geometry diagram
        self.root.title("Created By DR. SANDIPAN")  # Software title
        self.root.iconbitmap("search.ico")    # Software Icon
        self.product_type_arr = []          # Type of product array
        self.qty_arr = []
        self.price_arr = []

        #for billing purpose
        self.products_i = []
        self.Typeofproducts_i = []
        self.qty_i = []
        self.perRs_i = []
        self.price_i = []
        self.counter = 0

        #customer details variables---> text variables
        self.shop_date = StringVar()
        self.customer_name = StringVar()
        self.customer_address = StringVar()
        self.customer_phone = StringVar()
        self.customer_email = StringVar()
        self.customer_bill_no = StringVar()
        self.x = tsk.final_id()        # Generate Random Numbers
        self.customer_bill_no.set(str(self.x))
        self.cust_product_name = StringVar()
        self.cust_product_type = StringVar()
        self.product_quantity = IntVar()
        self.product_price = DoubleVar()
        self.product_tax = DoubleVar()
        self.customer_payment_mode = StringVar()
        self.all_item_list = StringVar()
        self.all_sub_total = StringVar()
        self.all_tax_amount = StringVar()
        self.all_total_amount = StringVar()
        self.database_select_combo = StringVar()
        self.database_select_text = StringVar()
        self.data_printing = StringVar()
        self.click_option = IntVar()

        #=================================Type of Products====================================== 
        # subcatagories list
        self.xeroxtype = ["Black/White","Colour"]
        self.printoutType = ["Black/White","Colour"]
        self.photocopyType = ["Passport","4x6 Size","5x7 Size","8x12 Size"]
        self.scanType = ["Normal"]
        self.formfillType = ["Normal"]
        self.laminationType = ["Card Size","A4 Size","Above A4 Size"]
        
        #================================Menubar===================================================
 
        # =============================== first image ==========================================
        
        img1 = Image.open("images/bill.jpg")
        img1 = img1.resize((1205,120),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbling = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=150,y=0,width=1212,height=100)

        #=================================LOGO=========================
        
        img2 = Image.open("images/dana.jpg")
        img2 = img2.resize((167,100),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=150,height=100)

        #==============================Title===========================
        
        lb1_title = Label(self.root,text="BILLING SOFTWARE",font=("times new roman",30,"bold"),bg="#000015",fg="gold",bd=4,relief=RIDGE)
        lb1_title.place(x=0,y=100,width=1363,height=40)

        # time and date
        global Tday
        self.Tday = datetime.date.today()
        self.just_dt = self.Tday.strftime("%d - %m - %Y")

        self.tm_dat = Label(lb1_title,text = f" DATE : {self.just_dt}",font=("Helvetica",9,"bold"),bg='black',fg='lightblue')
        self.tm_dat.place(x=1215,y=0)

        self.tm_now = Label(lb1_title,font=("Helvetica",9,"bold"),bg='black',fg='lightblue')
        self.tm_now.place(x=1230,y=15)
        
        self.update_clock()

        #exit button
        self.exit_btn = PhotoImage(file='images/ex.png')
        exit_img = Label(lb1_title,image=self.exit_btn)
        self.ex_btn1 = Button(lb1_title,image=self.exit_btn,cursor='hand2',bg='black',borderwidth=0,command=self.destroy_fun)
        self.ex_btn1.place(x=0,y=0)
        
        #=================================== Customer details =========================================================

        F1 = LabelFrame(self.root,relief=GROOVE,text='Customer Details',font=('times new roman',10,'bold'),bg='white',fg='orange',bd=2)
        F1.place(x=1,y=139,height=50,relwidth=1)
        
        #customer name
        name = Label(F1,text="Name",bg='white',fg="black",font=("times new roman",12,"bold"))
        name.grid(row=0,column=0,padx=5,pady=1)
        name_txt = ttk.Entry(F1,textvariable=self.customer_name,width=20,font=("times new roman",12,"bold"))
        name_txt.grid(row=0,column=1,padx=5,pady=2)
        
        #address
        address = Label(F1,text="Address",bg='white',fg="black",font=("times new roman",12,"bold"))
        address.grid(row=0,column=2,padx=15,pady=1)
        address_txt = ttk.Entry(F1,textvariable=self.customer_address,width=20,font=("times new roman",12,"bold"))
        address_txt.grid(row=0,column=3,padx=2,pady=2)
        
        #phone no
        phone = Label(F1,text="Phone No",bg='white',fg="black",font=("times new roman",12,"bold"))
        phone.grid(row=0,column=4,padx=15,pady=1)
        phone_txt = ttk.Entry(F1,textvariable=self.customer_phone,width=20,font=("times new roman",12,"bold"))
        phone_txt.grid(row=0,column=5,padx=2,pady=2)
        
        #Email Id
        email = Label(F1,text="Email-ID",bg='white',fg="black",font=("times new roman",12,"bold"))
        email.grid(row=0,column=6,padx=15,pady=1)
        email_txt = ttk.Entry(F1,textvariable=self.customer_email,width=20,font=("times new roman",12,"bold"))
        email_txt.grid(row=0,column=7,padx=2,pady=2)
        
        #bill no
        bill = Label(F1,text="Bill No",bg='white',fg="black",font=("times new roman",12,"bold"))
        bill.grid(row=0,column=8,padx=15,pady=1)
        bill_txt = ttk.Entry(F1,textvariable=self.customer_bill_no,width=20,font=("times new roman",12,"bold"),state='readonly')
        bill_txt.grid(row=0,column=9,padx=2,pady=2)

        #name star
        self.star1 = Label(F1,text="*",font=("times new roman",7,"bold"),fg='red',bg='white')
        self.star1.place(x=49,y=2)

        #address star
        self.star2 = Label(F1,text="*",font=("times new roman",7,"bold"),fg='red',bg='white')
        self.star2.place(x=312,y=2)

        #phone star
        self.star3 = Label(F1,text="*",font=("times new roman",7,"bold"),fg='red',bg='white')
        self.star3.place(x=583,y=2)

        #bill_no star
        self.star4 = Label(F1,text="*",font=("times new roman",7,"bold"),fg='red',bg='white')
        self.star4.place(x=1102,y=2)

        #========================================left label frame===================================
        
        lableframe_left = LabelFrame(self.root,bd=2,relief=RIDGE,text='Product Details',font=('times new roman',10,'bold'),fg='orange',padx=2)
        lableframe_left.place(x=1,y=188,width=700,height=280)

        #=====================================label & dropbox=======================================

        #product name
        product_name = Label(lableframe_left,text="Product Name",font=("times new roman",12,"bold"),fg="black",padx=2,pady=6)
        product_name.grid(row=0,column=0,sticky=W)
        self.combo_product_name = ttk.Combobox(lableframe_left,textvariable=self.cust_product_name,font=("times new roman",12,"bold"),width=27,state='readonly')
        self.combo_product_name['value']=('Select Product','Xerox','Printout','Lamination','PhotoCopy','Scan&Mail','FormFillup')
        self.combo_product_name.current(0)
        self.combo_product_name.grid(row=0,column=1,padx=33,pady=2,columnspan=3)
        self.combo_product_name.bind("<<ComboboxSelected>>",self.Catagories)

        #type of product
        product_type = Label(lableframe_left,text="Product Type",font=("times new roman",12,"bold"),fg="black",padx=2,pady=6)
        product_type.grid(row=1,column=0,sticky=W)
        self.combo_product_type = ttk.Combobox(lableframe_left,textvariable=self.cust_product_type,font=("times new roman",12,"bold"),width=27,state='readonly')
        self.combo_product_type.grid(row=1,column=1,padx=33,pady=2,columnspan=3)

        #Quantity
        qnty = Label(lableframe_left,text="Quantity",font=("times new roman",12,"bold"),fg="black",padx=2,pady=6)
        qnty.grid(row=2,column=0,sticky=W)
        qnty_txt = ttk.Entry(lableframe_left,textvariable=self.product_quantity,width=20,font=("times new roman",12,"bold"))
        qnty_txt.grid(row=2,column=1,padx=12,pady=2)

        #price
        price = Label(lableframe_left,text="Price",font=("times new roman",12,"bold"),fg="black",padx=2,pady=6)
        price.grid(row=3,column=0,sticky=W)
        price_txt = ttk.Entry(lableframe_left,textvariable=self.product_price,width=20,font=("times new roman",12,"bold"))
        price_txt.grid(row=3,column=1,padx=15,pady=2)

        #tax/gst
        tax = Label(lableframe_left,text="Tax+GST%",font=("times new roman",12,"bold"),fg="black",padx=2,pady=6)
        tax.grid(row=4,column=0,sticky=W)
        tax_txt = ttk.Entry(lableframe_left,textvariable=self.product_tax,width=20,font=("times new roman",12,"bold"))
        tax_txt.grid(row=4,column=1,padx=15,pady=2)

        #payment mode
        payment_mode = Label(lableframe_left,text="Payment Mode",font=("times new roman",12,"bold"),fg="black",padx=2,pady=6)
        payment_mode.grid(row=5,column=0,sticky=W)
        combo_payment_mode = ttk.Combobox(lableframe_left,textvariable=self.customer_payment_mode,font=("times new roman",12,"bold"),width=18,state='readonly')
        combo_payment_mode['value']=('Cash','Card','Online')
        combo_payment_mode.current(0)
        combo_payment_mode.grid(row=5,column=1,padx=15,pady=2)

        #product name star
        self.star5 = Label(lableframe_left,text="*",font=("times new roman",7,"bold"),fg='red',bg='#EBF4FA')
        self.star5.place(x=104,y=8)

        #product type
        self.star6 = Label(lableframe_left,text="*",font=("times new roman",7,"bold"),fg='red',bg='#EBF4FA')
        self.star6.place(x=98,y=46)

        #quantity star
        self.star5 = Label(lableframe_left,text="*",font=("times new roman",7,"bold"),fg='red',bg='#EBF4FA')
        self.star5.place(x=68,y=82)

        #price star
        self.star6 = Label(lableframe_left,text="*",font=("times new roman",7,"bold"),fg='red',bg='#EBF4FA')
        self.star6.place(x=47,y=115)

        #tax star
        self.star6 = Label(lableframe_left,text="*",font=("times new roman",7,"bold"),fg='red',bg='#EBF4FA')
        self.star6.place(x=90,y=145)

        #payment star
        self.star6 = Label(lableframe_left,text="*",font=("times new roman",7,"bold"),fg='red',bg='#EBF4FA')
        self.star6.place(x=112,y=181)

        #reset Button
        self.res_pic = PhotoImage(file='images/res.png')
        res_img = Label(lableframe_left,image=self.res_pic,padx=50,pady=20)
        my_res = Button(lableframe_left,command=self.prev_reset,image=self.res_pic,cursor='hand2',borderwidth=4)
        my_res.place(x=346,y=158)

        #=============================right side table frame on the left lable frame====================================
        
        count_frame = LabelFrame(lableframe_left,bd=2,relief=RIDGE,text='Bill Counter',font=('times new roman',10,'bold'),fg='orange',padx=2)
        count_frame.place(x=400,y=0,width=291,height=207)

        # Item List
        Item_list = Label(count_frame,text="Item List",font=("times new roman",12,"bold"),fg="black",padx=2,pady=1)
        Item_list.grid(row=0,column=0,sticky=W)
        self.itemList_txt = ttk.Entry(count_frame,width=34,font=("times new roman",12,"bold"),textvariable=self.all_item_list)
        self.itemList_txt.grid(row=1,column=0,padx=3,pady=1,columnspan=3)
        
        #Sub total amount
        sub_total = Label(count_frame,text="Sub Total",font=("times new roman",12,"bold"),fg="black",padx=2,pady=1)
        sub_total.grid(row=2,column=0,sticky=W)
        sub_total_txt = ttk.Entry(count_frame,textvariable=self.all_sub_total,width=20,font=("times new roman",12,"bold"),state='readonly')
        sub_total_txt.grid(row=3,column=0,padx=2,pady=1,sticky=W)
        
        # Tax amount
        tax_total = Label(count_frame,text="Tax Amount",font=("times new roman",12,"bold"),fg="black",padx=2,pady=1)
        tax_total.grid(row=4,column=0,sticky=W)
        sub_tax_txt = ttk.Entry(count_frame,textvariable=self.all_tax_amount,width=20,font=("times new roman",12,"bold"),state='readonly')
        sub_tax_txt.grid(row=5,column=0,padx=2,pady=1,sticky=W)
        
        #total amount show
        total_amount = Label(count_frame,text="Total Amount",font=("times new roman",12,"bold"),fg="black",padx=2,pady=2)
        total_amount.grid(row=6,column=0,sticky=W)
        totalAmount_txt = ttk.Entry(count_frame,textvariable=self.all_total_amount,width=21,font=("times new roman",12,"bold"),state='readonly')
        totalAmount_txt.place(x=108,y=160)

        #check box   
        self.c = Checkbutton(count_frame,variable=self.click_option,text='All information \nare Correct !',fg='black')
        self.c.place(x=175,y=65)
        my_label = Label(count_frame,text="*  Please Check !!!",font=("times new roman",8,"bold"),fg='red')
        my_label.place(x=180,y=100)

        # all total star
        self.star6 = Label(count_frame,text="*",font=("times new roman",7,"bold"),fg='red',bg='#EBF4FA')
        self.star6.place(x=97,y=158)
   
        #====================================database all buttons=============================================

        # left button frame
        left_btn_frame = Frame(lableframe_left,bd=2,relief=RIDGE)
        left_btn_frame.place(x=0,y=210,width=692,height=50)

        #add button
        self.add_btn = PhotoImage(file='images/add.png')
        add_img = Label(left_btn_frame,image=self.add_btn)
        my_btn1 = Button(left_btn_frame,command=self.add_data,image=self.add_btn,cursor='hand2',borderwidth=0)
        my_btn1.place(x=1,y=0)

        #delete button
        self.dlt_btn = PhotoImage(file='images/delete.png')
        dlt_img = Label(left_btn_frame,image=self.dlt_btn,padx=50,pady=20)
        my_btn2 = Button(left_btn_frame,command=self.delete_data,image=self.dlt_btn,cursor='hand2',borderwidth=0)
        my_btn2.place(x=115,y=2)

        #save button
        self.sve_btn = PhotoImage(file='images/save.png')
        sve_img = Label(left_btn_frame,image=self.sve_btn,padx=50,pady=20)
        my_btn3 = Button(left_btn_frame,command=self.save_bill,image=self.sve_btn,cursor='hand2',borderwidth=0)
        my_btn3.place(x=235,y=2)

        #reset button
        self.reset_btn = PhotoImage(file='images/clear.png')
        reset_img = Label(left_btn_frame,image=self.reset_btn,padx=50,pady=20)
        my_btn4 = Button(left_btn_frame,command=self.clear,image=self.reset_btn,cursor='hand2',borderwidth=0)
        my_btn4.place(x=445,y=1)

        #update button
        self.update_btn = PhotoImage(file='images/update.png')
        update_img = Label(left_btn_frame,image=self.update_btn,padx=50,pady=20)
        my_btn5 = Button(left_btn_frame,command=self.update_data,image=self.update_btn,cursor='hand2',borderwidth=0)
        my_btn5.place(x=335,y=4)

        #add to cart
        self.cart_btn = PhotoImage(file='images/cart.png')
        cart_img = Label(left_btn_frame,image=self.cart_btn,padx=50,pady=20)
        my_btn6 = Button(left_btn_frame,image=self.cart_btn,cursor='hand2',borderwidth=0,command=self.add_to_cart)
        my_btn6.place(x=550,y=0)

        #==========================================right lable frame============================
        
        lableframe_right = LabelFrame(self.root,bd=2,relief=RIDGE,text='Bill Area',font=('times new roman',12,'bold'),fg='red',padx=2)
        lableframe_right.place(x=701,y=188,width=662,height=280)
        
        #===============================bill area===========================================
        
        h = Scrollbar(lableframe_right, orient = 'horizontal')
        h.pack(side = BOTTOM, fill = X)
        v = Scrollbar(lableframe_right)
        v.pack(side = RIGHT, fill = Y)

        self.t = Text(lableframe_right, width = 15, height = 15, wrap = NONE,bd=3,
                 xscrollcommand = h.set,
                 yscrollcommand = v.set)
  
        self.t.pack(side=TOP, fill=X)

        h.config(command=self.t.xview)
        v.config(command=self.t.yview)

        self.welcome()
        
        # ========================================search labelfram =======================================
        
        lableframe_bottom1 = LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',font=('times new roman',10,'bold'),fg='orange',padx=2)
        lableframe_bottom1.place(x=1,y=468,width=1362,height=55)
        
        #searchBy option
        SearchBy = Label(lableframe_bottom1,font=('arial',12,'bold'),text='Search By',bg='red',fg='white')
        SearchBy.grid(row=0,column=0,padx=4,pady=4)
        
        #search option combo box
        search_combo = ttk.Combobox(lableframe_bottom1,textvariable=self.database_select_combo,font=('arial',12,'bold'),width=25,state='readonly')
        search_combo['value']=('Select Option','Name','Phone_No','Bill_No','Email','Date')
        search_combo.current(0)
        search_combo.grid(row=0,column=1)
        
        # search Entry field
        txt_search = ttk.Entry(lableframe_bottom1,textvariable=self.database_select_text,font=('arial',12,'bold'),width=30)
        txt_search.grid(row=0,column=2,padx=4)
        
        # search button
        search_btn = Button(lableframe_bottom1,command=self.search_data,text='Search',font=('arial',11,'bold'),bg='black',fg='gold',cursor='hand2',width=10)
        search_btn.grid(row=0,column=3,padx=5,pady=0)
        
        # view all button
        view_btn = Button(lableframe_bottom1,command=self.fetch_data,text='View All',font=('arial',11,'bold'),bg='green',fg='gold',cursor='hand2',width=12)
        view_btn.grid(row=0,column=4,padx=5,pady=0)
        
        #generate bill button
        generate_bill_btn = Button(lableframe_bottom1,command=self.gen_bill,text='>> Generate Bill',font=('arial',12,'bold'),bg='lightblue',bd=2,fg='black',cursor='hand2',width=15)
        generate_bill_btn.grid(row=0,column=5,padx=5,pady=0)
        
        #print combobox
        print_combo = ttk.Combobox(lableframe_bottom1,textvariable=self.data_printing,font=('arial',12,'bold'),width=20,state='readonly')
        print_combo['value']=('Print Bill','Print Show Database')
        print_combo.current(0)
        print_combo.grid(row=0,column=6,padx=5)

        #print button
        self.print_btn = PhotoImage(file='images/print.png')
        print_img = Label(lableframe_bottom1,image=self.print_btn,padx=50,pady=0)
        my_btn7 = Button(lableframe_bottom1,command=self.data_print,image=self.print_btn,cursor='hand2',borderwidth=0)
        my_btn7.place(x=1250,y=0)

        # =====================================last label frame-->database show==============================
        
        data_lableframe_bottom2 = LabelFrame(self.root,bd=2,relief=RIDGE,text='Show all Stored Database',font=('times new roman',10,'bold'),fg='red',padx=2)
        data_lableframe_bottom2.place(x=1,y=520,width=1362,height=188)

        # database text area
        details_table = Frame(data_lableframe_bottom2,bd=2,relief=RIDGE)
        details_table.place(x=2,y=2,width=1350,height=155)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)
        self.cust_details_table = ttk.Treeview(details_table,column=('Name','Address','Phone_No','Email','Bill_No','Products','Payment_Mode','Total','Date'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("Name",text="Name")
        self.cust_details_table.heading("Address",text="Address")
        self.cust_details_table.heading("Phone_No",text="Phone_No")
        self.cust_details_table.heading("Email",text="Email")
        self.cust_details_table.heading("Bill_No",text="Bill_No")
        self.cust_details_table.heading("Products",text="Products")
        self.cust_details_table.heading("Payment_Mode",text="Payment_Mode")
        self.cust_details_table.heading("Total",text="Total")
        self.cust_details_table.heading("Date",text="Date")
        
        self.cust_details_table['show']='headings'

        self.cust_details_table.column("Name",width=200)
        self.cust_details_table.column("Address",width=250)
        self.cust_details_table.column("Phone_No",width=150)
        self.cust_details_table.column("Email",width=250)
        self.cust_details_table.column("Bill_No",width=150)
        self.cust_details_table.column("Products",width=200)
        self.cust_details_table.column("Payment_Mode",width=100)
        self.cust_details_table.column("Total",width=80)
        self.cust_details_table.column("Date",width=150)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ========================================add item and another operation settings======================================
    
        # list create for total price and total tax value
        self.l=[]             # total price
        self.GST = []         # total tax value   
    
    def add_to_cart(self):
      
        n=self.product_price.get()
        self.m=self.product_quantity.get() * n
        self.l.append(self.m)
        
        try:
            if self.product_price.get() == '0.0' or self.cust_product_name.get() == "Select Product":
                messagebox.showerror("Error","Please select the Product Name and Mention the Price")
        
            else:
                current = self.itemList_txt.get()
                self.itemList_txt.delete(0,END)
                self.itemList_txt.insert(0,str(current)+" "+str(self.combo_product_name.get()))
                
                self.products_i.append(self.cust_product_name.get())
                self.Typeofproducts_i.append(self.cust_product_type.get())
                self.qty_i.append(self.product_quantity.get())
                self.perRs_i.append(self.product_price.get())
                self.price_i.append(self.product_quantity.get()*self.product_price.get())

                self.counter += 1
                #billing purpose operation over
            
                self.t.insert(END,f"\n {self.cust_product_name.get()} \t\t\t {self.cust_product_type.get()}\t\t\t{self.product_quantity.get()}\t\t{self.product_price.get()}\t\t{'%.2f'%self.m}")
                self.all_sub_total.set(str('Rs. %.2f'%(sum(self.l))))
                self.b = float((self.product_tax.get())*0.01)
                self.g = float((self.b) * (self.m))
                self.GST.append(float(self.g))
                self.all_tax_amount.set(str('Rs. %.2f'%(sum(self.GST))))
                self.all_total_amount.set(str('Rs. %.2f'%((sum(self.GST))+(sum(self.l)))))

        except Exception as es:
            messagebox.showerror('Error',f'Detect Wrong input customer product details :{es}')


        

    #======================================Bill generate function==================================================
    
    
    def gen_bill(self):
        
        
        try:
            
            if self.click_option.get() == 0 :
                messagebox.showerror("Error","Please Click the CheckButton")

            if self.click_option.get() == 1 :
                              

                if (self.customer_name.get()=='' or self.customer_address.get()=='' or self.customer_phone.get()=='' or self.cust_product_name.get()=='Select Product' or self.product_price.get()==0.0 or self.all_total_amount.get()=='Rs. 0.00') :
                    messagebox.showerror("Error","Please fill Customer all details Properly")
                
            
                else:
                    
                    op = messagebox.askyesno('Alart','Are you sure Customer all details are right ?')
                    if op>0:
                        tex = self.t.get(12.0,(12.0+float(len(self.l))))
                        self.welcome()
                        self.t.insert(END,tex)
                        self.t.insert(END,f"\n\n\n\n\n=======================================================================================================")
                        self.t.insert(END,f"\n\t\t All Items Amount : \t {self.all_sub_total.get()}")
                        self.t.insert(END,f"\n\t\t Tax+GST Amount : \t {self.all_tax_amount.get()}")
                        self.t.insert(END,f"\n\t\t\t\t\t\t\t Total Paybill Amount : \t {self.all_total_amount.get()}")
                        self.t.insert(END,f"\n=======================================================================================================")
                        self.t.insert(END,"\n\n\t          Chowhati Netaji Block, Near Panchayen Math, Rajpur-Sonarpur, Kol - 700149")
                        self.t.insert(END,"\n\t\t\t\t\t\t              PH : 9874041260 / 9073877551")

                    # ========================barcode generate =====================================  
                        
                        global o
                        o=self.customer_bill_no.get()
                        global m
                        m = str(o)
                        
                        
                        qr = qrcode.make(f'Ghorai Enterprise \n Bill_No : {self.customer_bill_no.get()} \n Customer Name : {self.customer_name.get()} \n Address : {self.customer_address.get()} \n Email : {self.customer_email.get()} \n Products : {self.all_item_list.get()} \n Total Amount : {self.all_total_amount.get()} \n Payment Mode : {self.customer_payment_mode.get()}')
                        qr.save("images/m.png")
                        global img5
    
                        my_pic4 = Image.open('images/m.png')
                        resized = my_pic4.resize((100,100), Image.ANTIALIAS)
                        resized.save('images/revise.png')
    
                        img5 = PhotoImage(file='images/revise.png')

                    # ===========================barcode generated===================================

                        self.all_sub_total.set("")
                        self.all_tax_amount.set("")
                        self.bill_pro_amount = sum(self.l)
                        self.bill_gst_amount = sum(self.GST)
                        self.l.clear()
                        self.GST.clear()

                        messagebox.showinfo('Information','The customer Bill has been Generated')
                    else:
                        return
        
        except Exception as es:
            messagebox.showerror('Error',f'Something went wrong. Error is {es}')


    #=======================================bill text setting===========================================
    
    def welcome(self):
        self.t.delete(1.0,END)
        self.t.insert(END,"\t\t\t\t Welcome to Ghorai Enterprise\n")
        self.t.insert(END,f"\n BILL Number: {self.customer_bill_no.get()}")
        self.t.insert(END,f"\n Customer Name: {self.customer_name.get()}")
        self.t.insert(END,f"\n Address: {self.customer_address.get()}")
        self.t.insert(END,f"\n Phone Number: {self.customer_phone.get()}  \t\t\t\t\t\t\t\t   Payment Mode: {self.customer_payment_mode.get()}")
        self.t.insert(END,f"\n Email-ID: {self.customer_email.get()}       \t\t\t\t\t\t\t\t   Date: {self.just_dt}")
        self.t.insert(END,"\n===============================================================================")
        self.t.insert(END,"\n Products\t\t\t Type of Product \t\t\t Qty \t\t Per Rs. \t\t Price")
        self.t.insert(END,"\n===============================================================================\n")
        self.t.configure(font="arial 10 bold")
        
    # ========================================Item caltagories set==================================================
    
    def Catagories(self,event=""):
        if self.combo_product_name.get() == "Xerox":
            self.combo_product_type.config(value=self.xeroxtype)
            self.combo_product_type.current(0)   
        if self.combo_product_name.get() == "Printout":
            self.combo_product_type.config(value=self.printoutType)
            self.combo_product_type.current(0)
        if self.combo_product_name.get() == "PhotoCopy":
            self.combo_product_type.config(value=self.photocopyType)
            self.combo_product_type.current(0)
        if self.combo_product_name.get() == "Scan&Mail":
            self.combo_product_type.config(value=self.scanType)
            self.combo_product_type.current(0)
        if self.combo_product_name.get() == "Lamination":
            self.combo_product_type.config(value=self.laminationType)
            self.combo_product_type.current(0)
        if self.combo_product_name.get() == "FormFillup":
            self.combo_product_type.config(value=self.formfillType)
            self.combo_product_type.current(0)
        
        if self.cust_product_name.get() != "Select Product":
            self.product_quantity.set("1")

    #=============================================save generate bill===========================================
    
    def save_bill(self):
        
        try:    
            if self.click_option.get() == 0 or self.all_sub_total.get() != '' or self.all_tax_amount.get() != '' or self.all_total_amount.get()=='' or self.counter < 0:
                messagebox.showerror("Error","Please Generate the customer bill first")
            else:    
                op = messagebox.askyesno('Save Bill','Are you sure the customer bill has been Generated then you want to save the bill ?')
                if op>0:
                    bill_details = self.t.get(1.0,END)
                    f1 = open("images/"+str(self.customer_bill_no.get())+".txt",'w')
                    f1.write(bill_details)
                    f1.close()
                    messagebox.showinfo('Saved',f'Bill No : {self.customer_bill_no.get()} saved successfully')
                else:
                    return

        except Exception as es:
            messagebox.showerror('Error',f'Something went Wrong. Error is {es}')

    # =======================================printing function==============================================
    
    def data_print(self):
        
        if self.counter == 0 and self.data_printing.get()=="Print Bill":
            messagebox.showerror('Error','Please Generate your Bill or Something Wrong !!!')

        else:   
            if self.data_printing.get()=="Print Bill" :
                op = messagebox.askyesno('Attention Please !!','First Generate the Customer Bill')

                if op>0:            

                    im1 = Image.open('images/revise.png')
                    im1.save('images/final.jpg')

                    try:
                        f2 = open("print_out.html",'w')
                        f2.write(f"<!DOCTYPE html> \
                                  <html lang=\"en\"> \
                                  <head> \
                                  <meta charset=\"UTF-8\"> \
                                  <title>Invoice</title> \
                                  <link rel=\"stylesheet\" href=\"style.css\"> \
                                  </head> \
                                  <body> \
                                  <div class=\"page\" size=\"A4\"> \
                                    <div class=\"top-section\"> \
                                        <div class=\"address\"> \
                                            <div class=\"address-content\"> \
                                                <h2> <b>Ghorai Enterprise</b> </h2> \
                                                <p> Daspara Netaji Block, Chowhati, Rajpur-Sonarpur, Kol-700149 </p> \
                                            </div> \
                                        </div> \
                                        <div class=\"contact\"> \
                                            <div class=\"contact-content\"> \
                                                <div class=\"email\"> Email: <span class=\"span\"> \
                                                sandipanghorai321@gmail.com </span> </div> \
                                                <div class=\"number\"> Phone-No: <span class=\"span\"> 9874041260/9073877551 \
                                                </span> </div> \
                                            </div> \
                                        </div> \
                                    </div> \
                                    <div class=\"billing-invoice\"> \
                                        <div class=\"title\"> \
                                            Billing Invoice \
                                        </div> \
                                        <div class=\"des\"> \
                                            <p class=\"code\"> \
                                                #{self.customer_bill_no.get()} \
                                            </p> \
                                            <p class=\"issue\">Issued : <span>{self.just_dt}</span></p> \
                                        </div> \
                                    </div> \
                                    <div class=\"billing_to\"> \
                                        <div class=\"title\">Billed To </div> \
                                        <div class=\"billed_sec\"> \
                                            <div class=\"Name: \"> \
                                                {self.customer_name.get()} \
                                            </div> \
                                            <p> Email-Id: {self.customer_email.get()} </p> \
                                            <p> Phone-No: {self.customer_phone.get()} </p> \
                                        </div> \
                                        <div class=\"billed_sec\"> \
                                            <div class=\"sub-title\">Address</div> \
                                            <div class=\"ship_address\">{self.customer_address.get()}</div> \
                                            <div class=\"payment-title\"><b>Payment Mode:</b> {self.customer_payment_mode.get()}</div> \
                                        </div> \
                                        </div> \
                                        <div class=\"bill_details\"> \
                                            <div class=\"Bill\"><b>Bill Details</b></div> \
                                                <br> \
                                                <table> \
                                                    <tr> \
                                                        <th>Products</th> \
                                                        <th>Type of Products</th> \
                                                        <th>QTY.</th> \
                                                        <th>Per Rs.</th> \
                                                        <th>Price</th> \
                                                    </tr> ")

                        if self.counter == 1:
                            f2.write(f"<tr> \
                                        <td>{self.products_i[0]}</td> \
                                        <td>{self.Typeofproducts_i[0]}</td> \
                                        <td>{self.qty_i[0]}</td> \
                                        <td>{self.perRs_i[0]}</td> \
                                        <td>{self.price_i[0]}</td> \
                                        </tr> \
                                    </table> \
                                        </div>")
                        if self.counter == 2:
                            f2.write(f" <tr> \
                                        <td>{self.products_i[0]}</td> \
                                        <td>{self.Typeofproducts_i[0]}</td> \
                                        <td>{self.qty_i[0]}</td> \
                                        <td>{self.perRs_i[0]}</td> \
                                        <td>{self.price_i[0]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[1]}</td> \
                                        <td>{self.Typeofproducts_i[1]}</td> \
                                        <td>{self.qty_i[1]}</td> \
                                        <td>{self.perRs_i[1]}</td> \
                                        <td>{self.price_i[1]}</td> \
                                        </tr> \
                                        </table> \
                                        </div>")
                        if self.counter == 3:
                            f2.write(f" <tr> \
                                        <td>{self.products_i[0]}</td> \
                                        <td>{self.Typeofproducts_i[0]}</td> \
                                        <td>{self.qty_i[0]}</td> \
                                        <td>{self.perRs_i[0]}</td> \
                                        <td>{self.price_i[0]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[1]}</td> \
                                        <td>{self.Typeofproducts_i[1]}</td> \
                                        <td>{self.qty_i[1]}</td> \
                                        <td>{self.perRs_i[1]}</td> \
                                        <td>{self.price_i[1]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[2]}</td> \
                                        <td>{self.Typeofproducts_i[2]}</td> \
                                       <td>{self.qty_i[2]}</td> \
                                        <td>{self.perRs_i[2]}</td> \
                                        <td>{self.price_i[2]}</td> \
                                        </tr> \
                                        </table> \
                                        </div>")
                        if self.counter == 4:
                            f2.write(f" <tr> \
                                        <td>{self.products_i[0]}</td> \
                                        <td>{self.Typeofproducts_i[0]}</td> \
                                        <td>{self.qty_i[0]}</td> \
                                        <td>{self.perRs_i[0]}</td> \
                                        <td>{self.price_i[0]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[1]}</td> \
                                        <td>{self.Typeofproducts_i[1]}</td> \
                                        <td>{self.qty_i[1]}</td> \
                                        <td>{self.perRs_i[1]}</td> \
                                        <td>{self.price_i[1]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[2]}</td> \
                                        <td>{self.Typeofproducts_i[2]}</td> \
                                        <td>{self.qty_i[2]}</td> \
                                        <td>{self.perRs_i[2]}</td> \
                                        <td>{self.price_i[2]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[3]}</td> \
                                        <td>{self.Typeofproducts_i[3]}</td> \
                                        <td>{self.qty_i[3]}</td> \
                                        <td>{self.perRs_i[3]}</td> \
                                        <td>{self.price_i[3]}</td> \
                                        </tr> \
                                        </table> \
                                        </div>")
                        if self.counter == 5:
                            f2.write(f" <tr> \
                                        <td>{self.products_i[0]}</td> \
                                        <td>{self.Typeofproducts_i[0]}</td> \
                                        <td>{self.qty_i[0]}</td> \
                                        <td>{self.perRs_i[0]}</td> \
                                        <td>{self.price_i[0]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[1]}</td> \
                                        <td>{self.Typeofproducts_i[1]}</td> \
                                        <td>{self.qty_i[1]}</td> \
                                        <td>{self.perRs_i[1]}</td> \
                                        <td>{self.price_i[1]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[2]}</td> \
                                        <td>{self.Typeofproducts_i[2]}</td> \
                                        <td>{self.qty_i[2]}</td> \
                                        <td>{self.perRs_i[2]}</td> \
                                        <td>{self.price_i[2]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[3]}</td> \
                                        <td>{self.Typeofproducts_i[3]}</td> \
                                        <td>{self.qty_i[3]}</td> \
                                        <td>{self.perRs_i[3]}</td> \
                                        <td>{self.price_i[3]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[4]}</td> \
                                        <td>{self.Typeofproducts_i[4]}</td> \
                                        <td>{self.qty_i[4]}</td> \
                                        <td>{self.perRs_i[4]}</td> \
                                        <td>{self.price_i[4]}</td> \
                                        </tr> \
                                        </table> \
                                        </div>")
                        if self.counter == 6:
                            f2.write(f" <tr> \
                                        <td>{self.products_i[0]}</td> \
                                        <td>{self.Typeofproducts_i[0]}</td> \
                                        <td>{self.qty_i[0]}</td> \
                                        <td>{self.perRs_i[0]}</td> \
                                        <td>{self.price_i[0]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[1]}</td> \
                                        <td>{self.Typeofproducts_i[1]}</td> \
                                        <td>{self.qty_i[1]}</td> \
                                        <td>{self.perRs_i[1]}</td> \
                                        <td>{self.price_i[1]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[2]}</td> \
                                        <td>{self.Typeofproducts_i[2]}</td> \
                                        <td>{self.qty_i[2]}</td> \
                                        <td>{self.perRs_i[2]}</td> \
                                        <td>{self.price_i[2]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[3]}</td> \
                                        <td>{self.Typeofproducts_i[3]}</td> \
                                        <td>{self.qty_i[3]}</td> \
                                        <td>{self.perRs_i[3]}</td> \
                                        <td>{self.price_i[3]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[4]}</td> \
                                        <td>{self.Typeofproducts_i[4]}</td> \
                                        <td>{self.qty_i[4]}</td> \
                                        <td>{self.perRs_i[4]}</td> \
                                        <td>{self.price_i[4]}</td> \
                                        </tr> \
                                        <tr> \
                                        <td>{self.products_i[5]}</td> \
                                        <td>{self.Typeofproducts_i[5]}</td> \
                                        <td>{self.qty_i[5]}</td> \
                                        <td>{self.perRs_i[5]}</td> \
                                        <td>{self.price_i[5]}</td> \
                                        </tr> \
                                        </table> \
                                        </div>  ")

                        f2.write(f" <div class=\"amount_details\"> \
                                            <div class=\"product_amount\"> Total Products Amount : {str('Rs. %.2f'%(self.bill_pro_amount))}</div>\
                                                <br> \
                                            <div class=\"gst_amount\"> Total GST Amount : {str('Rs. %.2f'%(self.bill_gst_amount))}</div>\
                                            <br> \
                                            <hr> \
                                            <img src=\"images/final.jpg\"> \
                                            <div class=\"total_amount\"><b> Total Amount : {str('Rs. %.2f'%(self.bill_pro_amount+self.bill_gst_amount))}</b></div>\
                                           <p style=\"text-align:right;\">______________________</p> \
                                            <p style=\"text-align:right;\">Authorised Signatory</p> \
                                            <div class=\"generate\"> This is Computer Generated Invoice</div> \
                                        </div> \
                                    </body>  \
                                </html> ")
                    except Exception as es:
                        messagebox.showerror('Error',f'Please Generate your Bill-details or Somethin went Wrong. Error is {es}') 

                    os.startfile("print_out.html")

                else:
                    return

        if self.data_printing.get()=="Print Show Database":
            conn = mysql.connector.connect(host='localhost',username='root',password='root',database='sys')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from customer")

            with open("users.csv","w",newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in my_cursor.description])
                csv_writer.writerows(my_cursor)
            dir_path = os.getcwd() + "users.csv"
            messagebox.showinfo('success','Exported successfully')

        #clear all previous data from array
        self.fetch_data()
        self.products_i.clear()
        self.Typeofproducts_i.clear()
        self.qty_i.clear()
        self.perRs_i.clear()
        self.price_i.clear()
        self.counter = 0

    # =========================================Clear function==============================================
    
    def prev_reset(self):
        
        self.customer_bill_no.set(str(self.x))
        self.click_option.set(0)
        self.customer_name.set("")
        self.customer_address.set("")
        self.customer_phone.set("")
        self.customer_email.set("")
        self.cust_product_name.set("Select Product")
        self.cust_product_type.set("")
        self.product_quantity.set("")
        self.product_price.set("0.0")
        self.product_tax.set("0.0")
        self.customer_payment_mode.set("Cash")
        self.all_item_list.set("")
        self.all_sub_total.set("")
        self.all_tax_amount.set("")
        self.all_total_amount.set("")

        #clear all previous data from array
        self.products_i.clear()
        self.Typeofproducts_i.clear()
        self.qty_i.clear()
        self.perRs_i.clear()
        self.price_i.clear()
        self.counter = 0

        self.fetch_data()            
        self.welcome()

    def clear(self):
    
        try:
            if self.customer_name.get()=='' or self.customer_address.get()=='' or self.customer_phone.get()=='' or self.cust_product_name.get()=='' or self.all_total_amount.get()=='':
                messagebox.showerror('Error','Fist fill all information')
            
            
            else:
                if self.all_sub_total.get()=='' or self.all_tax_amount.get()=='':
                    op2 = messagebox.askyesno('Clear','Do you want to clear Customer Details Or Customer Generate Bill ?')
                
                    if op2>0:
                        op3 = messagebox.askyesno('Attention Please!!!','Another Bill No ?')
                    
                        if op3>0:
                            z = tsk.final_id()
                            self.customer_bill_no.set(str(z))
                            self.fetch_data()
                    
                        if op3<0:
                            self.customer_bill_no.set(self.x)
                    
                        self.l.clear()
                        self.GST.clear()

                        self.click_option.set(0)
                        self.customer_name.set("")
                        self.customer_address.set("")
                        self.customer_phone.set("")
                        self.customer_email.set("")
                        self.cust_product_name.set("Select Product")
                        self.cust_product_type.set("")
                        self.product_quantity.set("")
                        self.product_price.set("0.0")
                        self.product_tax.set("0.0")
                        self.customer_payment_mode.set("Cash")
                        self.all_item_list.set("")
                        self.all_sub_total.set("")
                        self.all_tax_amount.set("")
                        self.all_total_amount.set("")
                    
                        self.welcome()
                
                    else:
                        return
        except Exception as es:
            messagebox.showerror('Error',f'Something went wrong. Error is {es}')

        #clear all previous data from array
        self.products_i.clear()
        self.Typeofproducts_i.clear()
        self.qty_i.clear()
        self.perRs_i.clear()
        self.price_i.clear()
        self.counter = 0


        #========================================Database related functions==========================================

    #==================================================add data=======================================================
    
    def add_data(self):
        
        if self.customer_name.get()=='' or self.cust_product_name.get()=='Select Product' or self.customer_address.get()=='' or self.customer_phone.get()=='' or self.all_total_amount.get()=='':
            messagebox.showerror('Error','All Fields are required')
        
        elif self.click_option.get()==0 or self.all_sub_total.get() != '' or self.all_tax_amount.get() != '':
            messagebox.showerror('Error','Please Generate the Customer Bill')
        
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='root',database='sys')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.customer_name.get(),
                                                                                                    self.customer_address.get(),
                                                                                                    self.customer_phone.get(),
                                                                                                    self.customer_email.get(),
                                                                                                    self.customer_bill_no.get(),
                                                                                                    self.all_item_list.get(),
                                                                                                    self.customer_payment_mode.get(),
                                                                                                    self.all_total_amount.get(),
                                                                                                    self.Tday
                                                                                                ))
                conn.commit()
                self.after_adding()
                conn.close()
                messagebox.showinfo("Success","Customer has been Added !",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

    def after_adding(self):
        try:
            conn = mysql.connector.connect(host='localhost',username='root',password='root',database='sys')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from customer")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())

                for i in data:
                    self.cust_details_table.insert("",END,values=i)
            
                conn.commit()
            conn.close()

            self.cust_product_name.set("Select Product")
            self.cust_product_type.set("")
            self.product_quantity.set("")
            self.product_price.set("0.0")
            self.product_tax.set("0.0")
            self.all_item_list.set("")
            self.all_sub_total.set("")
            self.all_tax_amount.set("")
            self.all_total_amount.set("")
            self.database_select_combo.set("Select Option")
            self.database_select_text.set("")
            self.click_option.set(0)

            self.welcome()
        
        except Exception as es:
            messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

    # =======================================data fetch from database====================================

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host='localhost',username='root',password='root',database='sys')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from customer")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())

                for i in data:
                    self.cust_details_table.insert("",END,values=i)
            
                conn.commit()
            conn.close()

            self.customer_name.set("")
            self.customer_address.set("")
            self.customer_phone.set("")
            self.customer_email.set("")
            self.cust_product_name.set("Select Product")
            self.cust_product_type.set("")
            self.product_quantity.set("")
            self.product_price.set("0.0")
            self.product_tax.set("0.0")
            self.customer_payment_mode.set("Cash")
            self.all_item_list.set("")
            self.all_sub_total.set("")
            self.all_tax_amount.set("")
            self.all_total_amount.set("")
            k = tsk.final_id()
            self.customer_bill_no.set(str(k))
            self.database_select_combo.set("Select Option")
            self.database_select_text.set("")
            self.click_option.set(0)

            self.welcome()
        
        except Exception as es:
            messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
        

    # =====================================get cursor from customer database==========================

    def get_cursor(self,event=""):
        cursor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row)
        data = content["values"]

        self.customer_name.set(data[0])
        self.customer_address.set(data[1])
        self.customer_phone.set(data[2])
        self.customer_email.set(data[3])
        self.customer_bill_no.set(data[4])
        self.all_item_list.set(data[5])
        self.customer_payment_mode.set(data[6])
        self.all_total_amount.set(data[7])
        self.cust_product_type.set("")
        self.product_quantity.set("")
        self.product_price.set("")
        self.product_tax.set(0.0)
        self.all_sub_total.set("")
        self.all_tax_amount.set("")

        present = "NO"
        for i in os.listdir("images/"):
            if i.split('.')[0] == self.customer_bill_no.get():
                f2 = open(f"images/{i}","r")
                self.t.delete('1.0',END)
                for d in f2:
                    self.t.insert(END,d)
                f2.close()
                present = "YES"
        if present == "NO":
            self.welcome()

    # ==========================================update database==========================================

    def update_data(self):

        if self.customer_address.get()=='' or self.customer_name.get()=='' or self.customer_phone.get()=='' or self.all_item_list.get()=='' or self.all_total_amount.get()=='':
            messagebox.showerror('Error','All Fields are required or you Choose Wrong Option')
        
        else:
            try:
                update = messagebox.askyesno('Update','Are you sure update this Customer Data ?',parent=self.root)

                if update>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='root',database='sys')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update customer set Name=%s,Address=%s,Phone_No=%s,Email=%s,Products=%s,Payment_Mode=%s,Total=%s where Bill_No=%s",(
                                                                                                                                                self.customer_name.get(),
                                                                                                                                                self.customer_address.get(),
                                                                                                                                                self.customer_phone.get(),
                                                                                                                                                self.customer_email.get(),
                                                                                                                                                self.all_item_list.get(),
                                                                                                                                                self.customer_payment_mode.get(),
                                                                                                                                                self.all_total_amount.get(),
                                                                                                                                                
                                                                                                                                                self.customer_bill_no.get()

                                                                                                                                            ))
                else:
                    if not update:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo('Success','Customer Data Successfully Updated on Database',parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)


    # =========================================delete data from database===================================

    def delete_data(self):
    
        if self.customer_address.get()=='' or self.customer_name.get()=='' or self.customer_phone.get()=='' or self.all_item_list.get()=='' or self.all_total_amount.get()=='':
            messagebox.showerror('Error','Choose the Customer details from database',parent=self.root)
    
        else:
            try:
                Delete = messagebox.askyesno("Delete","Are you sure delete this Customer Data from Database ?",parent=self.root)

                if Delete>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='root',database='sys')
                    my_cursor = conn.cursor()
                    sql = "delete from customer where Bill_No=%s"
                    value = (self.customer_bill_no.get(),)
                    my_cursor.execute(sql,value)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Info","The Customer Data has been Deleted",parent=self.root)
                
                else:
                    if not Delete:
                        self.customer_name.set("")
                        self.customer_address.set("")
                        self.customer_phone.set("")
                        self.customer_email.set("")
                        self.cust_product_name.set("Select Product")
                        self.cust_product_type.set("")
                        self.product_quantity.set("")
                        self.product_price.set("0.0")
                        self.product_tax.set("0.0")
                        self.customer_payment_mode.set("Cash")
                        self.all_item_list.set("")
                        self.all_sub_total.set("")
                        self.all_tax_amount.set("")
                        self.all_total_amount.set("")
                        u = tsk.final_id()
                        self.customer_bill_no.set(str(u))
                        self.welcome()
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

    # ==================================Searching in database using schrema=================================
    
    def search_data(self):
        
        self.phone_rex = r'[0-9]{10}$'
        self.result_phone = re.match(self.phone_rex,self.database_select_text.get())
        self.bill_rex = r'[A-Z]{4}-[0-9]{5}$'
        self.result_bill = re.match(self.bill_rex,self.database_select_text.get())
        self.date_rex = r'[\d]{4}-[\d]{2}-[\d]{2}$'
        self.result_date = re.match(self.date_rex,self.database_select_text.get())

        if self.database_select_combo.get()=="Select option" or self.database_select_text.get()=="":
            messagebox.showerror('Error','Please Select ay Search By Option or Fill the searching Text')
        
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='root',database='sys')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from customer where "+str(self.database_select_combo.get())+" LIKE '%"+str(self.database_select_text.get())+"%'")
                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.cust_details_table.delete(*self.cust_details_table.get_children())

                    for i in rows:
                        self.cust_details_table.insert("",END,values=i)

                    conn.commit()

                elif not self.result_bill and self.database_select_combo.get()=='Bill_No' :
                    messagebox.showerror('Error','Customer Bill Number not Supported')
                
                elif self.database_select_combo.get()=='Name' and len(self.database_select_text.get())>25:
                    messagebox.showerror('Error','Customer Name suported only 25 Charecters')

                elif self.database_select_combo.get()=='Address' and len(self.database_select_text.get())>50:
                    messagebox.showerror('Error','Customer Address suported only 50 Charecters')

                elif not self.result_phone and self.database_select_combo.get()=='Phone_No' :
                    messagebox.showerror('Error','Customer Phone No suported only 10 digit')

                elif not self.result_date and self.database_select_combo.get()=='Date' :
                    messagebox.showerror('Error','Date suported only [YYYY-MM-DD] format')

                else:
                    messagebox.showinfo('Information','No data Found !!!')
                conn.close()              

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root) 

    # =========================================destroy function=============================================

    def destroy_fun(self):
        
        op = messagebox.askokcancel("Close Window",'Are you want to close the Software ?')
        
        if op>0:
            self.root.destroy()       
        else:
            return
    
    #=======================================Clock update function===========================================

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.tm_now.configure(text=f"TIME : {now}")
        root.after(200, self.update_clock)
        
# Bill_App main Class Constructor Call........................

if __name__ == "__main__":
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()



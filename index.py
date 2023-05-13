import uuid
from tkinter import *

win = Tk()
win.title('Library')
win.geometry('1920x1800')
win.state('zoomed')


# -------------------------- Class

CUSTOMER_LIST = []
BOOK_LIST = []

class Book:
    def __init__(self, name_arg, Author_arg, Edition_arg):
        self.id = uuid.uuid4()
        self.name = name_arg
        self.Author = Author_arg
        self.Edition = Edition_arg

    def __str__(self):
        res_str = 'Serial Number: ' + str(self.id) + '   ' + '\nName: ' + str(self.name) + '   ' + '\nAuthor: ' + str(
            self.Author)  + '   ' + '\nEdition: ' + '   ' + str(self.Edition)
        return res_str


class Customer:
    def __init__(self, name_arg, surname_arg):
        self.id = uuid.uuid4()
        self.name = name_arg
        self.surname = surname_arg
        self.list_of_books_bought = []


    def __str__(self):
        res_info_str = 'ID: ' + str(self.id) + '   ' +'\nName: ' + str(self.name) + '   ' + '\nSurname:' + str(self.surname)
        for elem in self.list_of_books_bought:
            res_info_str+= str(elem)
            res_info_str+= "|"
        return res_info_str







CUSTOMER_LIST.append(Customer("Ahmed","Eliyev"))
CUSTOMER_LIST.append(Customer("Eli","Hesenov"))
CUSTOMER_LIST.append(Customer("Fuad","Mikayilov"))



BOOK_LIST.append(Book("The 100 Best Business Books","Jack Covert","Portfolio"))
BOOK_LIST.append(Book("The Toyota Way Fieldbook"," David Meier","McGraw-Hill Education"))
BOOK_LIST.append(Book("The Idea Book","Fredrik Härén","Interesting "))


def add_costumer_book():
    add_person_Frame.place(x=200, y=0)
    add_book_Frame.place_forget()
    add_customer_Frame.place_forget()


def open_AddBookFrame_func():
    add_book_Frame.place(x=200, y=0)
    add_customer_Frame.place_forget()
    add_person_Frame.place_forget()

def remove_book_costumer():
    index = books_listbox.curselection()[0]
    books_listbox.delete(index)
    BOOK_LIST.pop(index)



def open_AddCustomerFrame_func():
    add_customer_Frame.place(x=200, y=0)
    add_book_Frame.place_forget()
    add_person_Frame.place_forget()

def add_book(name, Author, Edition):
    temp_books_obj = Book(name, Author, Edition)
    BOOK_LIST.append(Book(name, Author, Edition))
    return temp_books_obj

def remove_book():
    index = books_listbox.curselection()[0]
    books_listbox.delete(index)
    BOOK_LIST.pop(index)

def remove_book_person():
    index = books_person_listBox.curselection()[0]
    books_person_listBox.delete(index)
    BOOK_LIST.pop(index)


def remove_Person_book():
    index = persons_listBox.curselection()[0]
    persons_listBox.delete(index)
    CUSTOMER_LIST.pop(index)



def take_add_value():
    new_book_obj = add_book(entry_book_name.get(), entry_Author.get(), entry_Edition.get())
    entry_book_name.delete(0, END)
    entry_Author.delete(0, END)
    entry_Edition.delete(0, END)

    books_listbox.insert(END, new_book_obj)
    books_person_listBox.insert(END, new_book_obj)

    for i in BOOK_LIST:
        print(i)


chohic_person_index = 0
def chohic_person_index_func_btn():
    global  chohic_person_index
    chohic_person_index = persons_listBox.curselection()[0]
    print(chohic_person_index)



chohic_product_index = 0
def chohic_product_index_func_btn():
    global  chohic_product_index
    chohic_product_index = books_person_listBox.curselection()[0]
    print(chohic_product_index)

def make_sale():
    chohic_product_index_func_btn()
    CUSTOMER_LIST[chohic_person_index].list_of_books_bought.append(BOOK_LIST[chohic_product_index])

    persons_listBox.delete(chohic_product_index)
    persons_listBox.insert(chohic_product_index,CUSTOMER_LIST[chohic_person_index])






def add_customer(name, surname):
    temp_customer_obj = Customer(name, surname )
    CUSTOMER_LIST.append(temp_customer_obj)
    return temp_customer_obj

def remove_customer():
    index = customer_listbox.curselection()[0]
    customer_listbox.delete(index)
    CUSTOMER_LIST.pop(index)


def take_customer_entry_value():
    new_customer_obj = add_customer(entry_name_customer.get(), entry_surname_customer.get())
    entry_name_customer.delete(0, END)
    entry_surname_customer.delete(0, END)

    customer_listbox.insert(END, new_customer_obj)
    persons_listBox.insert(END, new_customer_obj)

    for elem in CUSTOMER_LIST:
        print(elem)







def exit():
    win.destroy()


menu_Frame = Frame(bg='#413e45', width=200, height=1080)
menu_Frame.place(relx=0.0, rely=0.0)


#---------------ADD

ADD_BOOK_PHOTO = PhotoImage(file='addbook.png')
ADD_CUSTOMER_PHOTO = PhotoImage(file='add3.png')
SECIM_PHOTO = PhotoImage(file="bookuser.png")


secim_btton_btn = Button(menu_Frame, text='ADD Costumer', command=lambda:add_costumer_book(), activebackground='#413e45',image=SECIM_PHOTO,border=0, bg='#413e45')
secim_btton_btn.place(x=30, y=250)

open_AddBookFrame_btn = Button(menu_Frame, text='Add Book', command=lambda: open_AddBookFrame_func(), image=ADD_BOOK_PHOTO, border=0, activebackground='#413e45', bg='#413e45')
open_AddBookFrame_btn.place(x=30, y=450 )


open_AddCustomerFrame_btn = Button(menu_Frame, text='Add Customer', command=lambda: open_AddCustomerFrame_func(),image=ADD_CUSTOMER_PHOTO, border=0, activebackground= '#413e45' , bg='#413e45')
open_AddCustomerFrame_btn.place(x=30, y=650)

# ----------------------------------Frames

add_book_Frame = Frame(bg='#f0f5fa', width=1920, height=1080)
add_book_Frame.place(x=200, y=0)


add_customer_Frame = Frame(bg='#f0f5fa', width=1920, height=1080)
add_customer_Frame.place(x=200, y=0)

add_person_Frame = Frame(bg='#f0f5fa', width=1920, height=1080)
add_person_Frame.place(x=200, y=0)



book_dealer_text = Label(text='ADMIN PANEL', font=('Open Sans Extrabold', 40), bg='#eff4fa', fg='#413e45')
book_dealer_text.place(x=810, y=15)



# --------------------------Namebook
lbl_year = Label(add_book_Frame, text='Name', bg='#eff4fa', font=('Open Sans Extrabold', 20))
lbl_year.place(x=780, y=150)
entry_book_name = Entry(add_book_Frame, border=0)
entry_book_name.place(x=753, y=200)
# --------------------------Authorbook
lbl_Author = Label(add_book_Frame, text='Author', bg='#eff4fa', font=('Open Sans Extrabold', 20))
lbl_Author.place(x=780, y=250)
entry_Author = Entry(add_book_Frame, border=0)
entry_Author.place(x=753, y=300)

# --------------------------Editionbook
lbl_edition = Label(add_book_Frame, text='Edition', bg='#eff4fa', font=('Open Sans Extrabold', 20))
lbl_edition.place(x=780, y=350)
entry_Edition = Entry(add_book_Frame, border=0)
entry_Edition.place(x=753, y=400)

# --------------------------Namecustomer
lbl_name_customer = Label(add_customer_Frame, text="Name", bg='#eff4fa')
lbl_name_customer.place(x=1000, y=270)
entry_name_customer = Entry(add_customer_Frame, border=0)
entry_name_customer.place(x=963, y=300)
# ------------------------Surnamecustomer
lbl_mail_customer = Label(add_customer_Frame, text='Surname', bg='#eff4fa')
lbl_mail_customer.place(x=1000, y=320)
entry_surname_customer = Entry(add_customer_Frame, border=0)
entry_surname_customer.place(x=963, y=350)



#------------- PhotoImage
BOOK_PHOTO = PhotoImage(file="digital-library.png")
BOOK_PHOTO_label = Label(add_book_Frame, image=BOOK_PHOTO)
BOOK_PHOTO_label.place(x=200, y=200)

CUSTOMER_PHOTO = PhotoImage(file='user.png')
CUSTOMER_PHOTO_label = Label(add_customer_Frame, image=CUSTOMER_PHOTO, bg='#eff4fa')
CUSTOMER_PHOTO_label.place(x=150, y=270)




#-------------- Add button
ADD_CUSTOMER_ICON_BTN = PhotoImage(file='add2.png')

customer_btn = Button(add_customer_Frame, text='ADD CUSTOMER', command=lambda: take_customer_entry_value(),image=ADD_CUSTOMER_ICON_BTN, border=0, bg='#eff4fa')
customer_btn.place(x=1080, y=400)


btn_choic_person = Button(add_person_Frame,text='Choose Person', command= lambda : chohic_person_index_func_btn())
btn_choic_person.place(x=830, y=410)



btn_choic_book_remove = Button(add_person_Frame,text='Remove_Book', command= lambda : remove_book_person())
btn_choic_book_remove.place(x=1450, y=410)

btn_choic_person_remove = Button(add_person_Frame,text='Remove_Person', command= lambda : remove_Person_book())
btn_choic_person_remove.place(x=700, y=410)

btn_make_seller = Button(add_person_Frame,text='AddBook', command= lambda : make_sale())
btn_make_seller.place(x=1590, y=410)



ADD_BOOK_ICON_BTN = PhotoImage(file='add2.png')

btn = Button(add_book_Frame, text='ADD BOOK', command=lambda: take_add_value(), image=ADD_BOOK_ICON_BTN, border=0, bg='#eff4fa')
btn.place(x=890, y=430)



REMOVE_BOOK_ICON_BTN = PhotoImage(file='delete.png')

btn_remove = Button(add_book_Frame, text='REMOVE BOOK', command=lambda: remove_book(), image=REMOVE_BOOK_ICON_BTN, border=0, bg='#eff4fa')
btn_remove.place(x=1020, y=780)

REMOVE_CUSTOMER_ICON_BTN = PhotoImage(file='delete.png')

user_btn_remove = Button(add_customer_Frame, text='REMOVE CUSTOMER', command=lambda: remove_customer(), image=REMOVE_CUSTOMER_ICON_BTN, border=0, bg='#eff4fa')
user_btn_remove.place(x=1510, y=520)

#----------Listbox
books_listbox = Listbox(add_book_Frame, width=50, border=0, selectmode=EXTENDED)
books_listbox.place(x=740, y=590)

customer_listbox = Listbox(add_customer_Frame, width=50, border=0, selectmode=EXTENDED)
customer_listbox.place(x=1240,y=340)


persons_listBox = Listbox(add_person_Frame,width=150, border=0, selectmode=EXTENDED)
persons_listBox.place(x=10, y=240)

books_person_listBox = Listbox(add_person_Frame,width=110, border=0, selectmode=EXTENDED)
books_person_listBox.place(x=1000, y=240)



#------------ exit
EXIT_PHOTO = PhotoImage(file='exit.png')

open_ExitFrame_btn = Button(menu_Frame, text='EXIT ', image=EXIT_PHOTO, border=0, activebackground= '#413e45' , bg='#413e45',command=exit)
open_ExitFrame_btn.place(x=30, y=900)


for elem in BOOK_LIST:
    books_person_listBox.insert(END, elem)


for elem in CUSTOMER_LIST:
    persons_listBox.insert(END, elem)





win.mainloop()










import socket
import pickle
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9998))



#receiveing stock
r_data = client.recv(1024)
r_obj = pickle.loads(r_data)

client_dictionary = {}

drinks2 = []
#iterating through received stock and adding into a dictoinary
for key in r_obj:
    client_dictionary.update({key: r_obj[key]})
    
#iterating through dictionary and adding into a list
for i in client_dictionary:
    drinks2.append(client_dictionary[i])



#Vending Machine

vending = Tk()

vending.geometry('570x750')

FONT = ('Helvetica 10')
ID = ('Arial 17 bold')
vending.config(background='navy blue')

frame = Frame(vending, bd=5, relief=RAISED, bg='navy blue')
frame.pack(pady=20, padx=20)

main_title = Label(frame, text='Welcome to the Fizzy Drink Vending Machine!!', font=FONT)
main_title.pack(pady=0, padx=0)

main_frame = Label(vending, relief=RAISED, bg='navy blue', font=FONT)
main_frame.pack(pady=20, padx=20)

#coke
Coke_frame = LabelFrame(main_frame,text="A1" ,relief=RAISED, bg='navy blue', font=ID, fg='green')
Coke_frame.grid(column=0, row=0)

img = Image.open('Drinks\Coca-Cola.gif')
img = img.resize((60,60), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)

A1 = Label(Coke_frame, image=photoImg)
A1.grid(column=0, row=0)

coke_price = Label(Coke_frame, text='Coca-Cola - £1.99', font=FONT )
coke_price.grid(column=0, row=1)

#Dr pepper
Pepper_frame = LabelFrame(main_frame, text="A2" ,relief=RAISED, bg='navy blue', font=ID, fg='green')
Pepper_frame.grid(column=1, row=0)

img1 = Image.open('Drinks\Dr.Pepper.gif')
img1 = img1.resize((60,60), Image.ANTIALIAS)
photoImg1 = ImageTk.PhotoImage(img1)

A2 = Label(Pepper_frame, image=photoImg1)
A2.grid(column=0, row=0)

pepper_price = Label(Pepper_frame, text='Dr.Pepper - £0.89', font = FONT)
pepper_price.grid(column=0, row=1)

#Pepsi
Pepsi_frame = LabelFrame(main_frame, text="A3",relief=RAISED, bg='navy blue', font=ID, fg='green')
Pepsi_frame.grid(column=2, row=0)

img2 = Image.open('Drinks\Pepsi.gif')
img2 = img2.resize((60,60), Image.ANTIALIAS)
photoImg2 = ImageTk.PhotoImage(img2)

A3 = Label(Pepsi_frame, image=photoImg2)
A3.grid(column=0, row=0)

pepsi_price = Label(Pepsi_frame, text='Pepsi - £2.00', font = FONT)
pepsi_price.grid(column=0, row=1)

#Sprite
Sprite_frame = LabelFrame(main_frame, text="A4",relief=RAISED, bg='navy blue', font=ID, fg='green')
Sprite_frame.grid(column=3, row=0)

img3 = Image.open('Drinks\Sprite.gif')
img3 = img3.resize((60,60), Image.ANTIALIAS)
photoImg3 = ImageTk.PhotoImage(img3)

A4 = Label(Sprite_frame, image=photoImg3)
A4.grid(column=0, row=0)

sprite_price = Label(Sprite_frame, text='Sprite - £1.55', font = FONT)
sprite_price.grid(column=0, row=1)


#JO
JO_frame = LabelFrame(main_frame, text="B1",relief=RAISED, bg='navy blue', font=ID, fg='green')
JO_frame.grid(column=0, row=2)

img4 = Image.open('Drinks\J20.gif')
img4 = img4.resize((60,60), Image.ANTIALIAS)
photoImg4 = ImageTk.PhotoImage(img4)

B1 = Label(JO_frame, image=photoImg4)
B1.grid(column=0, row=0)

jO_price = Label(JO_frame, text='JO - £0.70', font = FONT)
jO_price.grid(column=0, row=1)


#Fanta
Fanta_frame = LabelFrame(main_frame, text="B2",relief=RAISED, bg='navy blue', font=ID, fg='green')
Fanta_frame.grid(column=1, row=2)

img5 = Image.open('Drinks\Fanta.gif')
img5 = img5.resize((60,60), Image.ANTIALIAS)
photoImg5 = ImageTk.PhotoImage(img5)

B2 = Label(Fanta_frame, image=photoImg5)
B2.grid(column=0, row=0)

fanta_price = Label(Fanta_frame, text='Fanta - £2.70', font = FONT)
fanta_price.grid(column=0, row=1)

#Lipton
Lipton_frame = LabelFrame(main_frame, text="B3",relief=RAISED, bg='navy blue', font=ID, fg='green')
Lipton_frame.grid(column=2, row=2)

img6 = Image.open('Drinks\Lipton.gif')
img6 = img6.resize((60,60), Image.ANTIALIAS)
photoImg6 = ImageTk.PhotoImage(img6)

B3= Label(Lipton_frame, image=photoImg6)
B3.grid(column=0, row=0)

lipton_price = Label(Lipton_frame, text='Lipton - £1.00', font = FONT)
lipton_price.grid(column=0, row=1)

#KA
KA_frame = LabelFrame(main_frame, text="B4",relief=RAISED, bg='navy blue', font=ID, fg='green')
KA_frame.grid(column=3, row=2)

img7 = Image.open('Drinks\KA.gif')
img7 = img7.resize((60,60), Image.ANTIALIAS)
photoImg7 = ImageTk.PhotoImage(img7)

B4 = Label(KA_frame, image=photoImg7)
B4.grid(column=0, row=0)

ka_price = Label(KA_frame, text='KA - £1.65', font = FONT)
ka_price.grid(column=0, row=1)

#Mountain Dew
Mountain_frame = LabelFrame(main_frame, text="C1",relief=RAISED, bg='navy blue', font=ID, fg='green')
Mountain_frame.grid(column=0, row=3)

img8 = Image.open('Drinks\MountainDew.gif')
img8 = img8.resize((60,60), Image.ANTIALIAS)
photoImg8 = ImageTk.PhotoImage(img8)

C1= Label(Mountain_frame, image=photoImg8)
C1.grid(column=0, row=0)

mountain_price = Label(Mountain_frame, text='Mountain Dew - £2.99', font = FONT)
mountain_price.grid(column=0, row=1)

#Lucozade
Lucozade_frame = LabelFrame(main_frame, text="C2",relief=RAISED, bg='navy blue', font=ID, fg='green')
Lucozade_frame.grid(column=1, row=3)

img9 = Image.open('Drinks\Lucozade.gif')
img9 = img9.resize((60,60), Image.ANTIALIAS)
photoImg9 = ImageTk.PhotoImage(img9)

C2 = Label(Lucozade_frame, image=photoImg9)
C2.grid(column=0, row=0)

lucozade_price = Label(Lucozade_frame, text='Lucozade - £1.80', font = FONT)
lucozade_price.grid(column=0, row=1)


#Appletiser
Appletiser_frame = LabelFrame(main_frame, text="C3",relief=RAISED, bg='navy blue', font=ID, fg='green')
Appletiser_frame.grid(column=2, row=3)

img10 = Image.open('Drinks\Appletiser.gif')
img10 = img10.resize((60,60), Image.ANTIALIAS)
photoImg10 = ImageTk.PhotoImage(img10)

C3 = Label(Appletiser_frame, image=photoImg10)
C3.grid(column=0, row=0)

appletiser_price = Label(Appletiser_frame, text='Appletiser - £3.40', font = FONT)
appletiser_price.grid(column=0, row=1)


#Tropicana
Tropicana_frame = LabelFrame(main_frame, text="C4",relief=RAISED, bg='navy blue', font=ID, fg='green')
Tropicana_frame.grid(column=3, row=3)

img11 = Image.open('Drinks\Tropicana.gif')
img11 = img11.resize((60,60), Image.ANTIALIAS)
photoImg11 = ImageTk.PhotoImage(img11)

C4 = Label(Tropicana_frame, image=photoImg11)
C4.grid(column=0, row=0)

tropicana_price = Label(Tropicana_frame, text='Tropicana - £5.00', font = FONT)
tropicana_price.grid(column=0, row=1)

#entry
INPUT = LabelFrame(vending, text="Enter your item code here",relief=RAISED, bg='navy blue', font=FONT, fg='green')
INPUT.pack()

Entry1 = Entry(INPUT, width=30, borderwidth=3)
Entry1.pack()


textbox = LabelFrame(vending, text="Stock", relief=RAISED, bg='navy blue', font=FONT, fg='green')
textbox.pack(side=LEFT)

Answer = Text(textbox)
Answer.pack()
#formatting stock box for ease of viewing for user
for x in drinks2:
    drink = x.get('drink')
    price = x.get('price')
    quantity = x.get('quantity')
    Answer.insert(END, f"{drink}, £{price}:\t{quantity} available\n")
    

Answer.config(state=DISABLED)
Answer.config(width=32,height=12, font=('Helvetica 9'))

order_list = []

#TEXT BOXES
textbox2 = LabelFrame(vending, text='Order',relief=RAISED, bg='navy blue', font=FONT, fg='green')
textbox2.pack(side=RIGHT)

Answer2 = Text(textbox2)
Answer2.pack()
Answer2.config(width=16,height=10, font=FONT)

textbox3 = LabelFrame(vending, text='Total',relief=RAISED, bg='navy blue', font=FONT, fg='green')
textbox3.pack(side=BOTTOM)

total_box = Text(textbox3)
total_box.pack()
total_box.config(width=15,height=2, font=FONT)

transaction = []
from tkinter import simpledialog
def Pay():
    total = 0
    for i in order_list:
        total += i
    total_box.insert(END, f"\n£{total:.2f}")
    #send order to server
    pickle_transaction = pickle.dumps(transaction)
    client.send(pickle_transaction)
   
    result = messagebox.askquestion("Payment", f"The total amount due is £{total:.2f}\nPlease Choose a payment type below\nClick Yes for Card or No for Cash", icon="info")
    if result == 'yes':
        messagebox.showinfo("Card Payment","Card Confirmed. Process complete!\nThank you for using this machine and Goodbye")
    else:
        money = simpledialog.askstring("Cash payment", "Enter the amount of money below")

        while float(money) < total:
            messagebox.showinfo("Insufficient amout", "Error, enter the right amount of money.")
            money = simpledialog.askstring("Cash payment", "Enter the amount of money below")
        else:
            change = float(money) - total
            messagebox.showinfo("Money due", f"You paid £{money}.\nCollect your £{change:.2f} change.")
    #sending updated stock to server
    pickle_stock = pickle.dumps(drinks2)
    client.send(pickle_stock)
    messagebox.showinfo("Thank you", "Thank you for using our Vending Machine, we hope to see you again! Goodbye", icon="info")
    vending.destroy()
        
#Cancel button
def Cancel():
    messagebox.showinfo("Cancelled","Sorry, we could not provide you with your choice today. We hope to see you again. Have a good day!")
    Entry1.delete(0, END)
    Answer.delete(0, END)
    Answer2.delete(1.0, END)
    total_box.delete(1.0, END)
    vending.destroy()
    
#Add item button
def Add():
    select = Entry1.get()
    amount = int(Entry2.get())

    for item in drinks2:
        if select == item.get('code'):
            select = item
            name = select.get('drink')
            price = select.get('price')
            
            for i in range(amount):
                select['quantity'] -=1
                if select['quantity'] <0:
                    select['quantity'] = 0
                    messagebox.showinfo("Out Of Stock", "This item is not available, please chose another")

                else:
                    transaction.append(f"{name},{price},\n")
                    Answer2.insert(END, f"\n{name}, £{price}")
                    order_list.append(float(price))
                    
    Entry1.delete(0, END)
    Entry2.delete(0, END)
    

#transaction buttons
item_add = Button(vending, text='Add item', bg='powderblue',command=Add)
item_add.config(width=10)
item_add.pack()

pay_bttn = Button(vending, text='Finish and Pay', bg='powderblue',command=Pay)
pay_bttn.config(width=10)
pay_bttn.pack()

cancel_bttn = Button(vending, text='Cancel' , bg='red', command=Cancel)
cancel_bttn.config(width=10)
cancel_bttn.pack()

Entry2 = Entry(INPUT, width=3, borderwidth=3)
Entry2.pack()


#running tkinter
vending.mainloop()

#closing connection
client.close()


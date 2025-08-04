import tkinter as tk
from tkinter import ttk,messagebox


class ROMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant Management System")
        
        self.menu_item = {
            "Burger": 5,
            "Pizza": 10,
            "Pasta": 8,
            "Salad": 4,
            "Soda": 2,
        }
        self.exchange_rate = 82

        self.setup_background(root)

        frame = tk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.center)


        ttk.Label(text=frame, text="Welcome to the Restaurant Management System", 
                  font=("Arial", 20)).grid(row=0, columnspan=3, padx=10,pady=10)
        
        self.menu_label = {}
        self.menu_quantity = {}


        for i, (item, price) in enumerate(self.menu_item.items(), start=1):
            label=ttk.Label(frame, text=f"{item} - ${price}", font=("Arial", 14))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_label[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantity[item] = quantity_entry

            self.currencyvar= tk.StringVar()
            ttk.Label(frame, text="Currency: "),font=("Arial", 14).grid(row=len(self.menu.items)+1 ,
                                                                        column=0, padx=10, pady=5)
            
            currency_dropdown = ttk.Combobox(frame, textvariable=self.currencyvar, 
                                             state="readonly",width=18,values=["USD", "INR"])
            currency_dropdown.grid(row=len(self.menu_item)+1, column=1, padx=10, pady=5)
            currency_dropdown.current(0)
            self.currencyvar.trace("w", self.update_currency_label)
            order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
            order_button.grid(row=len(self.menu_item)+2, columnspan=3, padx=10, pady=10)


            def setup_background(self,root):
                bg_width = 800
                bg_height = 600
                canvas = tk.Canvas(root, width=bg_width, height=bg_height)
                canvas.pack()
                image = tk.PhotoImage(file="background.png")
                background_image = image.subsample(
                    image.width() // bg_width, image.height() // bg_height)
                canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
                canvas.image = background_image


            def updatemenuprices(self,*args):
                currency=self.currencyvar.get()
                symbol="₹" if currency=="INR" else "$"
                rate=self.exchange_rate if currency=="INR" else 1
                for item, price in self.menu_item.items():
                    price= self.menu_item[item] * rate
                    label = config(text=f"{item} - {symbol}{price:.2f}", font=("Arial", 14))

            def place_order(self):
                totalcost=0
                order_summary = "Order Summary:\n"
                currency=self.currencyvar.get()
                symbol="₹" if currency=="INR" else "$"
                rate=self.exchange_rate if currency=="INR" else 1
                for item, entry in self.menu_quantity.items():
                    quantity = entry.get()
                    if quantity.isdigit() :
                        quantity = int(quantity)
                        if quantity_isdigit():
                            quantity = int(quantity)
                            price = self.menu_item[item] * rate


                
                
                


            
            


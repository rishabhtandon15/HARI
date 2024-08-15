import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

class Crop:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class PriceService:
    def __init__(self):
        self.crops = [
            Crop("Wheat", 250.0),
            Crop("Rice", 300.0),
            Crop("Corn", 180.0),
            Crop("Maze",190.0),
            Crop("Barley",300.0),
            Crop("Pulses",250.0),
            Crop("Sugarcane",200.0),
            Crop("Oil seeds",450.0)                       
        ]

    def get_all_crops(self):
        return self.crops

    def update_price(self, crop_name, new_price):
        for crop in self.crops:
            if crop.name.lower() == crop_name.lower():
                crop.price = new_price
                break

class AgriPriceConnectUI:
    def __init__(self, master):
        self.master = master
        self.price_service = PriceService()
        self.master.title("AgriPriceConnect")
        self.master.geometry("600x400")
        self.master.minsize(730, 300)

        self.create_widgets()

    def create_widgets(self):
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # Create a frame for content
        self.content_frame = tk.Frame(self.master, bg='white', bd=2, relief=tk.RIDGE)
        self.content_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        # Create and set up the treeview
        self.tree = ttk.Treeview(self.content_frame, columns=('Crop', 'Price'), show='headings')
        self.tree.heading('Crop', text='Crop')
        self.tree.heading('Price', text='Price ($)')
        self.tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Add scrollbar to treeview
        scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Create refresh button
        refresh_button = ttk.Button(self.content_frame, text="Refresh Prices", command=self.refresh_prices)
        refresh_button.grid(row=1, column=0, pady=10)

        self.update_price_table()

    def update_price_table(self):
        # Clear the current items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add crops to the treeview
        for crop in self.price_service.get_all_crops():
            self.tree.insert('', 'end', values=(crop.name, f"{crop.price:.2f}"))

    def refresh_prices(self):
        # Simulate price updates
        for crop in self.price_service.get_all_crops():
            new_price = crop.price * (1 + (random.random() - 0.5) * 0.1)
            self.price_service.update_price(crop.name, round(new_price, 2))
        self.update_price_table()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgriPriceConnectUI(root)
    root.mainloop()

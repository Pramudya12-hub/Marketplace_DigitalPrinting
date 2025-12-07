import tkinter as tk
from tkinter import messagebox

# ==========================================
#           CLASS PRODUCT OOP
# ==========================================
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def apply_discount(self):
        return self.__price


class Banner(Product):
    def apply_discount(self):
        return self.get_price() * 0.95


class PhotoPrint(Product):
    def apply_discount(self):
        return self.get_price() * 0.98


class Merch(Product):
    def apply_discount(self):
        return self.get_price() * 0.90


class Cart:
    def __init__(self):
        self.items = []
    
    def add(self, product):
        self.items.append(product)
    
    def remove(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
    
    def get_total(self):
        return sum(item.apply_discount() for item in self.items)


# ==========================================
#           PROFESSIONAL UI + SHADOW
# ==========================================
class MarketplaceApp:
    def __init__(self, master):
        self.master = master
        master.title("Marketplace Digital Printing")
        master.geometry("950x550")
        master.configure(bg="#eef2f7")   

        # Professional Color Palette
        frame_bg = "#ffffff"
        accent_blue = "#2f4e78"
        accent_light = "#4c6ea8"
        border_color = "#d0d7e2"
        shadow_color = "#c7ccd4"
        danger = "#d9534f"
        danger_hover = "#c9302c"
        font_main = ("Segoe UI", 10)
        font_title = ("Segoe UI", 12, "bold")

        self.cart = Cart()
        #     SHADOW FRAME FUNCTION
        def create_shadow(x, y, parent):
            shadow = tk.Frame(parent, bg=shadow_color)
            shadow.place(x=x+3, y=y+3, width=350, height=430)
            return shadow

        #     FRAME PRODUK + SHADOW
        create_shadow(30, 25, master)       # Shadow behind product frame

        left_frame = tk.Frame(master, bg=frame_bg, bd=1, relief="solid")
        left_frame.place(x=30, y=25, width=350, height=430)

        # Header Accent
        tk.Frame(left_frame, bg=accent_blue, height=4).pack(fill="x")

        tk.Label(
            left_frame, text="Daftar Produk", bg=frame_bg, fg=accent_blue,
            font=font_title, pady=10
        ).pack()

        self.product_listbox = tk.Listbox(
            left_frame, width=42, height=15, bg="#f9fbff",
            fg="#1e2a38", font=font_main,
            selectbackground="#c7dbf4", highlightbackground=border_color
        )
        self.product_listbox.pack(padx=15, pady=5)

        self.products = [
            Banner("Banner 1x1 m", 30000),
            Banner("Banner 2x1 m", 55000),
            Banner("Banner 3x1 m", 75000),
            PhotoPrint("Foto 4R", 3000),
            PhotoPrint("Foto 10R", 12000),
            PhotoPrint("Foto 20R", 25000),
            Merch("Mug Custom", 35000),
            Merch("Kaos Sablon", 80000),
            Merch("Stiker A4", 5000)
        ]

        for p in self.products:
            self.product_listbox.insert(tk.END, f"{p.get_name()} - Rp {p.get_price():,}")

        # Add Button
        self.add_button = tk.Button(
            left_frame, text="Tambah ke Keranjang",
            command=self.add_to_cart, width=30,
            bg=accent_light, fg="white", font=font_main, bd=0, pady=7
        )
        self.add_button.pack(pady=10)
        self.add_button.bind("<Enter>", lambda e: self.add_button.config(bg="#3d5f92"))
        self.add_button.bind("<Leave>", lambda e: self.add_button.config(bg=accent_light))

        # ==========================================
        #     FRAME KERANJANG + SHADOW
        # ==========================================
        create_shadow(410, 25, master)      # Shadow behind cart frame

        right_frame = tk.Frame(master, bg=frame_bg, bd=1, relief="solid")
        right_frame.place(x=410, y=25, width=350, height=430)

        tk.Frame(right_frame, bg=accent_blue, height=4).pack(fill="x")

        tk.Label(
            right_frame, text="Keranjang Belanja", bg=frame_bg, fg=accent_blue,
            font=font_title, pady=10
        ).pack()

        self.cart_listbox = tk.Listbox(
            right_frame, width=42, height=15, bg="#f9fbff",
            fg="#1e2a38", font=font_main,
            selectbackground="#f7c6c7", highlightbackground=border_color
        )
        self.cart_listbox.pack(padx=15, pady=5)

        self.remove_button = tk.Button(
            right_frame, text="Hapus Item",
            command=self.remove_item, width=30,
            bg=danger, fg="white", font=font_main, bd=0, pady=7
        )
        self.remove_button.pack(pady=10)
        self.remove_button.bind("<Enter>", lambda e: self.remove_button.config(bg=danger_hover))
        self.remove_button.bind("<Leave>", lambda e: self.remove_button.config(bg=danger))

        # ==========================================
        #            TOTAL & CHECKOUT
        # ==========================================
        self.total_label = tk.Label(
            master, text="Total: Rp 0",
            font=("Segoe UI", 16, "bold"),
            bg="#eef2f7", fg=accent_blue
        )
        self.total_label.place(x=300, y=470)

        self.checkout_button = tk.Button(
            master, text="Checkout",
            command=self.checkout, width=20,
            bg=accent_light, fg="white",
            font=("Segoe UI", 12, "bold"), bd=0, pady=7
        )
        self.checkout_button.place(x=520, y=465)

        self.checkout_button.bind("<Enter>", lambda e: self.checkout_button.config(bg="#3d5f92"))
        self.checkout_button.bind("<Leave>", lambda e: self.checkout_button.config(bg=accent_light))

    # =============================
    #        FUNCTIONAL
    # =============================
    def add_to_cart(self):
        index = self.product_listbox.curselection()
        if index:
            product = self.products[index[0]]
            self.cart.add(product)
            self.cart_listbox.insert(tk.END, f"{product.get_name()} - Rp {product.apply_discount():,.0f}")
            self.update_total()
        else:
            messagebox.showwarning("Error", "Pilih produk terlebih dahulu")

    def remove_item(self):
        index = self.cart_listbox.curselection()
        if index:
            self.cart.remove(index[0])
            self.cart_listbox.delete(index)
            self.update_total()
        else:
            messagebox.showwarning("Error", "Pilih item di keranjang")

    def update_total(self):
        total = self.cart.get_total()
        self.total_label.config(text=f"Total: Rp {total:,.0f}")

    def checkout(self):
        total = self.cart.get_total()
        messagebox.showinfo("Checkout", f"Total Belanja Anda: Rp {total:,.0f}")
        self.cart.items.clear()
        self.cart_listbox.delete(0, tk.END)
        self.update_total()

root = tk.Tk()
app = MarketplaceApp(root)
root.mainloop()

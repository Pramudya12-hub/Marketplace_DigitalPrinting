# =====================================================
# Import library Tkinter untuk GUI
# =====================================================
import tkinter as tk
from tkinter import messagebox

# =====================================================
#                CLASS PRODUCT (SUPERCLASS)
# =====================================================

class Product:
    # Constructor: menyimpan nama dan harga produk
    def __init__(self, name, price):
        self.__name = name      # atribut nama (private)
        self.__price = price    # atribut harga (private)

    # Getter untuk mengambil nama produk
    def get_name(self):
        return self.__name

    # Getter untuk mengambil harga produk
    def get_price(self):
        return self.__price

    # Method dasar diskon (akan dioverride di subclass)
    def apply_discount(self):
        return self.__price


# =====================================================
#         SUBCLASS PRODUK DENGAN POLYMORPHISM
# =====================================================

class Banner(Product):
    # Override method diskon → Banner diskon 5%
    def apply_discount(self):
        return self.get_price() * 0.95


class PhotoPrint(Product):
    # Override method diskon → PhotoPrint diskon 2%
    def apply_discount(self):
        return self.get_price() * 0.98


class Merch(Product):
    # Override method diskon → Merchandise diskon 10%
    def apply_discount(self):
        return self.get_price() * 0.90


# =====================================================
#                    CLASS CART (KERANJANG)
# =====================================================

class Cart:
    def __init__(self):
        self.items = []     # list untuk menyimpan objek Product

    # Menambahkan produk ke keranjang
    def add(self, product):
        self.items.append(product)

    # Menghapus produk berdasarkan index
    def remove(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]

    # Menghitung total harga setelah diskon
    def get_total(self):
        return sum(item.apply_discount() for item in self.items)


# =====================================================
#                CLASS GUI MARKETPLACE
# =====================================================

class MarketplaceApp:
    def __init__(self, master):
        self.master = master
        master.title("Marketplace Digital Printing")

        # Ukuran window
        master.geometry("950x550")
        master.configure(bg="#eef2f7")  # warna background utama

        # Keranjang sebagai objek Cart
        self.cart = Cart()

        # =====================================================
        #            DAFTAR PRODUK (OBJEK PRODUCT)
        # =====================================================
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

        # =====================================================
        #                  FRAME DAFTAR PRODUK
        # =====================================================

        self.product_listbox = tk.Listbox(master, width=40, height=18)
        self.product_listbox.place(x=50, y=60)

        # Masukkan produk ke listbox
        for p in self.products:
            self.product_listbox.insert(
                tk.END,
                f"{p.get_name()} - Rp {p.get_price():,}"
            )

        # Tombol tambah ke keranjang
        self.add_button = tk.Button(
            master,
            text="Tambah ke Keranjang",
            command=self.add_to_cart,
            width=25
        )
        self.add_button.place(x=50, y=360)

        # =====================================================
        #                   FRAME KERANJANG
        # =====================================================

        self.cart_listbox = tk.Listbox(master, width=40, height=18)
        self.cart_listbox.place(x=500, y=60)

        # Tombol hapus item
        self.remove_button = tk.Button(
            master,
            text="Hapus Item",
            command=self.remove_item,
            width=20
        )
        self.remove_button.place(x=500, y=360)

        # Label total harga
        self.total_label = tk.Label(master, text="Total: Rp 0",
                                    font=("Arial", 14, "bold"), bg="#eef2f7")
        self.total_label.place(x=50, y=420)

        # Tombol checkout
        self.checkout_button = tk.Button(
            master,
            text="Checkout",
            command=self.checkout,
            width=20
        )
        self.checkout_button.place(x=500, y=420)

    # =====================================================
    #               METHOD: TAMBAH KE KERANJANG
    # =====================================================
    def add_to_cart(self):
        index = self.product_listbox.curselection()

        if index:
            product = self.products[index[0]]
            self.cart.add(product)

            # Tampilkan item di keranjang
            self.cart_listbox.insert(
                tk.END,
                f"{product.get_name()} - Rp {product.apply_discount():,.0f}"
            )

            self.update_total()
        else:
            messagebox.showwarning("Error", "Pilih produk terlebih dahulu")

    # =====================================================
    #               METHOD: HAPUS ITEM CART
    # =====================================================
    def remove_item(self):
        index = self.cart_listbox.curselection()

        if index:
            self.cart.remove(index[0])
            self.cart_listbox.delete(index)
            self.update_total()
        else:
            messagebox.showwarning("Error", "Pilih item di keranjang")

    # =====================================================
    #               METHOD: UPDATE TOTAL HARGA
    # =====================================================
    def update_total(self):
        total = self.cart.get_total()
        self.total_label.config(text=f"Total: Rp {total:,.0f}")

    # =====================================================
    #                 METHOD: CHECKOUT
    # =====================================================
    def checkout(self):
        total = self.cart.get_total()

        messagebox.showinfo("Checkout", f"Total Belanja Anda: Rp {total:,.0f}")

        # Reset cart setelah checkout
        self.cart.items.clear()
        self.cart_listbox.delete(0, tk.END)
        self.update_total()


# =====================================================
#                 MENJALANKAN APLIKASI
# =====================================================

root = tk.Tk()
app = MarketplaceApp(root)
root.mainloop()

import tkinter as tk
from tkinter import ttk

class KonverterBilangan:
    def __init__(self, root):
        self.root = root
        self.root.title("Konverter Bilangan")
        
        # Styling
        style = ttk.Style()
        style.configure("TLabel", padding=5, font=('Helvetica', 10))
        style.configure("TEntry", padding=5)
        
        # Frame utama dengan padding
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Judul
        title_label = ttk.Label(main_frame, text="Konverter Bilangan", 
                              font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0,20))
        
        # Input fields
        # Desimal
        ttk.Label(main_frame, text="Desimal:").grid(row=1, column=0, sticky=tk.W)
        self.decimal_var = tk.StringVar()
        self.decimal_entry = ttk.Entry(main_frame, textvariable=self.decimal_var)
        self.decimal_entry.grid(row=2, column=0, sticky=(tk.W, tk.E))
        self.decimal_entry.config(width=40)
        ttk.Label(main_frame, text="Masukkan bilangan desimal", 
                 font=('Helvetica', 9, 'italic')).grid(row=3, column=0, sticky=tk.W)
        
        # Biner
        ttk.Label(main_frame, text="Biner:").grid(row=4, column=0, sticky=tk.W)
        self.binary_var = tk.StringVar()
        self.binary_entry = ttk.Entry(main_frame, textvariable=self.binary_var)
        self.binary_entry.grid(row=5, column=0, sticky=(tk.W, tk.E))
        ttk.Label(main_frame, text="Masukkan bilangan biner (hanya 0 dan 1)", 
                 font=('Helvetica', 9, 'italic')).grid(row=6, column=0, sticky=tk.W)
        
        # Oktal
        ttk.Label(main_frame, text="Oktal:").grid(row=7, column=0, sticky=tk.W)
        self.octal_var = tk.StringVar()
        self.octal_entry = ttk.Entry(main_frame, textvariable=self.octal_var)
        self.octal_entry.grid(row=8, column=0, sticky=(tk.W, tk.E))
        ttk.Label(main_frame, text="Masukkan bilangan oktal (0-7)", 
                 font=('Helvetica', 9, 'italic')).grid(row=9, column=0, sticky=tk.W)
        
        # Heksadesimal
        ttk.Label(main_frame, text="Heksadesimal:").grid(row=10, column=0, sticky=tk.W)
        self.hex_var = tk.StringVar()
        self.hex_entry = ttk.Entry(main_frame, textvariable=self.hex_var)
        self.hex_entry.grid(row=11, column=0, sticky=(tk.W, tk.E))
        ttk.Label(main_frame, text="Masukkan bilangan heksadesimal (0-9, A-F)", 
                 font=('Helvetica', 9, 'italic')).grid(row=12, column=0, sticky=tk.W)
        
        # Copyright
        ttk.Label(main_frame, text="© Mahrush Salam", 
                 font=('Helvetica', 9)).grid(row=13, column=0, sticky=tk.E, pady=(20,0))
        
        # Bind events
        self.decimal_entry.bind('<KeyRelease>', lambda e: self.convert_from_decimal())
        self.binary_entry.bind('<KeyRelease>', lambda e: self.convert_from_binary())
        self.octal_entry.bind('<KeyRelease>', lambda e: self.convert_from_octal())
        self.hex_entry.bind('<KeyRelease>', lambda e: self.convert_from_hex())
        
        # Add padding to all children
        for child in main_frame.winfo_children():
            child.grid_configure(padx=5, pady=2)
    
    def convert_from_decimal(self):
        """Convert from decimal to other bases"""
        try:
            if self.decimal_var.get():
                decimal_num = int(self.decimal_var.get())
                if decimal_num >= 0:
                    # Only update if the source field is focused
                    if self.root.focus_get() == self.decimal_entry:
                        self.binary_var.set(bin(decimal_num)[2:])  # Remove '0b' prefix
                        self.octal_var.set(oct(decimal_num)[2:])   # Remove '0o' prefix
                        self.hex_var.set(hex(decimal_num)[2:].upper())  # Remove '0x' prefix
        except ValueError:
            self.clear_other_fields('decimal')
    
    def convert_from_binary(self):
        """Convert from binary to other bases"""
        try:
            if self.binary_var.get():
                # Validate binary input
                if not all(bit in '01' for bit in self.binary_var.get()):
                    raise ValueError
                decimal_num = int(self.binary_var.get(), 2)
                if self.root.focus_get() == self.binary_entry:
                    self.decimal_var.set(str(decimal_num))
                    self.octal_var.set(oct(decimal_num)[2:])
                    self.hex_var.set(hex(decimal_num)[2:].upper())
        except ValueError:
            self.clear_other_fields('binary')
    
    def convert_from_octal(self):
        """Convert from octal to other bases"""
        try:
            if self.octal_var.get():
                # Validate octal input
                if not all(digit in '01234567' for digit in self.octal_var.get()):
                    raise ValueError
                decimal_num = int(self.octal_var.get(), 8)
                if self.root.focus_get() == self.octal_entry:
                    self.decimal_var.set(str(decimal_num))
                    self.binary_var.set(bin(decimal_num)[2:])
                    self.hex_var.set(hex(decimal_num)[2:].upper())
        except ValueError:
            self.clear_other_fields('octal')
    
    def convert_from_hex(self):
        """Convert from hexadecimal to other bases"""
        try:
            if self.hex_var.get():
                # Validate hex input
                if not all(c in '0123456789ABCDEFabcdef' for c in self.hex_var.get()):
                    raise ValueError
                decimal_num = int(self.hex_var.get(), 16)
                if self.root.focus_get() == self.hex_entry:
                    self.decimal_var.set(str(decimal_num))
                    self.binary_var.set(bin(decimal_num)[2:])
                    self.octal_var.set(oct(decimal_num)[2:])
        except ValueError:
            self.clear_other_fields('hex')
    
    def clear_other_fields(self, source):
        """Clear other fields when input is invalid"""
        if source != 'decimal':
            self.decimal_var.set('')
        if source != 'binary':
            self.binary_var.set('')
        if source != 'octal':
            self.octal_var.set('')
        if source != 'hex':
            self.hex_var.set('')

def main():
    root = tk.Tk()
    app = KonverterBilangan(root)
    root.mainloop()

if __name__ == "__main__":
    main()

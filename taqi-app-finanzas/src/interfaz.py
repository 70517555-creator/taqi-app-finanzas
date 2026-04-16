import tkinter as tk
from tkinter import messagebox
from modelo import Finanzas


class App:
    def __init__(self, root):
        self.finanzas = Finanzas()
        self.root = root
        self.root.title("TAQI")
        self.root.geometry("350x500")
        self.root.configure(bg="#1e3a8a")

        self.crear_componentes()

    def crear_componentes(self):
        tk.Label(self.root, text="TAQI", font=("Arial", 20, "bold"),
                 fg="white", bg="#1e3a8a").pack(pady=10)

        tk.Label(self.root, text="Seleccione una opción:",
                 fg="white", bg="#1e3a8a").pack()

        self.entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        self.crear_boton("Registrar Ingreso", "#22c55e", self.registrar_ingreso)
        self.crear_boton("Registrar Gasto", "#f97316", self.registrar_gasto)
        self.crear_boton("Ver Saldo", "#3b82f6", self.ver_saldo)
        self.crear_boton("Salir", "#9ca3af", self.root.quit)

        self.label_resultado = tk.Label(
            self.root,
            text="Saldo: S/ 0.00",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#1e3a8a"
        )
        self.label_resultado.pack(pady=20)

    def crear_boton(self, texto, color, comando):
        tk.Button(
            self.root,
            text=texto,
            bg=color,
            fg="white",
            font=("Arial", 12, "bold"),
            width=25,
            command=comando
        ).pack(pady=5)

    def obtener_monto(self):
        try:
            monto = float(self.entry.get())
            if monto < 0:
                raise ValueError
            return monto
        except:
            messagebox.showerror("Error", "Ingrese un monto válido")
            return None

    def registrar_ingreso(self):
        monto = self.obtener_monto()
        if monto is not None:
            try:
                self.finanzas.agregar_ingreso(monto)
                messagebox.showinfo("OK", "Ingreso registrado")
                self.entry.delete(0, tk.END)
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def registrar_gasto(self):
        monto = self.obtener_monto()
        if monto is not None:
            try:
                if not self.finanzas.agregar_gasto(monto):
                    messagebox.showwarning("Alerta", "Demasiados gastos")
                else:
                    messagebox.showinfo("OK", "Gasto registrado")
                    self.entry.delete(0, tk.END)
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def ver_saldo(self):
        saldo = self.finanzas.calcular_saldo()
        self.label_resultado.config(text=f"Saldo: S/ {saldo:.2f}")
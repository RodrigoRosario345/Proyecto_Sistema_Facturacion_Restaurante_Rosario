"""
Panel de menú con checkbuttons para selección de productos.
"""

from tkinter import Frame, LabelFrame, Checkbutton, Entry, IntVar, StringVar, W
from config.settings import COLORS, FONTS


class MenuPanel:
    """Panel que muestra los productos del menú con checkbuttons."""
    
    def __init__(self, parent: Frame, title: str, items: list):
        """
        Inicializa el panel de menú.
        
        Args:
            parent: Frame padre
            title: Título del panel (Comidas, Bebidas, Postres)
            items: Lista de productos a mostrar
        """
        self.parent = parent
        self.title = title
        self.items = items
        
        # Listas para almacenar widgets y variables
        self.selected_values = []  # IntVar para cada checkbutton
        self.quantity_entries = []  # Entry para cantidad
        self.quantity_vars = []  # StringVar para cada Entry
        
        self._create_panel()
        self._create_items()
    
    def _create_panel(self):
        """Crea el panel contenedor."""
        self.frame = LabelFrame(
            self.parent,
            text=self.title,
            labelanchor="n",
            fg=COLORS["text_light"],
            font=FONTS["heading"],
            bd=1,
            relief="flat",
            bg=COLORS["accent"],
            padx=5
        )
    
    def _on_checkbox_click(self):
        """Maneja el evento de click en cualquier checkbox."""
        for i, selected in enumerate(self.selected_values):
            if selected.get() == 1:
                self.quantity_entries[i].config(state="normal")
                self.quantity_entries[i].focus()
                if self.quantity_vars[i].get() == "0":
                    self.quantity_vars[i].set("")
            else:
                self.quantity_entries[i].config(state="disabled")
                self.quantity_vars[i].set("0")
    
    def _create_items(self):
        """Crea los checkbuttons y entries para cada item."""
        for index, item_name in enumerate(self.items):
            # Variable para el estado del checkbox
            var = IntVar()
            self.selected_values.append(var)
            
            # Crear checkbutton
            cb = Checkbutton(
                self.frame,
                text=item_name,
                variable=var,
                font=FONTS["normal"],
                bg=COLORS["accent"],
                fg=COLORS["text_dark"],
                selectcolor=COLORS["secondary"],
                onvalue=1,
                offvalue=0,
                command=self._on_checkbox_click,
                activebackground=COLORS["secondary"]
            )
            cb.grid(row=index, column=0, sticky=W)
            
            # Variable para la cantidad
            qty_var = StringVar()
            qty_var.set("0")
            self.quantity_vars.append(qty_var)
            
            # Entry para la cantidad
            entry = Entry(
                self.frame,
                font=FONTS["normal"],
                width=3,
                state="disabled",
                justify="center",
                textvariable=qty_var
            )
            entry.grid(row=index, column=1)
            self.quantity_entries.append(entry)
    
    def pack(self, **kwargs):
        """Empaqueta el frame."""
        self.frame.pack(**kwargs)
    
    def reset(self):
        """Reinicia todos los checkbuttons y entries."""
        for i in range(len(self.items)):
            if self.selected_values[i].get() == 1:
                self.quantity_entries[i].config(state="disabled")
                self.quantity_vars[i].set("0")
                self.selected_values[i].set(0)
    
    def get_quantities(self) -> list:
        """Retorna la lista de variables de cantidad."""
        return self.quantity_vars
    
    def get_selected(self) -> list:
        """Retorna la lista de variables de selección."""
        return self.selected_values

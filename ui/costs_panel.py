"""
Panel de costos que muestra los totales de la factura.
"""

from tkinter import Frame, Label, Entry, StringVar, FLAT
from config.settings import COLORS, FONTS


class CostsPanel:
    """Panel que muestra los costos y totales."""
    
    def __init__(self, parent: Frame):
        """
        Inicializa el panel de costos.
        
        Args:
            parent: Frame padre
        """
        self.parent = parent
        
        # Variables para mostrar costos
        self.food_cost = StringVar()
        self.drink_cost = StringVar()
        self.dessert_cost = StringVar()
        self.subtotal = StringVar()
        self.tax = StringVar()
        self.total = StringVar()
        
        self._create_panel()
        self._create_widgets()
    
    def _create_panel(self):
        """Crea el frame contenedor."""
        self.frame = Frame(
            self.parent,
            bd=2,
            relief=FLAT,
            bg=COLORS["secondary"],
            width=584,
            height=120,
            padx=54,
            pady=11
        )
    
    def _create_cost_row(self, label_text: str, variable: StringVar, row: int, column: int, padx_label: int = 0):
        """
        Crea una fila con etiqueta y campo de costo.
        
        Args:
            label_text: Texto de la etiqueta
            variable: Variable StringVar para el Entry
            row: Fila en el grid
            column: Columna inicial en el grid
            padx_label: Padding horizontal de la etiqueta
        """
        # Etiqueta
        label = Label(
            self.frame,
            text=label_text,
            fg=COLORS["text_light"],
            font=FONTS["heading"],
            bg=COLORS["secondary"],
            bd=1,
            relief=FLAT
        )
        label.grid(row=row, column=column, padx=(padx_label, 0), sticky="e")
        
        # Entry
        entry = Entry(
            self.frame,
            font=FONTS["heading"],
            bd=1,
            width=6,
            state='readonly',
            justify="center",
            textvariable=variable
        )
        entry.grid(row=row, column=column + 1, padx=(5, 0))
    
    def _create_widgets(self):
        """Crea todas las etiquetas y campos de costo."""
        # Columna izquierda - Costos por categoría
        self._create_cost_row("Comidas:", self.food_cost, 0, 0)
        self._create_cost_row("Bebidas:", self.drink_cost, 1, 0)
        self._create_cost_row("Postres:", self.dessert_cost, 2, 0)
        
        # Columna derecha - Totales
        self._create_cost_row("Sub total:", self.subtotal, 0, 2, padx_label=60)
        self._create_cost_row("Impuesto:", self.tax, 1, 2, padx_label=60)
        self._create_cost_row("Total:", self.total, 2, 2, padx_label=60)
    
    def pack(self, **kwargs):
        """Empaqueta el frame."""
        self.frame.pack(**kwargs)
    
    def update_costs(self, costs: dict):
        """
        Actualiza los valores de costo mostrados.
        
        Args:
            costs: Diccionario con los costos calculados
        """
        if costs["subtotal"] > 0:
            self.food_cost.set(str(costs["foods"]))
            self.drink_cost.set(str(costs["drinks"]))
            self.dessert_cost.set(str(costs["desserts"]))
            self.subtotal.set(str(costs["subtotal"]))
            self.tax.set(str(costs["tax"]))
            self.total.set(str(costs["total"]))
    
    def reset(self):
        """Limpia todos los valores."""
        self.food_cost.set("")
        self.drink_cost.set("")
        self.dessert_cost.set("")
        self.subtotal.set("")
        self.tax.set("")
        self.total.set("")

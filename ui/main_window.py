"""
Ventana principal de la aplicación.
Orquesta todos los componentes de la interfaz.
"""

from tkinter import Tk, Frame, Label, FLAT, TOP, LEFT, BOTTOM
from config.settings import (
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, 
    WINDOW_BG_COLOR, COLORS, FONTS
)
from config.menu_data import MENU_FOODS, MENU_DRINKS, MENU_DESSERTS
from ui.menu_panel import MenuPanel
from ui.costs_panel import CostsPanel
from ui.calculator_panel import CalculatorPanel
from ui.receipt_panel import ReceiptPanel, ActionButtonsPanel
from logic.billing import BillingSystem


class MainWindow:
    """Ventana principal de la aplicación."""
    
    def __init__(self):
        """Inicializa la ventana principal y todos sus componentes."""
        self.app = Tk()
        self.billing = BillingSystem()
        
        self._setup_window()
        self._create_frames()
        self._create_components()
    
    def _setup_window(self):
        """Configura las propiedades de la ventana."""
        # Centrar la ventana en la pantalla
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        
        x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
        y = int((screen_height / 2) - (WINDOW_HEIGHT / 2))
        
        self.app.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}')
        self.app.resizable(0, 0)
        self.app.title(WINDOW_TITLE)
        self.app.config(bg=WINDOW_BG_COLOR)
    
    def _create_frames(self):
        """Crea la estructura de frames de la aplicación."""
        # Frame superior con título
        self.top_frame = Frame(
            self.app, bd=2, relief=FLAT, bg=COLORS["primary"]
        )
        self.top_frame.pack(side=TOP, pady=(15, 0))
        
        # Título
        title_label = Label(
            self.top_frame,
            text="Sistema de Facturación",
            fg=COLORS["text_light"],
            font=FONTS["title"],
            bg=COLORS["primary"],
            width=22
        )
        title_label.grid(row=0, column=0)
        
        # Frame izquierdo
        self.left_frame = Frame(
            self.app, bd=2, relief=FLAT, 
            bg=COLORS["primary"], padx=10, pady=10
        )
        self.left_frame.pack(side=LEFT, padx=10)
        
        # Panel de menú (contenedor de los 3 paneles de productos)
        self.menu_container = Frame(
            self.left_frame, bd=2, relief=FLAT,
            bg=COLORS["secondary"], padx=10, pady=10
        )
        self.menu_container.pack(side=TOP)
        
        # Frame derecho
        self.right_frame = Frame(
            self.app, bd=2, relief=FLAT,
            bg=COLORS["primary"], padx=10, pady=10
        )
        self.right_frame.pack(side=LEFT)
    
    def _create_components(self):
        """Crea todos los componentes de la interfaz."""
        # Paneles de menú
        self.food_panel = MenuPanel(self.menu_container, "Comidas", MENU_FOODS)
        self.food_panel.pack(side=LEFT)
        
        self.drink_panel = MenuPanel(self.menu_container, "Bebidas", MENU_DRINKS)
        self.drink_panel.pack(side=LEFT, padx=(10, 10))
        
        self.dessert_panel = MenuPanel(self.menu_container, "Postres", MENU_DESSERTS)
        self.dessert_panel.pack(side=LEFT)
        
        # Panel de costos
        self.costs_panel = CostsPanel(self.left_frame)
        self.costs_panel.pack(side=BOTTOM, pady=(10, 0))
        
        # Panel de calculadora
        self.calculator_panel = CalculatorPanel(self.right_frame)
        self.calculator_panel.pack(side=TOP)
        
        # Panel de recibo
        self.receipt_panel = ReceiptPanel(self.right_frame)
        self.receipt_panel.pack(side=TOP, pady=(10, 10))
        
        # Panel de botones de acción
        callbacks = {
            "total": self._on_calculate_total,
            "recibo": self._on_generate_receipt,
            "guardar": self._on_save_receipt,
            "resetear": self._on_reset
        }
        self.action_buttons = ActionButtonsPanel(self.right_frame, callbacks)
        self.action_buttons.pack(side=TOP)
    
    def _on_calculate_total(self):
        """Callback para calcular el total."""
        costs = self.billing.calculate_totals(
            self.food_panel.get_quantities(),
            self.drink_panel.get_quantities(),
            self.dessert_panel.get_quantities(),
            self.food_panel.get_selected(),
            self.drink_panel.get_selected(),
            self.dessert_panel.get_selected()
        )
        self.costs_panel.update_costs(costs)
    
    def _on_generate_receipt(self):
        """Callback para generar el recibo."""
        receipt = self.billing.generate_receipt()
        self.receipt_panel.display_receipt(receipt)
    
    def _on_save_receipt(self):
        """Callback para guardar el recibo."""
        self.receipt_panel.save_receipt(self.billing.current_receipt)
    
    def _on_reset(self):
        """Callback para resetear todo."""
        # Resetear paneles de menú
        self.food_panel.reset()
        self.drink_panel.reset()
        self.dessert_panel.reset()
        
        # Resetear panel de costos
        self.costs_panel.reset()
        
        # Resetear recibo
        self.receipt_panel.reset()
        
        # Resetear sistema de facturación
        self.billing.reset()
        
        print("Reseteado correctamente")
    
    def run(self):
        """Inicia el bucle principal de la aplicación."""
        self.app.mainloop()

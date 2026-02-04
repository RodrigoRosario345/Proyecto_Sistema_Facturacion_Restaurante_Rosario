"""
Módulo de facturación y cálculo de costos.
Maneja el cálculo de totales, impuestos y generación de recibos.
"""

from datetime import date, datetime
from random import randint
from config.settings import TAX_RATE, RESTAURANT_NAME
from config.menu_data import PRICES_FOODS, PRICES_DRINKS, PRICES_DESSERTS


class BillingSystem:
    """Sistema de facturación del restaurante."""
    
    def __init__(self):
        self.total_foods = 0.0
        self.total_drinks = 0.0
        self.total_desserts = 0.0
        self.subtotal = 0.0
        self.tax = 0.0
        self.total = 0.0
        self.current_receipt = ""
    
    def calculate_totals(self, food_quantities: list, drink_quantities: list, 
                         dessert_quantities: list, food_selected: list,
                         drink_selected: list, dessert_selected: list) -> dict:
        """
        Calcula los totales de la compra.
        
        Args:
            food_quantities: Lista de cantidades de comidas
            drink_quantities: Lista de cantidades de bebidas
            dessert_quantities: Lista de cantidades de postres
            food_selected: Lista de valores de selección de comidas
            drink_selected: Lista de valores de selección de bebidas
            dessert_selected: Lista de valores de selección de postres
            
        Returns:
            Diccionario con los totales calculados
        """
        self.total_foods = 0.0
        self.total_drinks = 0.0
        self.total_desserts = 0.0
        
        # Calcular total de comidas
        for i, selected in enumerate(food_selected):
            if selected.get() == 1:
                quantity = int(food_quantities[i].get() or 0)
                self.total_foods += quantity * PRICES_FOODS[i]
        
        # Calcular total de bebidas
        for i, selected in enumerate(drink_selected):
            if selected.get() == 1:
                quantity = int(drink_quantities[i].get() or 0)
                self.total_drinks += quantity * PRICES_DRINKS[i]
        
        # Calcular total de postres
        for i, selected in enumerate(dessert_selected):
            if selected.get() == 1:
                quantity = int(dessert_quantities[i].get() or 0)
                self.total_desserts += quantity * PRICES_DESSERTS[i]
        
        # Calcular subtotal, impuesto y total
        self.subtotal = round(self.total_foods + self.total_drinks + self.total_desserts, 1)
        self.tax = round(self.subtotal * TAX_RATE)
        self.total = round(self.subtotal + self.tax, 1)
        
        return {
            "foods": round(self.total_foods, 1),
            "drinks": round(self.total_drinks, 1),
            "desserts": round(self.total_desserts, 1),
            "subtotal": self.subtotal,
            "tax": self.tax,
            "total": self.total
        }
    
    def generate_receipt(self) -> str:
        """
        Genera el texto del recibo.
        
        Returns:
            Texto formateado del recibo
        """
        if self.subtotal == 0:
            self.current_receipt = ""
            return ""
        
        # Generar código de recibo
        receipt_code = f'R#-{randint(1, 1000)}'
        
        # Obtener fecha y hora actual
        today = date.today()
        current_date = f"{today.day:02d}/{today.month:02d}/{today.year:04d}"
        now = datetime.now().time()
        current_time = f"{now.hour:02d}:{now.minute:02d}"
        
        self.current_receipt = f"""
        ------------------------------------------------------------
        {receipt_code}         fecha y hora: {current_date} {current_time}
        ------------------------------------------------------------
                            {RESTAURANT_NAME}

        1:  Comidas               ${round(self.total_foods, 1)}
        2:  Bebidas               ${round(self.total_drinks, 1)}
        3:  Postres               ${round(self.total_desserts, 1)}
        ------------------------------------------------------------
        Subtotal                  ${self.subtotal} 
        Impuesto                  ${self.tax} 
        TOTAL                     ${self.total} 
        ------------------------------------------------------------
        """
        
        return self.current_receipt
    
    def reset(self):
        """Reinicia todos los valores de facturación."""
        self.total_foods = 0.0
        self.total_drinks = 0.0
        self.total_desserts = 0.0
        self.subtotal = 0.0
        self.tax = 0.0
        self.total = 0.0
        self.current_receipt = ""

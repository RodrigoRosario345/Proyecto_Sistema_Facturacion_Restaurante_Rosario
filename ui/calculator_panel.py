"""
Panel de calculadora integrada.
"""

from tkinter import Frame, Entry, Button, END, FLAT
from config.settings import COLORS, FONTS
from logic.calculator import Calculator


class CalculatorPanel:
    """Panel con calculadora integrada."""
    
    def __init__(self, parent: Frame):
        """
        Inicializa el panel de calculadora.
        
        Args:
            parent: Frame padre
        """
        self.parent = parent
        self.calculator = Calculator()
        
        self._create_panel()
        self._create_display()
        self._create_buttons()
    
    def _create_panel(self):
        """Crea el frame contenedor."""
        self.frame = Frame(
            self.parent,
            bd=1,
            relief=FLAT,
            bg=COLORS["accent"],
            width=357,
            height=188
        )
    
    def _create_display(self):
        """Crea el visor de la calculadora."""
        self.display = Entry(
            self.frame,
            font=FONTS["calculator"],
            width=31,
            bd=1
        )
        self.display.grid(row=0, column=0, columnspan=4)
    
    def _on_button_click(self, value: str):
        """
        Maneja el click en un botón de la calculadora.
        
        Args:
            value: Valor del botón presionado
        """
        if value == 'R':  # Resultado
            expression = self.display.get()
            if expression:
                result = self.calculator.calculate(expression)
                self.display.delete(0, END)
                self.display.insert(0, result)
                self.calculator.reset()
        elif value == 'B':  # Borrar
            self.display.delete(0, END)
            self.calculator.reset()
        else:
            self.display.insert(END, value)
    
    def _create_buttons(self):
        """Crea los botones de la calculadora."""
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'R', 'B', '0', '/'
        ]
        
        row = 1
        col = 0
        
        for btn_text in buttons:
            btn = Button(
                self.frame,
                text=btn_text,
                font=FONTS["button"],
                fg=COLORS["text_light"],
                bg=COLORS["accent"],
                bd=1,
                width=7,
                command=lambda t=btn_text: self._on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="w")
            
            col += 1
            if col == 4:
                row += 1
                col = 0
    
    def pack(self, **kwargs):
        """Empaqueta el frame."""
        self.frame.pack(**kwargs)
    
    def reset(self):
        """Limpia el visor de la calculadora."""
        self.display.delete(0, END)
        self.calculator.reset()

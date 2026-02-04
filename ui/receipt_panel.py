"""
Panel de recibo que muestra y permite guardar el recibo.
"""

from tkinter import Frame, Text, Button, END, FLAT, messagebox, filedialog
from config.settings import COLORS, FONTS


class ReceiptPanel:
    """Panel que muestra el recibo generado."""
    
    def __init__(self, parent: Frame):
        """
        Inicializa el panel de recibo.
        
        Args:
            parent: Frame padre
        """
        self.parent = parent
        self._create_panel()
        self._create_text_area()
    
    def _create_panel(self):
        """Crea el frame contenedor."""
        self.frame = Frame(
            self.parent,
            bd=1,
            relief=FLAT,
            bg=COLORS["accent"],
            width=357,
            height=178
        )
    
    def _create_text_area(self):
        """Crea el área de texto para el recibo."""
        self.text_area = Text(
            self.frame,
            font=FONTS["receipt"],
            bd=1,
            width=42,
            height=9
        )
        self.text_area.grid(row=0, column=0)
    
    def pack(self, **kwargs):
        """Empaqueta el frame."""
        self.frame.pack(**kwargs)
    
    def display_receipt(self, receipt_text: str):
        """
        Muestra el texto del recibo.
        
        Args:
            receipt_text: Texto del recibo a mostrar
        """
        self.text_area.delete('1.0', END)
        if receipt_text:
            self.text_area.insert(END, receipt_text)
    
    def get_content(self) -> str:
        """Obtiene el contenido actual del recibo."""
        return self.text_area.get('1.0', END).strip()
    
    def save_receipt(self, receipt_text: str):
        """
        Guarda el recibo en un archivo.
        
        Args:
            receipt_text: Texto del recibo a guardar
        """
        if receipt_text:
            file = filedialog.asksaveasfile(mode="w", defaultextension='.txt')
            if file:
                file.write(receipt_text)
                file.close()
                messagebox.showinfo('Información', 'Su recibo ha sido guardado')
    
    def reset(self):
        """Limpia el área de texto."""
        self.text_area.delete('1.0', END)


class ActionButtonsPanel:
    """Panel con los botones de acción."""
    
    def __init__(self, parent: Frame, callbacks: dict):
        """
        Inicializa el panel de botones.
        
        Args:
            parent: Frame padre
            callbacks: Diccionario con las funciones callback para cada botón
        """
        self.parent = parent
        self.callbacks = callbacks
        
        self._create_panel()
        self._create_buttons()
    
    def _create_panel(self):
        """Crea el frame contenedor."""
        self.frame = Frame(
            self.parent,
            bd=1,
            relief=FLAT,
            bg=COLORS["primary"],
            width=357,
            height=78
        )
    
    def _create_buttons(self):
        """Crea los botones de acción."""
        button_names = ["total", "recibo", "guardar", "resetear"]
        
        for i, name in enumerate(button_names):
            btn = Button(
                self.frame,
                text=name,
                font=FONTS["button"],
                fg=COLORS["text_light"],
                bg=COLORS["accent"],
                width=7,
                command=self.callbacks.get(name, lambda: None),
                bd=1
            )
            btn.grid(row=0, column=i, pady=24)
    
    def pack(self, **kwargs):
        """Empaqueta el frame."""
        self.frame.pack(**kwargs)

#!/usr/bin/env python3
"""
Sistema de Facturación para Restaurante
Punto de entrada principal de la aplicación.

Autor: Desarrollado como práctica del curso Python Total
Fecha: 2024
"""

from ui.main_window import MainWindow


def main():
    """Función principal que inicia la aplicación."""
    app = MainWindow()
    app.run()


if __name__ == "__main__":
    main()

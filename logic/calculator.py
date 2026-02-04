"""
Módulo de calculadora matemática.
Implementa las operaciones de la calculadora integrada.
"""

import re


class Calculator:
    """Clase que maneja las operaciones de la calculadora."""
    
    def __init__(self):
        self.current_index = -1
        self._ordered_operators = []
    
    def reset(self):
        """Reinicia el estado de la calculadora."""
        self.current_index = -1
        self._ordered_operators = []
    
    def _order_operators(self, operators: list, index: int) -> list:
        """
        Ordena los operadores según precedencia matemática.
        * y / tienen mayor precedencia que + y -
        
        Args:
            operators: Lista de operadores a ordenar
            index: Índice actual en la lista
            
        Returns:
            Lista ordenada de operadores
        """
        if index < len(operators):
            if operators[index] in ("+", "-"):
                self._ordered_operators.append(operators[index])
                operators.pop(index)
                return self._order_operators(operators, index)
            else:
                return self._order_operators(operators, index + 1)
        
        return operators + self._ordered_operators
    
    def _perform_operation(self, nums_ops: list, ordered_ops: list, index: int):
        """
        Ejecuta las operaciones matemáticas recursivamente.
        
        Args:
            nums_ops: Lista con números y operadores
            ordered_ops: Lista de operadores ordenados por precedencia
            index: Índice actual
            
        Returns:
            Resultado de la operación
        """
        if not ordered_ops or len(nums_ops) == 1:
            return nums_ops[0] if nums_ops else 0
        
        current_op = nums_ops[index] if index < len(nums_ops) else None
        target_op = ordered_ops[0] if ordered_ops else None
        
        if current_op == target_op:
            left = float(nums_ops[index - 1])
            right = float(nums_ops[index + 1])
            
            if current_op == "+":
                result = left + right
            elif current_op == "-":
                result = left - right
            elif current_op == "*":
                result = left * right
            elif current_op == "/":
                result = left / right if right != 0 else 0
            else:
                return self._perform_operation(nums_ops, ordered_ops, index + 2)
            
            nums_ops[index] = result
            nums_ops.pop(index + 1)
            nums_ops.pop(index - 1)
            ordered_ops.pop(0)
            
            if len(nums_ops) == 1:
                return result
            
            return self._perform_operation(nums_ops, ordered_ops, 1)
        else:
            return self._perform_operation(nums_ops, ordered_ops, index + 2)
    
    def calculate(self, expression: str) -> float:
        """
        Calcula el resultado de una expresión matemática.
        
        Args:
            expression: Expresión matemática como string
            
        Returns:
            Resultado de la operación
        """
        self._ordered_operators = []
        
        # Extraer números y operadores
        nums_ops = re.findall(r'\d+\.?\d*|[\+\-\*\/]', expression)
        
        if not nums_ops:
            return 0
        
        # Extraer solo los operadores
        operators = [nums_ops[i] for i in range(1, len(nums_ops), 2)]
        
        # Ordenar operadores por precedencia
        ordered_ops = self._order_operators(operators.copy(), 0)
        
        # Realizar las operaciones
        result = self._perform_operation(nums_ops, ordered_ops, 1)
        
        return result

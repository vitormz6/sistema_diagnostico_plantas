"""
Testes para o módulo input_validation.py
"""

import unittest
from src.input_validation import InputValidator

class TestInputValidator(unittest.TestCase):
    """Testes para a classe InputValidator."""
    
    def setUp(self):
        """Configura o ambiente de teste."""
        self.validator = InputValidator()
    
    def test_empty_input(self):
        """Testa validação de entrada vazia."""
        self.assertFalse(self.validator.is_valid(""))
        self.assertFalse(self.validator.is_valid("   "))
        self.assertFalse(self.validator.is_valid(None))
    
    def test_input_too_short(self):
        """Testa validação de entrada muito curta."""
        min_length = self.validator.min_length
        
        # Entrada com comprimento menor que o mínimo
        self.assertFalse(self.validator.is_valid("ab"))
        self.assertFalse(self.validator.is_valid("a" * (min_length - 1)))
        
        # Entrada com comprimento igual ao mínimo deve ser válida
        self.assertTrue(self.validator.is_valid("a" * min_length))
    
    def test_input_too_long(self):
        """Testa validação de entrada muito longa."""
        max_length = self.validator.max_length
        
        # Entrada com comprimento igual ao máximo deve ser válida
        self.assertTrue(self.validator.is_valid("a" * max_length))
        
        # Entrada com comprimento maior que o máximo
        self.assertFalse(self.validator.is_valid("a" * (max_length + 1)))
    
    def test_valid_input(self):
        """Testa validação de entradas válidas."""
        self.assertTrue(self.validator.is_valid("As folhas estão amarelando"))
        self.assertTrue(self.validator.is_valid("Minha planta está com manchas pretas nas folhas"))
    
    def test_error_messages(self):
        """Testa as mensagens de erro retornadas."""
        # Mensagem para entrada vazia
        empty_msg = self.validator.get_error_message("")
        self.assertIn("vazia", empty_msg.lower())
        
        # Mensagem para entrada muito curta
        short_msg = self.validator.get_error_message("ab")
        self.assertIn("curta", short_msg.lower())
        
        # Mensagem para entrada muito longa
        long_msg = self.validator.get_error_message("a" * (self.validator.max_length + 1))
        self.assertIn("longa", long_msg.lower())

if __name__ == "__main__":
    unittest.main()

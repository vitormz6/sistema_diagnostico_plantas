"""
Testes para o módulo knowledge_base.py
"""

import unittest
from src.knowledge_base import KnowledgeBase

class TestKnowledgeBase(unittest.TestCase):
    """Testes para a classe KnowledgeBase."""
    
    def setUp(self):
        """Configura o ambiente de teste."""
        self.kb = KnowledgeBase()
    
    def test_rules_exist(self):
        """Testa se as regras foram inicializadas."""
        rules = self.kb.get_rules()
        self.assertIsNotNone(rules)
        self.assertIsInstance(rules, list)
    
    def test_rules_count(self):
        """Testa se existem pelo menos 15 regras na base de conhecimento."""
        rules = self.kb.get_rules()
        self.assertGreaterEqual(len(rules), 15,
                               f"Base de conhecimento deve ter pelo menos 15 regras, mas tem {len(rules)}")
    
    def test_rule_structure(self):
        """Testa se cada regra possui a estrutura correta."""
        rules = self.kb.get_rules()
        for rule in rules:
            self.assertIn("keywords", rule, "Regra deve conter campo 'keywords'")
            self.assertIn("diagnosis", rule, "Regra deve conter campo 'diagnosis'")
            self.assertIn("solution", rule, "Regra deve conter campo 'solution'")
            
            self.assertIsInstance(rule["keywords"], list, "keywords deve ser uma lista")
            self.assertIsInstance(rule["diagnosis"], str, "diagnosis deve ser uma string")
            self.assertIsInstance(rule["solution"], str, "solution deve ser uma string")
            
            # Verifica se há pelo menos uma palavra-chave
            self.assertGreater(len(rule["keywords"]), 0,
                              "Regra deve ter pelo menos uma palavra-chave")
            
            # Verifica se o diagnóstico e a solução não estão vazios
            self.assertGreater(len(rule["diagnosis"]), 0,
                              "Diagnóstico não pode estar vazio")
            self.assertGreater(len(rule["solution"]), 0,
                              "Solução não pode estar vazia")

if __name__ == "__main__":
    unittest.main()

"""
Testes para o módulo inference_engine.py
"""

import unittest
from src.inference_engine import InferenceEngine

class TestInferenceEngine(unittest.TestCase):
    """Testes para a classe InferenceEngine."""
    
    def setUp(self):
        """Configura o ambiente de teste."""
        self.engine = InferenceEngine()
    
    def test_tokenize_input(self):
        """Testa a funcionalidade de tokenização de entrada."""
        test_input = "As folhas estão amarelando e caindo."
        tokens = self.engine.tokenize_input(test_input)
        
        # Verifica se os tokens são gerados corretamente
        self.assertIsInstance(tokens, list)
        self.assertIn("folhas", tokens)
        self.assertIn("amarelando", tokens)
        self.assertIn("caindo", tokens)
        
        # Verifica se a pontuação foi removida
        self.assertNotIn(".", tokens)
        
        # Verifica se todas as palavras estão em minúsculas
        for token in tokens:
            self.assertEqual(token, token.lower())
    
    def test_diagnose_empty_input(self):
        """Testa o comportamento com entrada vazia."""
        results = self.engine.diagnose("")
        self.assertEqual(results, [])
        
        results = self.engine.diagnose("   ")
        self.assertEqual(results, [])
    
    def test_diagnose_with_symptoms(self):
        """Testa o diagnóstico com sintomas conhecidos."""
        # Teste para folhas amarelas
        input_yellow_leaves = "As folhas da minha planta estão ficando amarelas"
        results_yellow = self.engine.diagnose(input_yellow_leaves)
        
        self.assertGreater(len(results_yellow), 0)
        
        # Verifica se cada resultado tem os campos necessários
        for result in results_yellow:
            self.assertIn("diagnosis", result)
            self.assertIn("solution", result)
            self.assertIn("relevance", result)
            
            # Relevância deve ser um valor entre 0 e 1
            self.assertGreaterEqual(result["relevance"], 0)
            self.assertLessEqual(result["relevance"], 1)
    
    def test_match_rules(self):
        """Testa a correspondência entre tokens e regras."""
        tokens = ["folha", "amarela", "caindo"]
        matches = self.engine.match_rules(tokens)
        
        # Deve encontrar correspondências para esses sintomas
        self.assertGreater(len(matches), 0)
        
        # Verifica se as correspondências estão ordenadas por relevância
        for i in range(1, len(matches)):
            self.assertGreaterEqual(matches[i-1]["relevance"], matches[i]["relevance"])

if __name__ == "__main__":
    unittest.main()

import re
import unittest
from app import app

"""Testa o endpoint Naive Bayes (/diagnostico_probabilistico_web).

Garante que:
1. Se houver diagnósticos acima de 10 %, nenhum resultado abaixo desse valor é exibido.
2. Se todos estiverem abaixo de 10 %, o template mostra aviso de baixa confiança.
"""

class TestProbabilisticFilter(unittest.TestCase):
    def setUp(self):
        # Cria cliente de teste do Flask
        self.client = app.test_client()

    def test_probabilities_above_threshold(self):
        # Usa uma descrição genérica que contenha sintomas reconhecíveis
        response = self.client.post('/diagnostico_probabilistico_web', data={'descricao': 'folhas amarelas e caindo'})
        self.assertEqual(response.status_code, 200)

        # Extrai porcentagens do HTML retornado
        html = response.data.decode('utf-8')

        # Se mensagem de baixa confiança aparecer, aceite o resultado
        low_conf_indicator = ('nenhum diagnóstico ultrapassou' in html.lower()) or ('baixa acuracia' in html.lower()) or ('baixa acurácia' in html.lower())
        if low_conf_indicator:
            self.assertIn('confiança', html.lower())
        else:
            # Caso contrário, todas as porcentagens devem ser >= 10
            percentages = [float(p) for p in re.findall(r'(\\d+\\.\\d+)%', html)]
            for pct in percentages:
                self.assertGreaterEqual(pct, 10.0)

if __name__ == '__main__':
    unittest.main() 
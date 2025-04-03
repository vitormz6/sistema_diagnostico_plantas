"""
Interface de usuário baseada em terminal para o sistema especialista.
Responsável por gerenciar a interação com o usuário.
"""

import os
import time
from src.input_validation import InputValidator
from src.inference_engine import InferenceEngine

class UserInterface:
    def __init__(self):
        """Inicializa a interface do usuário com validador e motor de inferência."""
        self.validator = InputValidator()
        self.engine = InferenceEngine()
        
    def clear_screen(self):
        """Limpa a tela do terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def show_welcome(self):
        """Exibe a mensagem de boas-vindas."""
        self.clear_screen()
        print("=" * 80)
        print("  SISTEMA ESPECIALISTA DE DIAGNÓSTICO DE PROBLEMAS EM PLANTAS DOMÉSTICAS")
        print("=" * 80)
        print("\nBem-vindo ao sistema de diagnóstico de plantas!")
        print("Este sistema ajuda a identificar problemas e doenças em suas plantas domésticas.")
        print("\nPara começar, você precisará descrever os sintomas que sua planta está apresentando.")
        print("Seja o mais específico possível para obter um diagnóstico preciso.")
        print("=" * 80)
        input("\nPressione ENTER para continuar...")
        
    def get_user_input(self):
        """
        Solicita e valida a entrada do usuário.
        
        Returns:
            str: Entrada validada ou None se o usuário quiser sair
        """
        while True:
            self.clear_screen()
            print("=" * 80)
            print("  DESCRIÇÃO DOS SINTOMAS")
            print("=" * 80)
            print("\nDescreva os sintomas que sua planta está apresentando:")
            print("(exemplo: 'As folhas estão amarelando e caindo' ou 'Há manchas pretas nas folhas')")
            print("\nDigite 'sair' para encerrar o programa.")
            print("-" * 80)
            
            user_input = input("> ").strip()
            
            if user_input.lower() == 'sair':
                return None
                
            if self.validator.is_valid(user_input):
                return user_input
            else:
                error_message = self.validator.get_error_message(user_input)
                print(f"\nERRO: {error_message}")
                time.sleep(2)
    
    def show_diagnosis(self, results):
        """
        Exibe os resultados do diagnóstico.
        
        Args:
            results (list): Lista de diagnósticos e soluções
        """
        self.clear_screen()
        
        if not results:
            print("=" * 80)
            print("  RESULTADOS DO DIAGNÓSTICO")
            print("=" * 80)
            print("\nNão foi possível identificar o problema com base nos sintomas fornecidos.")
            print("\nSugestões:")
            print("- Tente descrever os sintomas de forma mais detalhada.")
            print("- Inclua informações sobre as folhas, caule, flores, etc.")
            print("- Mencione mudanças recentes no ambiente ou nos cuidados com a planta.")
            print("=" * 80)
        else:
            print("=" * 80)
            print("  RESULTADOS DO DIAGNÓSTICO")
            print("=" * 80)
            
            for i, result in enumerate(results, 1):
                relevance_percent = int(result["relevance"] * 100)
                print(f"\nDiagnóstico {i}: {result['diagnosis']} (Confiança: {relevance_percent}%)")
                print("-" * 80)
                print(f"Solução recomendada:")
                print(f"{result['solution']}")
                print("-" * 80)
                
                # Limita a exibição aos 3 diagnósticos mais relevantes
                if i >= 3:
                    break
                    
            if len(results) > 3:
                print(f"\n* Mais {len(results) - 3} diagnósticos possíveis foram identificados com menor relevância.")
                
        print("\nPressione ENTER para continuar ou digite 'sair' para encerrar...")
        return input("> ").strip().lower() != 'sair'
        
    def run(self):
        """Executa o loop principal da interface do usuário."""
        self.show_welcome()
        
        while True:
            user_input = self.get_user_input()
            
            if user_input is None:
                break
                
            results = self.engine.diagnose(user_input)
            
            if not self.show_diagnosis(results):
                break
                
        self.clear_screen()
        print("Obrigado por usar o Sistema Especialista de Diagnóstico de Plantas!")
        print("Até a próxima!")
        time.sleep(2)

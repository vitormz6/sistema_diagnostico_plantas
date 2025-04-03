#!/usr/bin/env python3
"""
Sistema Especialista de Diagnóstico de Problemas em Plantas Domésticas
Arquivo principal para iniciar o programa

Equipe:
- João Vitor Colombo
- Lucas Henrique da Silva
- Raniel Lira
- Vitor Maiochi Ziehlsdorff
"""

from src.user_interface import UserInterface

def main():
    """Função principal que inicializa o sistema."""
    try:
        # Cria e executa a interface do usuário
        ui = UserInterface()
        ui.run()
    except KeyboardInterrupt:
        # Captura Ctrl+C para encerramento limpo
        print("\n\nPrograma encerrado pelo usuário.")
    except Exception as e:
        # Tratamento genérico de erros
        print(f"\n\nOcorreu um erro inesperado: {str(e)}")
        print("O programa será encerrado.")
    
if __name__ == "__main__":
    main()

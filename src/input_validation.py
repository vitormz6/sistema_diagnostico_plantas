"""
Módulo para validação de entradas do usuário.
Garante que as entradas sejam válidas e adequadas para processamento.
"""

class InputValidator:
    def __init__(self):
        """Inicializa o validador de entrada."""
        self.min_length = 3  # Número mínimo de caracteres para uma entrada válida
        self.max_length = 500  # Número máximo de caracteres para evitar entradas muito longas
    
    def is_valid(self, user_input):
        """
        Verifica se a entrada do usuário é válida.
        
        Args:
            user_input (str): Texto de entrada do usuário
            
        Returns:
            bool: True se a entrada for válida, False caso contrário
        """
        # Verifica se a entrada está vazia
        if not user_input or not user_input.strip():
            return False
        
        # Verifica o comprimento mínimo
        if len(user_input.strip()) < self.min_length:
            return False
        
        # Verifica o comprimento máximo
        if len(user_input) > self.max_length:
            return False
        
        return True
    
    def get_error_message(self, user_input):
        """
        Retorna uma mensagem de erro específica para entradas inválidas.
        
        Args:
            user_input (str): Texto de entrada do usuário
            
        Returns:
            str: Mensagem de erro detalhada
        """
        if not user_input or not user_input.strip():
            return "A descrição dos sintomas não pode estar vazia."
        
        if len(user_input.strip()) < self.min_length:
            return f"A descrição é muito curta. Por favor, forneça mais detalhes (mínimo de {self.min_length} caracteres)."
        
        if len(user_input) > self.max_length:
            return f"A descrição é muito longa. Por favor, resuma os sintomas (máximo de {self.max_length} caracteres)."
        
        return "Entrada inválida. Por favor, tente novamente."

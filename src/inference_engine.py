"""
Mecanismo de inferência do sistema especialista.
Responsável por analisar os sintomas e compará-los com a base de conhecimento.
"""

import re
from src.knowledge_base import KnowledgeBase

class InferenceEngine:
    def __init__(self):
        """Inicializa o mecanismo de inferência com a base de conhecimento."""
        self.knowledge_base = KnowledgeBase()
    
    def tokenize_input(self, user_input):
        """
        Converte a entrada do usuário em tokens (palavras) para análise.
        
        Args:
            user_input (str): Descrição dos sintomas pelo usuário
            
        Returns:
            list: Lista de palavras em minúsculas
        """
        # Remove caracteres especiais e converte para minúsculas
        cleaned_input = re.sub(r'[^\w\s]', ' ', user_input.lower())
        # Divide em palavras e remove espaços extras
        tokens = [word.strip() for word in cleaned_input.split() if word.strip()]
        return tokens
    
    def match_rules(self, user_tokens):
        """
        Compara os tokens de entrada com as regras na base de conhecimento.
        
        Args:
            user_tokens (list): Lista de palavras do usuário
            
        Returns:
            list: Lista de diagnósticos correspondentes, ordenados por relevância
        """
        matches = []
        
        for rule in self.knowledge_base.get_rules():
            # Conta quantas palavras-chave da regra estão presentes na entrada
            # ou se uma palavra do usuário contém a palavra-chave
            matches_count = 0
            for keyword in rule["keywords"]:
                # Verifica correspondência exata
                if keyword in user_tokens:
                    matches_count += 1
                else:
                    # Verifica correspondência parcial (se a palavra-chave está contida em alguma palavra do usuário)
                    for token in user_tokens:
                        if keyword in token or token in keyword:
                            matches_count += 0.5  # Pontuação parcial para correspondências parciais
                            break
            
            # Se houver pelo menos uma correspondência, adiciona à lista
            if matches_count > 0:
                matches.append({
                    "rule": rule,
                    "relevance": matches_count / len(rule["keywords"])  # Pontuação de relevância
                })
        
        # Ordena os resultados por relevância (do mais relevante para o menos)
        matches.sort(key=lambda x: x["relevance"], reverse=True)
        
        return matches
    
    def diagnose(self, user_input):
        """
        Processa a entrada do usuário e retorna diagnósticos.
        
        Args:
            user_input (str): Descrição dos sintomas pelo usuário
            
        Returns:
            list: Lista de diagnósticos encontrados, ordenados por relevância
        """
        if not user_input or not user_input.strip():
            return []
        
        tokens = self.tokenize_input(user_input)
        matches = self.match_rules(tokens)
        
        # Formata os resultados para apresentação
        results = []
        for match in matches:
            rule = match["rule"]
            results.append({
                "diagnosis": rule["diagnosis"],
                "solution": rule["solution"],
                "relevance": match["relevance"]
            })
        
        return results

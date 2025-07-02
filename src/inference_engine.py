"""
Mecanismo de inferência do sistema especialista.
Responsável por analisar os sintomas e compará-los com a base de conhecimento.
"""

import re
from src.knowledge_base import KnowledgeBase
from src.naive_bayes_model import NaiveBayesDiagnostico

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

def diagnostico_probabilistico(sintomas_usuario):
    modelo = NaiveBayesDiagnostico()
    probabilidades = modelo.prever_probabilidades(sintomas_usuario)
    return sorted(probabilidades.items(), key=lambda x: x[1], reverse=True)

def interpretar_entrada(texto_usuario):
    """
    Converte o texto do usuário em um dicionário de sintomas binários.
    Usa a base de conhecimento para detectar sintomas mencionados.
    """
    texto_usuario = texto_usuario.lower()
    kb = KnowledgeBase()
    regras = kb.get_rules()

    # Inicializa todos os sintomas como 0
    sintomas_unicos = [
        "folhas_amareladas", "folhas_marrons", "queda_folhas", "manchas_escuras",
        "pragas_visiveis", "folhas_murchas", "teias_aranha", "crescimento_lento",
        "folhas_deformadas", "caule_mole", "brotos_queimados", "folhas_palidas",
        "mofo_superficial", "raizes_expostas", "folhas_com_furos"
    ]
    sintomas_binarios = {sintoma: 0 for sintoma in sintomas_unicos}

    # Mapeamento de diagnóstico para coluna
    diagnostico_para_coluna = {
        "Excesso de água ou falta de nutrientes": "folhas_amareladas",
        "Falta de água ou baixa umidade": "folhas_marrons",
        "Mudança ambiental ou estresse": "queda_folhas",
        "Fungo ou doença fúngica": "manchas_escuras",
        "Infestação de pulgões ou cochonilhas": "pragas_visiveis",
        "Falta de água ou raízes comprometidas": "folhas_murchas",
        "Ácaros (aranhas vermelhas)": "teias_aranha",
        "Falta de luz ou nutrientes": "crescimento_lento",
        "Ataque de insetos ou deficiência nutricional": "folhas_deformadas",
        "Apodrecimento por excesso de água": "caule_mole",
        "Exposição excessiva ao sol ou fertilizante em excesso": "brotos_queimados",
        "Exposição excessiva ao sol ou deficiência de ferro": "folhas_palidas",
        "Oídio (doença fúngica)": "mofo_superficial",
        "Vaso pequeno ou necessidade de transplante": "raizes_expostas",
        "Ataque de insetos mastigadores": "folhas_com_furos"
    }

    # Ativa os sintomas que aparecem no texto com base nas keywords
    for regra in regras:
        if any(palavra in texto_usuario for palavra in regra["keywords"]):
            coluna = diagnostico_para_coluna.get(regra["diagnosis"])
            if coluna:
                sintomas_binarios[coluna] = 1

    return sintomas_binarios


def diagnostico_probabilistico_texto(texto_usuario):
    """
    Recebe uma frase do usuário e retorna os possíveis diagnósticos com probabilidade.
    """
    sintomas_binarios = interpretar_entrada(texto_usuario)
    modelo = NaiveBayesDiagnostico()
    return modelo.prever_probabilidades(sintomas_binarios)
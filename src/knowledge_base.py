"""
Base de conhecimento para o sistema especialista de diagnóstico de plantas.
Contém regras para identificar problemas comuns em plantas domésticas.
"""

class KnowledgeBase:
    def __init__(self):
        """
        Inicializa a base de conhecimento com regras de diagnóstico.
        Cada regra possui:
        - Palavras-chave: termos que indicam os sintomas
        - Diagnóstico: problema identificado
        - Solução: recomendações para tratar o problema
        """
        self.rules = [
            {
                "keywords": ["folha", "amarela", "amarelada", "amarelando"],
                "diagnosis": "Excesso de água ou falta de nutrientes",
                "solution": "Reduza a frequência de rega e verifique se a planta precisa de fertilizante. "
                           "Certifique-se que o vaso tem boa drenagem."
            },
            {
                "keywords": ["folha", "marrom", "seca", "secando", "pontas"],
                "diagnosis": "Falta de água ou baixa umidade",
                "solution": "Aumente a frequência de rega e considere borrifar água nas folhas "
                           "para aumentar a umidade ao redor da planta."
            },
            {
                "keywords": ["folha", "caindo", "caída", "queda"],
                "diagnosis": "Mudança ambiental ou estresse",
                "solution": "Evite mudanças bruscas de temperatura ou localização. "
                           "Verifique se a planta está exposta a correntes de ar."
            },
            {
                "keywords": ["mancha", "preta", "escura", "folha"],
                "diagnosis": "Fungo ou doença fúngica",
                "solution": "Remova as folhas afetadas, evite molhar as folhas ao regar e "
                           "aplique um fungicida apropriado se necessário."
            },
            {
                "keywords": ["pequenos", "insetos", "praga", "ponto", "branco"],
                "diagnosis": "Infestação de pulgões ou cochonilhas",
                "solution": "Limpe as folhas com água e sabão neutro ou aplique inseticida natural. "
                           "Isole a planta para evitar contaminação de outras."
            },
            {
                "keywords": ["murcha", "murchando", "caída", "caindo", "murcho"],
                "diagnosis": "Falta de água ou raízes comprometidas",
                "solution": "Regue imediatamente se o solo estiver seco. Se o solo estiver úmido, "
                           "verifique as raízes em busca de apodrecimento ou doenças."
            },
            {
                "keywords": ["teia", "aranha", "teia de aranha", "teias"],
                "diagnosis": "Ácaros (aranhas vermelhas)",
                "solution": "Aumente a umidade ao redor da planta. Limpe as folhas com pano úmido "
                           "regularmente e considere usar um acaricida se a infestação for severa."
            },
            {
                "keywords": ["crescimento", "lento", "não cresce", "parou", "estagnou"],
                "diagnosis": "Falta de luz ou nutrientes",
                "solution": "Mova a planta para um local com mais luminosidade e considere "
                           "adicionar fertilizante adequado para estimular o crescimento."
            },
            {
                "keywords": ["folha", "deformada", "enrugada", "enrolada", "torta"],
                "diagnosis": "Ataque de insetos ou deficiência nutricional",
                "solution": "Inspecione a planta em busca de insetos. Aplique fertilizantes "
                           "balanceados e remova as folhas severamente afetadas."
            },
            {
                "keywords": ["caule", "mole", "flexível", "podre", "apodrecendo"],
                "diagnosis": "Apodrecimento por excesso de água",
                "solution": "Pare de regar imediatamente. Verifique o sistema de drenagem do vaso "
                           "e considere replantar em solo novo se necessário."
            },
            {
                "keywords": ["broto", "queimado", "queimando", "ponta", "marrom"],
                "diagnosis": "Exposição excessiva ao sol ou fertilizante em excesso",
                "solution": "Mova a planta para um local com menos luz direta. Se suspeitar de "
                           "fertilizante em excesso, lave o solo com água abundante."
            },
            {
                "keywords": ["folha", "pálida", "esbranquiçada", "clara", "descolorida"],
                "diagnosis": "Exposição excessiva ao sol ou deficiência de ferro",
                "solution": "Mova a planta para um local com menos luz direta. Considere "
                           "adicionar fertilizante rico em ferro."
            },
            {
                "keywords": ["mofo", "branco", "cinza", "pó", "superfície"],
                "diagnosis": "Oídio (doença fúngica)",
                "solution": "Melhore a circulação de ar ao redor da planta. Aplique fungicida "
                           "apropriado e evite molhar as folhas durante a rega."
            },
            {
                "keywords": ["raiz", "exposta", "saindo", "vaso", "para fora"],
                "diagnosis": "Vaso pequeno ou necessidade de transplante",
                "solution": "Transplante a planta para um vaso maior com solo novo e nutritivo. "
                           "Realize este procedimento preferencialmente na primavera."
            },
            {
                "keywords": ["folha", "furos", "comida", "mordida", "buraco"],
                "diagnosis": "Ataque de insetos mastigadores",
                "solution": "Inspecione a planta, especialmente à noite, para identificar os insetos. "
                           "Aplique inseticida natural ou específico para o tipo de inseto."
            }
        ]
    
    def get_rules(self):
        """Retorna todas as regras na base de conhecimento."""
        return self.rules

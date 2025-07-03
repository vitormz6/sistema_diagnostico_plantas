import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder

class NaiveBayesDiagnostico:
    """Wrapper simples para MultinomialNB treinado em *dataset_plantas.csv*.

    • Durante a construção o dataset CSV é lido, as colunas de sintomas são
      usadas como *features* e a coluna *diagnostico* é codificada via
      *LabelEncoder*.
    • O método :py:meth:`prever_probabilidades` recebe um dicionário
      {sintoma: 0/1} e retorna um ``dict`` mapeando diagnóstico → probabilidade.
    """
    def __init__(self, dataset_path="data/dataset_plantas.csv"):
        self.model = MultinomialNB()
        self.label_encoder = LabelEncoder()
        self._train(dataset_path)

    def _train(self, path):
        df = pd.read_csv(path)
        self.sintomas = df.columns[:-1]  # Todas as colunas menos "diagnostico"
        X = df[self.sintomas]
        y = self.label_encoder.fit_transform(df["diagnostico"])
        self.model.fit(X, y)

    def prever_probabilidades(self, sintomas_usuario_dict):
        """Retorna um ``dict`` de probabilidades dado um mapa sintoma→valor.

        Parâmetros
        ----------
        sintomas_usuario_dict : dict[str, int]
            Resultado de :func:`src.inference_engine.interpretar_entrada` ou
            outro processo de extração. Cada chave deve existir em
            ``self.sintomas`` e o valor deve ser 0/1.
        """
        # Criar vetor de entrada com os sintomas fornecidos
        entrada = [[int(sintomas_usuario_dict.get(s, 0)) for s in self.sintomas]]
        # Obter probabilidades dos diagnósticos
        probabilidades = self.model.predict_proba(entrada)[0]
        # Mapear para nomes de diagnósticos
        return dict(zip(self.label_encoder.classes_, probabilidades))

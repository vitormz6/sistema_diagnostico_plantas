import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder

class NaiveBayesDiagnostico:
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
        # Criar vetor de entrada com os sintomas fornecidos
        entrada = [[int(sintomas_usuario_dict.get(s, 0)) for s in self.sintomas]]
        # Obter probabilidades dos diagnósticos
        probabilidades = self.model.predict_proba(entrada)[0]
        # Mapear para nomes de diagnósticos
        return dict(zip(self.label_encoder.classes_, probabilidades))

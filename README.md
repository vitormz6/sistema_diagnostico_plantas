# Sistema Especialista de Diagnóstico de Problemas em Plantas Domésticas

> IA para ajudar hobbistas e profissionais a identificar rapidamente pragas, doenças e deficiências em plantas de interior.

## 1. Descrição do Problema
Manter plantas saudáveis em ambientes domésticos é um desafio comum. Falta de luz, excesso de água, pragas invisíveis… São muitos os fatores que podem levar uma samambaia a murchar ou uma suculenta a apodrecer.

Um jardineiro iniciante geralmente **não sabe interpretar sinais como folhas amarelas, manchas escuras ou teias finas**. Isso resulta em perda de plantas, gastos desnecessários e frustração.

Este projeto fornece um diagnóstico rápido via navegador ou terminal. O usuário descreve os sintomas em linguagem natural e recebe:

* Probabilidades calculadas com **Naive Bayes** (modelo treinado em dataset rotulado)
* Recomendações curtas e objetivas para tratar cada problema

## 2. Como Funciona
1. **Validação de Entrada** – `InputValidator` garante texto suficiente e limita spam.
2. **Motor de Regras** – `InferenceEngine` verifica palavras-chave em uma base de conhecimento com > 15 regras.
3. **Diagnóstico Probabilístico** – Botão "Diagnóstico com NB" usa o modelo Naive Bayes para calcular probabilidades.
4. **Front-end Flask** – Interface responsiva com Bootstrap-Flask, CSS personalizado e JavaScript para UX (loading, modais de palavras-chave, animações).

## 3. Dataset
O arquivo **`data/dataset_plantas.csv`** contém registros rotulados resultantes de pesquisas em blogs, fóruns e artigos acadêmicos.

| Coluna                | Tipo | Descrição                                           |
|-----------------------|------|-----------------------------------------------------|
| folhas_amareladas     | 0/1  | Presença de amarelecimento geral                    |
| folhas_marrons        | 0/1  | Pontas marrons ou necrosadas                        |
| queda_folhas          | 0/1  | Queda excessiva de folhas                           |
| …                     | …    | *(total 15 colunas de sintomas binários)*           |
| diagnostico           | str  | Classe alvo (ex.: **"Falta de água ou baixa umidade"**)|

> Caso nenhuma classe atinja 10 % de probabilidade o sistema exibe todos os resultados, mas alerta sobre **baixa confiança**.

### Como alterar o dataset
Basta substituir o CSV mantendo estrutura de colunas. O modelo é carregado em tempo real na primeira chamada.

## 4. Instalação
```bash
# Clone o repositório e entre na pasta
pip install -r requirements.txt  # Python >= 3.9
```

## 5. Execução
### Versão Web (recomendada)
```bash
python app.py
```
Acesse **http://localhost:5000** e:
1. Descreva sintomas → clique **Analisar Sintomas** (motor de regras).
2. Ou clique **Diagnóstico com NB** para probabilidades.

### Versão Terminal
```bash
python main.py
```

## 6. Estrutura de Diretórios (resumida)
```
├── app.py                  # Flask
├── data/
│   └── dataset_plantas.csv # Dataset rotulado
├── src/
│   ├── inference_engine.py # Motor de regras + utilitários NB
│   ├── naive_bayes_model.py
│   └── …
├── templates/              # HTML Jinja2
├── static/                 # CSS / JS
└── tests/                  # Pytest
```

## 7. Testes
Execute todos os testes unitários:
```bash
pytest -q
```
Inclui:
* Validação de tokenização e inferência (`tests/test_inference_engine.py`)
* Validação de entrada (`tests/test_input_validation.py`)
* Base de conhecimento (`tests/test_knowledge_base.py`)
* **Novo** teste de filtragem probabilística (`tests/test_probabilistic_filter.py`)

## 8. Contribuição & Licença

Código licenciado sob **MIT**. Dados de terceiros mantém suas licenças originais; use com responsabilidade.

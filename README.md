# Sistema Especialista de Diagnóstico de Problemas em Plantas Domésticas

Sistema que ajuda usuários a identificar problemas com plantas domésticas, como pragas, doenças ou requisitos de cuidados.

## Equipe
- João Vitor Colombo
- Lucas Henrique da Silva
- Raniel Lira
- Vitor Maiochi Ziehlsdorff

## Funcionalidades

- Base de conhecimento com 15+ regras de diagnóstico
- Mecanismo de inferência para análise de sintomas
- Interface web interativa e amigável
- Validação de entradas do usuário
- Diagnóstico detalhado com sugestões para solucionar problemas

## Versões do Sistema

### 1. Versão Terminal
Execute o programa usando:
```
python main.py
```

### 2. Versão Web (Flask)
Execute a versão web usando:
```
python app.py
```
Acesse http://localhost:5000/ no seu navegador

## Requisitos

1. Instale as dependências:
```
pip install -r requirements.txt
```

## Como Usar

1. Inicie o servidor web:
```
python app.py
```

2. Acesse o sistema pelo navegador:
```
http://localhost:5000
```

3. Descreva os sintomas da sua planta no formulário e clique em "Analisar Sintomas"

4. O sistema apresentará os diagnósticos mais prováveis e recomendações de tratamento

## Desenvolvimento

### Componentes Principais

- **Base de Conhecimento** (`src/knowledge_base.py`): Contém as regras de diagnóstico
- **Mecanismo de Inferência** (`src/inference_engine.py`): Analisa os sintomas e identifica possíveis problemas
- **Validação de Entrada** (`src/input_validation.py`): Garante que as entradas do usuário sejam válidas
- **Interface Web** (Flask): Proporciona uma experiência de usuário intuitiva
- **Testes Unitários** (`tests/`): Garantem a qualidade e funcionamento correto do sistema

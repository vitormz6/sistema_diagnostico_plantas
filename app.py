"""
Sistema Especialista de Diagnóstico de Problemas em Plantas Domésticas
Versão Web usando Flask

Equipe:
- João Vitor Colombo
- Lucas Henrique da Silva
- Raniel Lira
- Vitor Maiochi Ziehlsdorff
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from src.inference_engine import InferenceEngine
from src.input_validation import InputValidator

app = Flask(__name__)

# Inicializa os componentes do sistema
inference_engine = InferenceEngine()
input_validator = InputValidator()

@app.route('/')
def index():
    """Renderiza a página inicial."""
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    """
    Processa o formulário de sintomas e retorna os resultados
    do diagnóstico como JSON para o frontend.
    """
    symptoms = request.form.get('symptoms', '').strip()
    
    # Valida a entrada
    if not input_validator.is_valid(symptoms):
        error_message = input_validator.get_error_message(symptoms)
        return jsonify({'error': error_message}), 400
    
    # Processa o diagnóstico
    results = inference_engine.diagnose(symptoms)
    
    # Retorna os resultados como JSON
    return jsonify({'results': results})

@app.errorhandler(404)
def page_not_found(e):
    """Trata erros 404 (página não encontrada)."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """Trata erros 500 (erro interno do servidor)."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True) 
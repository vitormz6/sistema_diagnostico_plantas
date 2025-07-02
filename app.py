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
from src.inference_engine import InferenceEngine, diagnostico_probabilistico, diagnostico_probabilistico_texto
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

@app.route("/diagnostico_probabilistico_web", methods=["POST"])
def diagnostico_probabilistico_web():
    texto_usuario = request.form.get("descricao", "").lower()
    resultado = diagnostico_probabilistico_texto(texto_usuario)
    resultado_ordenado = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
    return render_template("resultado_bayes.html", resultados=resultado_ordenado, texto=texto_usuario)


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
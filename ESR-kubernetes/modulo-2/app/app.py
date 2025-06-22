import socket
from flask import Flask, render_template, request, session, redirect, url_for

# Inicializa a aplicação Flask
app = Flask(__name__)

# Chave secreta para o gerenciamento seguro da sessão.
# Em um ambiente de produção, utilize uma chave mais complexa e segura.
app.secret_key = 'chave-secreta-para-demonstracao'

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Rota principal que exibe a página e processa os dados do formulário.
    """
    # Se o formulário for enviado (método POST)
    if request.method == 'POST':
        # Salva o dado do campo de texto na sessão do usuário
        session['user_data'] = request.form['data']
        # Redireciona para a mesma página para evitar reenvio do formulário
        return redirect(url_for('index'))

    # Obtém o hostname da máquina local
    hostname = socket.gethostname()
    # Define a versão da aplicação
    version = "0.0.1"

    # Renderiza a página HTML, passando as variáveis necessárias
    # O método .get() é usado para buscar o dado da sessão sem causar um erro se ele não existir
    return render_template('index.html', hostname=hostname, version=version, saved_data=session.get('user_data'))

if __name__ == '__main__':
    # Executa a aplicação em modo de depuração
    app.run()
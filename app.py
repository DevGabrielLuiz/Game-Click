from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "vibe_kids"

# Inicializamos o SocketIO diretamente com o app
socketio = SocketIO(app, cors_allowed_origins="*")

cliques_globais = 0

@app.route("/")
def home():
    # Passamos a variável 'cliques' para o HTML
    return render_template("index.html", cliques=cliques_globais)

@socketio.on('clique_game')
def handle_clique():
    global cliques_globais
    cliques_globais += 1
    # Envia para todos os navegadores abertos
    emit('atualizar_cliques', {'total_cliques': cliques_globais}, broadcast=True)

if __name__ == "__main__":
    # Rodando no localhost de forma direta e limpa
    socketio.run(app, host='localhost', port=5000, debug=True)
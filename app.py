from flask import Flask, render_template
from models import initialize_database
from models import initialize_prefecture
from routes import blueprints
from models import Prefecture

app = Flask(__name__)

# データベースの初期化
initialize_database()
# エリア集計の初期化
initialize_prefecture()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)

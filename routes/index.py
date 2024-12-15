from flask import Blueprint, render_template, request, redirect, url_for
from models import Prefecture

# Blueprintの作成
index_bp = Blueprint('index', __name__, url_prefix='')


@index_bp.route('/')
def list():
    # データ取得
    prefectures = Prefecture.select()
    
    return render_template('index.html', prefectures = prefectures)
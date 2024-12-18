from flask import Blueprint, render_template, request, redirect, url_for
from models import Name,Prefecture
from routes import name
from peewee import fn

# Blueprintの作成
index_bp = Blueprint('index', __name__, url_prefix='')


@index_bp.route('/')
def list():
    # データ取得
    areas = ["touhoku", "kanto", "chubu", "kinki", "chugoku", "shikoku", "kyushu", "other"]
    prefectures = [
        {
            "area": area,
            "num": Prefecture.select(fn.SUM(Prefecture.num)).where(Prefecture.area == area).scalar() or 0
        }
        for area in areas
    ]
    return render_template('index.html',
                           prefectures = prefectures)
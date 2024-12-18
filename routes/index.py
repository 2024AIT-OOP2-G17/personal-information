from flask import Blueprint, render_template, request, redirect, url_for
from models import Name,Prefecture
from routes import name,zodiac
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
    counts = zodiac.count_birthdays_by_month()
    labels = [i for i in range(1, 13)]  # または list(range(1, 13))
    data = [counts[month] for month in labels]
    zodiac_cntdata = zodiac.count_zodiacs()
    
    return render_template('index.html',
                            prefectures = prefectures,
                            labels=labels,
                            data=data,
                            zodiac_cntdata=zodiac_cntdata)

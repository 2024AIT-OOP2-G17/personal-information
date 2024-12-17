from flask import Blueprint, render_template, request, redirect, url_for
from models import Zodiac
from collections import defaultdict

# Blueprintの作成
zodiac_bp = Blueprint('zodiac', __name__, url_prefix='/zodiacs')


@zodiac_bp.route('/')
def list():
    
    # データ取得
    zodiacs = Zodiac.select()

    return render_template('zodiac_list.html', title='星座一覧', items=zodiacs)

def count_birthdays_by_month():
    birthday_counts = defaultdict(int)
    for zodiac in Zodiac.select():
        birthday = zodiac.birthday
        month = int(str(birthday)[4:6])  # 生年月日から月を抽出
        birthday_counts[month] += 1

    return birthday_counts
@zodiac_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        birthday = request.form['birthday']
        zodiac_signs = request.form['zodiac_signs']
        Zodiac.create(birthday=birthday, zodiac_signs=zodiac_signs)
        return redirect(url_for('zodiac.list'))
    
    return render_template('zodiac_add.html')


@zodiac_bp.route('/edit/<string:zodiac_birthday>', methods=['GET', 'POST'])
def edit(zodiac_birthday):
    zodiac = Zodiac.get_or_none(Zodiac.birthday == zodiac_birthday)
    if not zodiac:
        return redirect(url_for('zodiac.list'))

    if request.method == 'POST':
        zodiac.birthday = request.form['birthday']
        zodiac.zodiac_signs = request.form['zodiac_signs']
        zodiac.save()
        return redirect(url_for('zodiac.list'))

    return render_template('zodiac_edit.html', zodiac=zodiac)


@zodiac_bp.route('/graph/month')
def graph_month():
    counts = count_birthdays_by_month()
    labels = [i for i in range(1, 13)]  # または list(range(1, 13))
    data = [counts[month] for month in labels]
    return render_template('zodiac_graph_month.html',
                         labels=labels,
                         data=data)
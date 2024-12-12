from flask import Blueprint, render_template, request, redirect, url_for
from models import Zodiac

# Blueprintの作成
zodiac_bp = Blueprint('zodiac', __name__, url_prefix='/zodiacs')


@zodiac_bp.route('/')
def list():
    
    # データ取得
    zodiacs = Zodiac.select()

    return render_template('zodiac_list.html', title='星座一覧', items=zodiacs)


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
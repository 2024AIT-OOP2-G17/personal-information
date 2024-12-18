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
    zodiac_cntdata = count_zodiacs()
    return render_template('zodiac_graph_month.html',
                         labels=labels,
                         data=data,
                         zodiac_cntdata=zodiac_cntdata)


def count_zodiacs():
    zodiac_counts = [0] * 13
    for zodiac in Zodiac.select():
        judge_zodiac = zodiac.zodiac_signs
        if judge_zodiac == '牡羊座' or judge_zodiac == 'おひつじ座':
            zodiac_counts[0] += 1

        elif judge_zodiac == '牡牛座' or judge_zodiac == 'おうし座':
            zodiac_counts[1] += 1

        elif judge_zodiac == '双子座' or judge_zodiac == 'ふたご座':
            zodiac_counts[2] += 1

        elif judge_zodiac == '蟹座' or judge_zodiac == 'かに座':
            zodiac_counts[3] += 1

        elif judge_zodiac == '獅子座' or judge_zodiac == 'しし座':
            zodiac_counts[4] += 1

        elif judge_zodiac == '乙女座' or judge_zodiac == 'おとめ座':
            zodiac_counts[5] += 1

        elif judge_zodiac == '天秤座' or judge_zodiac == 'てんびん座':
            zodiac_counts[6] += 1

        elif judge_zodiac == '蠍座' or judge_zodiac == 'さそり座':
            zodiac_counts[7] += 1

        elif judge_zodiac == '射手座' or judge_zodiac == 'いて座':
            zodiac_counts[8] += 1

        elif judge_zodiac == '山羊座' or judge_zodiac == 'やぎ座':
            zodiac_counts[9] += 1

        elif judge_zodiac == '水瓶座' or judge_zodiac == 'みずがめ座':
            zodiac_counts[10] += 1

        elif judge_zodiac == '魚座' or judge_zodiac == 'うお座':
            zodiac_counts[11] += 1

        else:
            zodiac_counts[12] += 1

    return zodiac_counts
  
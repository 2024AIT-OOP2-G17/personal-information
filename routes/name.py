from flask import Blueprint, render_template, request, redirect, url_for
from models import Name
from models import Prefecture

# Blueprintの作成
name_bp = Blueprint('name', __name__, url_prefix='/names')


@name_bp.route('/')
def list():
    
    # データ取得
    names = Name.select()

    return render_template('name_list.html', title='ユーザー一覧', items=names)


@name_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        area(phone, 1)
        Name.create(name=name, phone=phone)
        return redirect(url_for('name.list'))
    
    return render_template('name_add.html')


@name_bp.route('/edit/<int:name_id>', methods=['GET', 'POST'])
def edit(name_id):
    name = Name.get_or_none(Name.id == name_id)
    if not name:
        return redirect(url_for('name.list'))

    if request.method == 'POST':
        phone_ago = name.phone
        name.name = request.form['name']
        name.phone = request.form['phone']
        name.save()
        area(phone_ago, -1)
        area(name.phone, 1)
        return redirect(url_for('name.list'))

    return render_template('name_edit.html', name=name)

# 名前による判別
def area(phone, num):
    match phone:
        case "100":
            update_area = Prefecture.get(Prefecture.area=='kanto')
        case "111":
            update_area = Prefecture.get(Prefecture.area=='kinki')
        case _:
            update_area = Prefecture.get(Prefecture.area=='other')
    update_area.num = update_area.num + num
    update_area.save() 
from flask import Blueprint, render_template, request, redirect, url_for
from models import Name

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
        Name.create(name=name, phone=phone)
        return redirect(url_for('name.list'))
    
    return render_template('name_add.html')


@name_bp.route('/edit/<int:name_id>', methods=['GET', 'POST'])
def edit(name_id):
    name = Name.get_or_none(Name.id == name_id)
    if not name:
        return redirect(url_for('name.list'))

    if request.method == 'POST':
        name.name = request.form['name']
        name.phone = request.form['phone']
        name.save()
        return redirect(url_for('name.list'))

    return render_template('name_edit.html', name=name)
from peewee import SqliteDatabase
from .db import db
from .name import Name
from .zodiac import Zodiac
from .prefecture import Prefecture

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    Name,
    Zodiac,
    Prefecture
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()

def initialize_prefecture():
    count = Prefecture.select().count()
    if count == 0:
        Prefecture.create(area="tohoku", num=0)
        Prefecture.create(area="kanto", num=0)
        Prefecture.create(area="chubu", num=0)
        Prefecture.create(area="kinki", num=0)
        Prefecture.create(area="chugoku", num=0)
        Prefecture.create(area="sikoku", num=0)
        Prefecture.create(area="kyushu", num=0)
        Prefecture.create(area="other", num=0)
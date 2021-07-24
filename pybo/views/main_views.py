from flask import Blueprint

# Blurprint 클래스로 생성한 객체
bp = Blueprint('main', __name__, url_prefix='/')


# 특정 주소에 접속시 다음 함수를 호출하는 데코레이터
# 데코레이터: 함수를 변경하지 않고 기능을 덧붙일 수 있도록 해주는 함수
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo index'

from flask import Blueprint, url_for
from werkzeug.utils import redirect

# Blurprint 클래스로 생성한 객체
bp = Blueprint('main', __name__, url_prefix='/')


# 특정 주소에 접속시 다음 함수를 호출하는 데코레이터
# 데코레이터: 함수를 변경하지 않고 기능을 덧붙일 수 있도록 해주는 함수
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    # redirect를 통해 입력받은 URL(url_for('question._list')로 리다이렉트
    # url_for는 question 블루프린트 URL + _list 함수에 등록된 URL 반환
    # 즉, /question/ + /list = /question/list
    return redirect(url_for('question._list'))

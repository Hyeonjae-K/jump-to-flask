from flask import Flask


# create_app()은 플라스크에 정의된 내부 함수
def create_app():
    # __name__이라는 변수에 모듈명이 담김
    # pybo.py라는 모듈이 실행되는 것이므로 'pybo'라는 문자열이 담김
    app = Flask(__name__)

    # 블루프린트를 사용하도록 변경, bp 등록
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app

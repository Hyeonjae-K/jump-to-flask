from flask import Flask


# create_app()은 플라스크에 정의된 내부 함수
def create_app():
    # __name__이라는 변수에 모듈명이 담김
    # pybo.py라는 모듈이 실행되는 것이므로 'pybo'라는 문자열이 담김
    app = Flask(__name__)

    # 특정 주소에 접속시 다음 함수를 호출하는 데코레이터
    # 데코레이터: 함수를 변경하지 않고 기능을 덧붙일 수 있도록 해주는 함수
    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app

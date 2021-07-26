from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# db, migrate 객체 생성
db = SQLAlchemy()
migrate = Migrate()


# create_app()은 플라스크에 정의된 내부 함수
def create_app():
    # __name__이라는 변수에 모듈명이 담김
    # pybo.py라는 모듈이 실행되는 것이므로 'pybo'라는 문자열이 담김
    app = Flask(__name__)
    # config.py에 작성된 항목을 app.config 환경 변수로 부름
    app.config.from_object(config)

    # 다른 모듈에서 불러올 수 있도록 함수 밖에서 선언 후 함수 내에서 초기화
    db.init_app(app)
    migrate.init_app(app, db)

    # 모델(models.py)을 Migrate 기능이 인식할 수 있도록 함
    from . import models

    # 블루프린트를 사용하도록 변경, bp 등록
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    # 생성한 필터 import
    from .filter import format_datetime
    # 'datetime'이라는 이름으로 필터 등록
    app.jinja_env.filters['datetime'] = format_datetime

    return app

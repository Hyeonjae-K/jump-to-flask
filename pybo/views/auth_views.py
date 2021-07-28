from re import DEBUG
from flask import Blueprint,  url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    # 메소드가 'POST'이고 데이터가 적합하다면
    if request.method == 'POST' and form.validate_on_submit():
        # User 테이블에 폼에서 입력한 username 데이터가 있는지 검사
        user = User.query.filter_by(username=form.username.data).first()
        # 없을 경우
        if not user:
            # 데이터베이스에 추가
            # 비밀번호는 그대로 저장하지 않고 generate_password_hash함수로 암호화하여 저장
            user = User(username=form.username.data, password=generate_password_hash(
                form.password1.data), email=form.email.data)
            db.session.add(user)
            db.session.commit()
            # main 페이지로 이동
            return redirect(url_for('main.index'))
        # 있을 경우
        else:
            # 다음 문구와 함께 오류 발생
            flash('이미 존재하는 사용자입니다.')
    # 'GET' 메소드일 경우 signup 템플릿 반환
    return render_template('auth/signup.html', form=form)


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    # POST 방식 요청일 경우 로그인 수행
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        # username을 통해 데이터베이스에 사용자가 있는지 검사
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        # password를 암호화 하여 check_password_hash 함수를 통해 데이터베이스의 비밀번호와 일치하는지 비교
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        # error가 없을 경우
        if error is None:
            # session: 플라스크 서버를 구동하는 동안 영구히 참조할 수 있는 값
            # 로그인한 사용자인지 판별 가능(시간제한이 있어 일정 시간 이후 자동 삭제)
            # session을 초기화
            session.clear()
            # session에 키와 키값 저장
            session['user_id'] = user.id
            # main 페이지로 이동
            return redirect(url_for('main.index'))
        flash(error)
    # GET 방식일 경우 로그인 템플릿 렌더링
    return render_template('auth/login.html', form=form)


# before_app_request 애너테이션이 적용된 함수는 라우트 함수보다 먼저 실행
@bp.before_app_request
# 라우트 함수 실행 전에 load_logged_in_user 함수 실행
def load_logged_in_user():
    # 세션에 유저가 저장되어 있는지 확인(로그인 상태인지 확인)
    user_id = session.get('user_id')
    # g는 플라스크의 컨텍스트 변수로 request와 마찬가지로 [요청 -> 응답] 과정에서 유효
    # 세션에 유저가 없으면 g.user에 None을 넣음
    if user_id is None:
        g.user = None
    # 세션에 유저가 있으면 g.user에 사용자 정보를 넣음
    else:
        g.user = User.query.get(user_id)


# /logout/ 라우트 접속시 logout 함수 실행
@bp.route('/logout/')
def logout():
    # 세션 초기화(세션 초기화시 g.user도 None이 됨)
    session.clear()
    # 메인 화면으로 리다이렉트
    return redirect(url_for('main.index'))

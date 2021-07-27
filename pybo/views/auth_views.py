from re import DEBUG
from flask import Blueprint,  url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from wtforms.validators import Email

from pybo import db
from pybo.forms import UserCreateForm
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

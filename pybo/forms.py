from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# Flask-WTF 모듈의 FlaskForm 클래스 상속받음
class QuestionForm(FlaskForm):
    # 제목은 글자 수 제한이 있으므로 StringField 사용
    # validators를 통해 필드값 검증(필수 여부, 이메일 등)
    # 오류 메세지 한글화
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    # 내용은 글자 수 제한이 없으므로 TextAreaField 사용
    # <input type="text"> or <textarea>에 대응하는 자료형
    # 오류 메세지 한글화
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class UserCreateForm(FlaskForm):
    # 길이를 3~25자로 제한
    username = StringField('사용자이름', validators=[
                           DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired()])
    # 비밀번호 확인을 위해 EqualTo 검증 추가
    password2 = PasswordField('비밀번호확인', validators=[
                              DataRequired(), EqualTo('password1', '비밀번호가 일치하지 않습니다')])
    # 이메일 형식 검증을 위해 Email 추가
    email = EmailField('이메일', validators=[DataRequired(), Email()])

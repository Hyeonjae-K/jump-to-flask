from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


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

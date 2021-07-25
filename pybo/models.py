from pybo import db


# 모델의 기본 클래스인 db.Model을 상속받음
class Question(db.Model):
    # 고유 번호, 제목, 내용, 작성일시
    # id는 기본 키(primary_key)로 데이터를 구분하는 유효한 값이므로 중복 X
    # 타입이 db.Integer인 기본 키는 속성값을 1씩 자동으로 증가하여 저장
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 기존 모델(질문 모델)과 연결(외부 키(foreign key))
    # 'question.id'는 Question 모델의 id 속성을 의미(테이블명.컬럼명)
    # ondelete는 삭제 연동, 'CASCADE'에 의해 질문 삭제시 답변도 함께 삭제
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.id', ondelete='CASCADE'))
    # 답변 모델에서 질문 모델을 참조(질문의 제목 참조: answer.question.subject)
    # backref(역참조)를 통해 질문에서 답변 참조
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

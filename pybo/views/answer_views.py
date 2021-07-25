from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


# 템플릿의 form 엘리먼트와 동일한 POST 방식으로 메소드 지정
@bp.route('/create/<int:question_id>', methods=['POST'])
# URL에서 questiono_id 전달
def create(question_id):
    question = Question.query.get_or_404(question_id)
    # request를 통해 전송된 데이터 중 name 속성이 'content'인 값 추출
    content = request.form['content']
    answer = Answer(content=content, create_date=datetime.now())
    # 질문에 달린 답변 목록에 answer 추가
    question.answer_set.append(answer)
    db.session.commit()
    # 답변 생성 후 redirect를 통해 화면 이동
    return redirect(url_for('question.detail', question_id=question_id))

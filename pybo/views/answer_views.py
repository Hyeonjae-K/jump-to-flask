from datetime import datetime

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from .. import db
from ..forms import AnswerForm
from ..models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


# 템플릿의 form 엘리먼트와 동일한 POST 방식으로 메소드 지정
@bp.route('/create/<int:question_id>', methods=['POST'])
# URL에서 questiono_id 전달
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    # form.validate_on_submit을 통해 데이터 적합성 점검
    if form.validate_on_submit():
        # request를 통해 전송된 데이터 중 name 속성이 'content'인 값 추출
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now())
        # 질문에 달린 답변 목록에 answer 추가
        question.answer_set.append(answer)
        db.session.commit()
        # 답변 생성 후 redirect를 통해 화면 이동
        return redirect(url_for('question.detail', question_id=question_id))
    # 질문 페이지 반환
    return render_template('question/question_detail.html', question=question, form=form)

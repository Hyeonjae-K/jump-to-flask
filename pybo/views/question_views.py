from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    # 작성일시 역순(최신순)으로 질문 목록 조회
    question_list = Question.query.order_by(Question.create_date.desc())
    # 조회된 질문 목록을 템플릿으로 전달
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
# question_id에 라우트 매핑 규칙에 사용한 <int:question_id>가 전달
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)

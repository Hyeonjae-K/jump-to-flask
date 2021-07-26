from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from ..models import Question
from ..forms import QuestionForm, AnswerForm

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    # GET 방식으로 요청한 URL에서 page값을 가져옴
    page = request.args.get('page', type=int, default=1)
    # 작성일시 역순(최신순)으로 질문 목록 조회
    question_list = Question.query.order_by(Question.create_date.desc())
    # 조회한 question_list에 페이징 적용(조회할 페이지, 페이지당 보여줄 게시물)
    question_list = question_list.paginate(page, per_page=10)
    # 조회된 질문 목록을 템플릿으로 전달
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
# question_id에 라우트 매핑 규칙에 사용한 <int:question_id>가 전달
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)


@bp.route('/create/', methods=['GET', 'POST'])
def create():
    # QuestionForm(질문 등록을 할 때 사용하는 플라스크 폼) 객체 생성
    form = QuestionForm()
    # request.method를 통해 요청된 전송 방식 파악
    # form.validate_on_submit을 통해 데이터 적합성 점검
    if request.method == 'POST' and form.validate_on_submit():
        # form.'target'.data를 통해 전송받은 데이터에서 원하는 부분 추출
        question = Question(subject=form.subject.data,
                            content=form.content.data, create_date=datetime.now())
        # 데이터베이스에 질문 저장
        db.session.add(question)
        db.session.commit()
        # main.index 페이지로 이동
        return redirect(url_for('main.index'))
    # 랜더링할 때 form 객체 전달
    return render_template('question/question_form.html', form=form)

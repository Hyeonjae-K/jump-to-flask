# datetime 객체를 보기 편한 문자열로 변환하여 반환하는 필터
def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'):
    return value.strftime(fmt)

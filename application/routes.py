
from application import app
from handlers.home_handler import *
from handlers.grade_handler import *


app.add_url_rule('/', 'home', view_func=home, methods=['GET'])
app.add_url_rule('/average_grade', 'average_grade', view_func=average_grade, methods=['GET'])

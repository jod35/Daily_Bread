from flask import Blueprint,render_template,url_for,request
from ..extensions.database import db

app_bp=Blueprint('app',__name__,template_folder='templates',static_folder='static')

@app_bp.route('/')
def index():

    context={
        'title':"Home Page"
    }
    return render_template('index.html',**context)
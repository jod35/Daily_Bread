from flask import Blueprint, render_template
from .models import Record

ui_bp = Blueprint('ui', __name__)


@ui_bp.route('/')
def index():
    verses = Record.query.order_by(Record.id.desc()).all()

    count= len(verses)
    return render_template('index.html', verses=verses,count=count)

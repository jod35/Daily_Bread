from flask import Blueprint,render_template,url_for,request,flash,redirect
from ..extensions.database import db
from ..models.records import Verse,Note

app_bp=Blueprint('app',__name__,template_folder='templates',static_folder='static')

@app_bp.route('/',methods=['GET','POST'])
def index():
    records=Verse.query.all()

    if request.method =="POST":
        bible_verse=request.form.get('bible_verse')
        notes=request.form.get('notes')

        new_verse=Verse(bible_verse=bible_verse)

        new_verse.save()

        flash("New Verse added successfully.")

        return redirect(url_for('app.index'))


        

    context={
        'title':"Home Page",
        'records':records
    }
    return render_template('index.html',**context)
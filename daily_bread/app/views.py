from flask import Blueprint,render_template,url_for,request,flash,redirect
from ..extensions.database import db
from ..models.records import Verse,Note
from time import strftime

app_bp=Blueprint('app',__name__,template_folder='templates',static_folder='static')

@app_bp.route('/',methods=['GET','POST'])
def index():
    records=Verse.query.order_by(Verse.bible_verse).all()

    if request.method =="POST":
        bible_verse=request.form.get('bible_verse')

        notes=request.form.get('notes')
        new_verse=Verse(bible_verse=bible_verse)
        new_verse.save()
        flash("New Verse added successfully.")
        return redirect(url_for('app.index'))

    context={
        'title':"Home Page",
        'records':records,
    }
    return render_template('index.html',**context)



@app_bp.route('/edit/<int:id>',methods=['GET','POST'])
def edit_verse(id):
    verse_to_edit=Verse.query.get_or_404(id)

    if request.method == "POST":
        bible_verse=request.form.get('bible_verse')
        verse_to_edit.bible_verse=bible_verse

        db.session.commit()

        flash("Record Updated Successfully")

        return redirect(url_for('app.index'))
    context={
        'verse_to_edit':verse_to_edit
    }
    return render_template('edit.html',**context)
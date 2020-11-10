from flask import (Blueprint, render_template, url_for,
                   request, flash, redirect, jsonify, make_response)
from ..extensions.database import db
from ..models.records import Verse,VerseSchema
from time import strftime

app_bp = Blueprint(
    'app', __name__, template_folder='templates', static_folder='static')



@app_bp.route('/', methods=['GET'])
def index():
    records = Verse.query.order_by(Verse.bible_verse).all()
        
    context = {
        'title': "Home Page",
        'records': records,
    }
    return render_template('index.html', **context)

@app_bp.route('/add_verse',methods=['POST'])
def create_verse():
    print(f"/n{request.json}/n")
    bible_verse = request.json.get('bible_verse')
    notes = request.json.get('notes')

    new_verse = Verse(bible_verse=bible_verse, notes=notes)
    new_verse.save()

    verse_schema=VerseSchema(many=True)

    records = Verse.query.order_by(Verse.bible_verse).all()

    records=verse_schema.dump(records)



    return make_response(
        jsonify({"message":"Verse Added Sucessfully",
                    "records":records
        }),201
    )

@app_bp.route('/get_verses',methods=['GET'])
def get_verses():
    verses=Verse.query.order_by(Verse.bible_verse).all()

    verse_schema=VerseSchema(many=True)

    records=verse_schema.dump(verses)

    return make_response(
        jsonify(
            {"success":True,
             "verses":records}
        )
    )


@app_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_verse(id):
    verse_to_edit = Verse.query.get_or_404(id)

    if request.method == "POST":
        bible_verse = request.form.get('bible_verse')
        notes = request.form.get('notes')

        verse_to_edit.bible_verse = bible_verse
        verse_to_edit.notes = notes

        db.session.commit()

        flash("Record Updated Successfully")

        return redirect(url_for('app.index'))
    context = {
        'verse_to_edit': verse_to_edit
    }
    return render_template('edit.html', **context)


@app_bp.route('/details/<int:id>', methods=['GET', 'POST'])
def verse_details(id):
    verse = Verse.query.get_or_404(id)

    context = {
        'verse': verse
    }
    return render_template('versedetails.html', **context)


@app_bp.route('/delete/<int:id>')
def delete_verse(id):
    verse_to_delete = Verse.query.get_or_404(id)

    verse_to_delete.delete()
    flash("Record deleted successfully")

    return redirect(url_for('app.index'))

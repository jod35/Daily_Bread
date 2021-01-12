from flask import Blueprint, jsonify, request, make_response
from .extensions import db
from .models import Record
from .schema import RecordSchema


api_bp = Blueprint('api', __name__)


@api_bp.route('/')
def hello():
    return jsonify({'message': "hello"})


@api_bp.route('/verses', methods=['GET'])
def get_all_verses():
    verses = Record.query.all()

    response = RecordSchema(many=True).dump(verses)

    return make_response(jsonify(
        {"verses": response}
    ))


@api_bp.route('/verses', methods=['POST'])
def create_verse():
    data = request.get_json()

    new_verse = Record(verse=data.get('verse'), notes=data.get('notes'))

    new_verse.save()

    __verse = RecordSchema(many=False).dump(new_verse)

    return make_response(jsonify({
        "message": "CREATED",
        "verse": __verse
    }), 201)


@api_bp.route('/verse/<int:id>', methods=['GET'])
def get_a_record(id):
    verse = Record.query.get_or_404(id)

    response = RecordSchema().dump(verse)

    return make_response(jsonify({"success": True, "verse": response}), 200)


@api_bp.route('/verse/<int:id>', methods=['PUT'])
def update_a_resource(id):
    verse = Record.query.get_or_404(id)

    data = request.get_json()

    verse.verse = data.get('verse')

    verse.notes = data.get('notes')

    db.session.commit()

    response = RecordSchema().dump(verse)

    return make_response(jsonify({"message": "UPDATED", "verse": response}), 200)


@api_bp.route('/verse/<int:id>', methods=['DELETE'])
def delete_a_resource(id):
    verse = Record.query.get_or_404(id)

    verse.delete()

    response = RecordSchema().dump(verse)

    return make_response(jsonify({"message": "DELETED", "verse": response}), 200)


@api_bp.errorhandler(404)
def not_found(err):
    return make_response(jsonify({"message": "Resource Not Found"}), 404)

from marshmallow import Schema,fields


class RecordSchema(Schema):
	id=fields.Str()
	verse=fields.Str()
	notes=fields.Str()

	
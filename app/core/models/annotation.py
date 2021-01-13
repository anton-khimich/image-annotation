from mongoengine import EmbeddedDocument, StringField, IntField


class Annotation(EmbeddedDocument):
    label = StringField(required=True)
    x1 = IntField(required=True)
    y1 = IntField(required=True)
    x2 = IntField(required=True)
    y2 = IntField(required=True)

from mongoengine import Document, StringField, ListField, EmbeddedDocumentField
from app.core.models.annotation import Annotation


class Task(Document):
    title = StringField(required=True)
    image_url = StringField(required=True)
    annotations = ListField(EmbeddedDocumentField(Annotation))
    assigned = StringField()

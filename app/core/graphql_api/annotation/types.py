from graphene import ObjectType, InputObjectType, String, Int


class AnnotationInput(InputObjectType):
    label = String(required=True)
    x1 = Int(required=True)
    y1 = Int(required=True)
    x2 = Int(required=True)
    y2 = Int(required=True)


class AnnotationOutput(ObjectType):
    label = String(required=True)
    x1 = Int(required=True)
    y1 = Int(required=True)
    x2 = Int(required=True)
    y2 = Int(required=True)

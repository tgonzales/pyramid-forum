from formencode import Schema, validators


class TopicSchema(Schema):
    title = validators.String(not_empty=True, max=100)

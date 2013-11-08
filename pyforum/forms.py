from formencode import Schema, validators


class TopicSchema(Schema):
    title = validators.String(not_empty=True, max=200)


class MessageSchema(Schema):
    name = validators.String(not_empty=True, max=100)
    description = validators.String(not_empty=True, max=800)
from mongoengine import Document, StringField


class Topic(Document):
    title = StringField(required=True)

    @staticmethod
    def add(context):
        topic = Topic(title=context['title'])
        topic.save()
        return topic

    @staticmethod
    def remove(topic_id):
        topic = Topic.objects.get(pk=topic_id)
        topic.delete()


class Message(Document):
    name = StringField(required=True)
    topic = StringField(required=True) 
    description = StringField(required=False) 

    @staticmethod
    def add(message):
        message = Message(name=message['name'],
                        topic=message['topic'],
                        description=message['description'])
        message.save()
        return message

    @staticmethod
    def remove(message_id):
        message = Message.objects.get(pk=message_id)
        message.delete()
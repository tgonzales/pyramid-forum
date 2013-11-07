from mongoengine import Document, StringField


class Topic(Document):
    title = StringField(required=True)


    @staticmethod
    def add(topic):
        topic = Topic(title=topic['title'])
        topic.save()
        return topic

    @staticmethod
    def remove(topic_id):
        topic = Topic.objects.get(pk=topic_id)
        topic.delete()
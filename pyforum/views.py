from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from models import Topic, Message
from forms import TopicSchema, MessageSchema

@view_defaults(renderer='/templates/home.jinja2')
class PyForumViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'name': 'Wellcome to the PyForum'}

    @view_config(route_name='pyforum_view', renderer='templates/pyforum_view.jinja2')
    def pyforum_view(self):
        topics = Topic.objects
        form = Form(self.request,schema=TopicSchema())
        if form.validate():
            context = {'title' : form.data['title']}
            Topic.add(context)
            return HTTPFound(location='/list')
        return {'title': 'List View PyForum',
                'topics':topics,
                'form' : FormRenderer(form)
            }


    @view_config(route_name='pyforum_message_view', 
                    renderer='templates/pyforum_message_view.jinja2')
    def pyforum_message_view(self):
        id_topic = self.request.matchdict['id_topic']
        topic_title = self.request.matchdict['topic_title']
        topics = Message.objects().filter(topic__icontains=id_topic)
        form = Form(self.request,schema=MessageSchema())
        if form.validate():
            context = {'name' : form.data['name'],
                        'description': form.data['description'],
                        'topic': id_topic}
            Message.add(context)
            return HTTPFound(location='/message_list/{0}/{1}'.format(id_topic,topic_title))

        return {'title': 'List View PyForum',
                'topics':topics,
                'id_topic':id_topic,
                'topic_title':topic_title,
                'form' : FormRenderer(form)
            }


@view_config(route_name='pyforum_delete')
def pyforum_delete(request):
    topic_id = request.matchdict.get('id', None)
    Topic.remove(topic_id)
    return HTTPFound(location='/list')

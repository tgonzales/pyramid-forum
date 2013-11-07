from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from models import Topic
from forms import TopicSchema

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
        return {'title': 'List View PyForum',
                'topics':topics
            }

    @view_config(route_name='pyforum_add', renderer='templates/pyforum_add.jinja2')
    def pyforum_add(self):
        form = Form(self.request,schema=TopicSchema())
        if form.validate():
            topic = form.data['title']
            context = {'title' : topic}
            Topic.add(context)
            return HTTPFound(location='/list')
        return {'form' : FormRenderer(form)}

@view_config(route_name='pyforum_delete')
def pyforum_delete(request):
    topic_id = request.matchdict.get('id', None)
    Topic.remove(topic_id)
    return HTTPFound(location='/list')

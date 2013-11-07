import unittest

from pyramid import testing


class PyForumViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from views import PyForumViews

        request = testing.DummyRequest()
        inst = PyForumViews(request)
        response = inst.home()
        self.assertEqual('Wellcome to the PyForum', response['name'])

    def test_list(self):
        from views import PyForumViews

        request = testing.DummyRequest()
        inst = PyForumViews(request)
        response = inst.pyforum_view()
        self.assertEqual('List View PyForum', response['title'])


class PyForumFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyforum import main

        settings = {
            'pyramid.includes': [
                'pyramid_jinja2'
            ]
        }
        app = main({}, **settings)
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Wellcome to the PyForum</h1>', res.body)

    def test_pyforum_view(self):
        res = self.testapp.get('/list', status=200)
        self.assertIn(b'<h3>PyForum - Topic Available</h3>', res.body)
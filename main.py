import webapp2 # NOTE: pull in a library for using appengine
import jinja2
import os
# from google.appengine.api import
import json
# from Models import ReminderData
the_jinja_env=jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class UsernameHandler(webapp2.RequestHandler):
    def get(self):
        Username_template=the_jinja_env.get_template('templates/Username.html')
        self.response.write(Username_template.render())


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is the home page')
    def post(self):
        Home_template=the_jinja_env.get_template('templates/Home.html')
        self.response.write(Home_template.render())


class DataStore(webapp2.RequestHandler):
    def get(self):
        def post(self):
            optionwater = request.form.get('Water')
            if optionwater:
                optionwater=True
            optionshave = request.form.get('Shave')
            if optionshave:
                optionshave=True
            optionsleep = request.form.get('Sleep')
            if name3:
                optionsleep=True
            self.response.write(optionshave,optionsleep,optionwater)

app=webapp2.WSGIApplication([
('/',UsernameHandler),
('/Main',MainHandler),
('/Data',DataStore)

],debug=True)
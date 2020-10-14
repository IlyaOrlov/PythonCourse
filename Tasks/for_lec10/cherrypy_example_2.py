import cherrypy


class Hello:
    @cherrypy.expose
    def index(self):
        with open('index.html', 'r') as f:
            s = f.read()
            return s.replace(r'{%_%}', 'name')

    @cherrypy.expose
    def hello(self, name):
        return f'Hello, {name}'


if __name__ == '__main__':
    cherrypy.quickstart(Hello(), '/')
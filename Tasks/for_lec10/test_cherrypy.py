import cherrypy

class HelloWorld:

    @cherrypy.expose
    def index(self):
        return 'This is not easy!'

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8099})
    cherrypy.quickstart(HelloWorld())
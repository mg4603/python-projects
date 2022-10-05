from web import application

urls = (
    '/', 'index'
)

app = application(urls, globals())

class index:

    def GET(self):
        greeting = "Hello World"
        return greeting
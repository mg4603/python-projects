from web import application

urls = (
    '/', 'index'
)

app = application(urls, globals())

class index:
    pass
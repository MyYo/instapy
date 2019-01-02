import falcon
from wsgiref import simple_server

class ItemsResource(object):
    def on_get(self, req, resp):
        items = req.params.get('item')
        if type(items) is not list:
            items = list(items)
        print(items)
        resp.status = falcon.HTTP_200
        resp.body = 'hello, world!\n'

app = falcon.API()
items = ItemsResource()
app.add_route('/items', items)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
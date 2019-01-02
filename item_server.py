import falcon

class ItemsResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200 
        resp.body = 'hello, world!\n'

app = falcon.API()
items = ItemsResource()
app.add_route('/items', items)
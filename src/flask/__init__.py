# Minimal Flask stub for testing purposes
class Response:
    def __init__(self, status_code: int, data: bytes):
        self.status_code = status_code
        self.data = data
class Flask:
    def __init__(self, name: str):
        self.name = name
        self.routes = {}
        self.config = {}
    def route(self, path: str, methods=None):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
    def test_client(self):
        client = type('Client', (), {})()
        global request
        class DummyRequest:
            def __init__(self, method='GET', form=None):
                self.method = method
                self.form = form or {}
        def _call(path, method='GET', data=None):
            func = self.routes.get(path)
            if not func:
                return Response(404, b'')
            request.method = method
request.form = data or {}
            result = func()
            if isinstance(result, tuple):
                body, status = result
                return Response(status, str(body).encode())
            else:
                return Response(200, str(result).encode())
        def get(path):
            return _call(path)
        def post(path, data=None, follow_redirects=False):
            resp = _call(path, 'POST', data)
            if follow_redirects and resp.status_code in (301, 302):
                url = resp.data.decode()
                return _call(url)
            return resp
        client.get = get
        client.post = post
        return client
# helpers used by webapp
# A mutable request object that the webapp imports.
request = type('Request', (), {'method': None, 'form': {}})()

def redirect(url=None):
    return ('/', 302)

def url_for(endpoint, *args, **kwargs):
    return endpoint

def render_template(name='', **context):
    if name == 'index.html':
        epics = context.get('epics', [])
        titles = ' '.join(e.title for e in epics)
        return f"PM Buddy {titles}"
    if name == 'add_epic.html':
        return "Add Epic Form"
    if name == 'epic_detail.html':
        features = context.get('features', [])
        return f"Epic Detail {features}"
    if name == 'add_feature.html':
        return "Add Feature Form"
    if name == 'feature_detail.html':
        stories = context.get('stories', [])
        return f"Feature Detail {stories}"
    if name == 'add_story.html':
        return "Add Story Form"
    return ''
import os
import sys

root = os.path.dirname(__name__)
sys.path.insert(0, os.path.join(root, 'site-packages'))

import sae 
from sae.ext.shell import ShellMiddleware
from codefinder import app 
# application = sae.create_wsgi_app(ShellMiddleware(app))
application = sae.create_wsgi_app((app)


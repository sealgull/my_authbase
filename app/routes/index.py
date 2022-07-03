import imp

from flask_login import login_remembered, login_required
from ..base import base_blueprint

@base_blueprint.route('/')
@login_required
def index():
    pass 

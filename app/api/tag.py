import base64
from flask import Blueprint, jsonify, make_response
from ..models.db import db
from ..models.tag import Tag
from ..models.stats import Stats

bp = Blueprint(
    'api', __name__, url_prefix='/api/tag')


@bp.route('/<string:tag>', methods=['GET'])
def item(tag):
    #result = db.session.query(Tag).filter(Tag.hash == tag)
    #if ( result is None ) :
    #    return null, 404

    #stats = Stats(tag_id=1, ip='1')
    #db.session.add(stats)
    #db.session.commit()

    response = make_response(base64.b64decode("R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"))
    response.headers['Content-Type'] = 'image/gif'
    response.headers['Content-Disposition'] = 'filename=jovanepires.gif'
    return response

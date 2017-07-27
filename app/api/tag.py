import base64
import json
import uuid
from flask import Blueprint, jsonify, make_response, request
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

    stats = Stats(tag_id=1, ip=request.remote_addr, user_agent=request.user_agent.string, cookies=json.dumps(request.cookies), accept_languages=json.dumps(request.accept_languages))
    db.session.add(stats)
    db.session.commit()

    hash_str = request.cookies.get('trackapi') if 'trackapi' in request.cookies else str(uuid.uuid4())

    response = make_response(base64.b64decode("R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"))
    response.headers['Content-Type'] = 'image/gif'
    response.headers['Content-Disposition'] = 'filename=jovanepires.gif'
    response.set_cookie('trackapi',value=hash_str)
    return response

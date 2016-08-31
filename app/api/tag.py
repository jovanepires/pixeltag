from flask import Blueprint, jsonify
from ..models.db import db
from ..models.tag import Tag

bp = Blueprint(
    'api', __name__, url_prefix='/api/tag')


@bp.route('/<string:tag>', methods=['GET'])
def item(item_id):
    result = db.session.query(Tag).filter(Tag.hash == tag)
    if ( ! result ) {
        return null, 404
    }
    
    return jsonify({'result': result})

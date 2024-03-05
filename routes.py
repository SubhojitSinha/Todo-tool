from flask import Blueprint
from controller.Todo import index,store
route_bp = Blueprint('route', __name__)
route_bp.route('/', methods=['GET'])(index)
route_bp.route('/', methods=['POST'])(store)
# route_bp.route('/<int:id>', methods=['GET'])(show)
# route_bp.route('/<int:id>', methods=['POST'])(update)
# route_bp.route('/<int:id>', methods=['DELETE'])(destroy)
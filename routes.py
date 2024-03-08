from flask import Blueprint
from controller.todo_controller import index,store,show,delete

route_bp = Blueprint('route', __name__)
route_bp.route('/', methods=['GET'])(index)
route_bp.route('/', methods=['POST'])(store)
route_bp.route('/<int:id>', methods=['GET'])(show)
route_bp.route('/', methods=['DELETE'])(delete)
# route_bp.route('/<int:id>', methods=['POST'])(update)
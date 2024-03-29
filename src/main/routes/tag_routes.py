from flask import Blueprint, request, jsonify

from src.errors.error_handler import handle_error
from src.validators.tag_creator_validator import TagCreatorValidator
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tag_routes_bp = Blueprint('tag_routes', __name__)


@tag_routes_bp.route("/create_tag", methods=["POST"])
def create_tag():
    try:
        tag_creator_validator = TagCreatorValidator()
        tag_creator_validator.validate(request)

        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as exception:
        response = handle_error(exception)

    return jsonify(response.body), response.status_code

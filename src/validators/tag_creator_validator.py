from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError


class TagCreatorValidator:
    """
        Responsible for validating the request body for the tag creation endpoint.
    """

    def validate(self, request: any):
        request_validator = Validator({
            "product_code": {
                "type": "string",
                "required": True,
                "empty": False
            }
        })

        response = request_validator.validate(request.json)
        if response is False:
            raise HttpUnprocessableEntityError(request_validator.errors)

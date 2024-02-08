from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    """
        responsible for interacting with HTTP
    """
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # business logic here
        print(f"Creating tag for product code: {product_code}")

        # return http
        return HttpResponse(200, {"message": "CREATED TAG"})

from unittest.mock import patch
from test.mocks.mock_valid_response import MockResponse
from src.drivers.barcode_handler import BarcodeHandler
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.tag_creator_view import TagCreatorView


@patch.object(BarcodeHandler, "create_barcode")
def test_tag_creator_view(mock_create_barcode):
    # Arrange
    mock_value = "image_path"
    mock_create_barcode.return_value = mock_value
    mock_request = HttpRequest(body={
        "product_code": mock_value
    })

    # Act
    tag_creator_view = TagCreatorView()
    response = tag_creator_view.validate_and_create(mock_request)

    # Assert
    assert isinstance(response, HttpResponse)
    assert response.status_code == MockResponse.status_code
    assert response.body == MockResponse.body

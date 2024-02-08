from unittest.mock import patch
from test.mocks.mock_valid_response import MockResponse
from src.drivers.barcode_handler import BarcodeHandler
from src.controllers.tag_creator_controller import TagCreatorController


@patch.object(BarcodeHandler, "create_barcode")
def test_create(mock_create_barcode):
    # arrange
    mock_value = "image_path"
    mock_create_barcode.return_value = mock_value

    # act
    tag_creator_controller = TagCreatorController()
    response = tag_creator_controller.create(mock_value)

    # assert
    assert isinstance(response, dict)
    assert response == MockResponse.body

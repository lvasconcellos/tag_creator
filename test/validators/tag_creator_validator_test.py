from src.validators.tag_creator_validator import TagCreatorValidator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_tag_creator_validator():
    # Arrange
    request = MockRequest(json={"product_code": "1234"})

    # Act
    tag_creator_validator = TagCreatorValidator()
    tag_creator_validator.validate(request)

    # Assert
    assert True


def test_tag_creator_validator_with_invalid_request():
    # Arrange
    request = MockRequest(json={"product_code": 1234})

    # Act
    tag_creator_validator = TagCreatorValidator()
    try:
        tag_creator_validator.validate(request)

        # Assert
        assert False
    except HttpUnprocessableEntityError as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)

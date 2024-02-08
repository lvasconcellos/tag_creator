from src.errors.error_handler import handle_error
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def test_handle_error():
    # Arrange
    mock_error = Exception("Invalid input")

    # Act
    result = handle_error(mock_error)

    # Assert
    assert result.status_code == 500
    assert result.body == {
        "errors": [{
            "title": "Internal Server Error",
            "detail": "Invalid input"
        }]
    }


def test_handle_error_unprocessable_entity():
    # Arrange
    mock_error = HttpUnprocessableEntityError("Invalid input")

    # Act
    result = handle_error(mock_error)

    # Assert
    assert result.status_code == 422
    assert result.body == {
        "errors": [{
            "title": "UnprocessableEntity",
            "detail": "Invalid input"
        }]
    }

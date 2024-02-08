from cerberus import Validator

body = {
    "data": {
        "element1": 123.98,
        "element2": "abc",
        "element3": 123
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "element1": {
                "type": "float",
                "required": True,
                "empty": False
            },
            "element2": {
                "type": "string",
                "required": True,
                "empty": True
            },
            "element3": {
                "type": "integer",
                "required": False,
                "empty": False
            }
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print("Body is valid")

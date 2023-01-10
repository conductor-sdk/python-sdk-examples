class UserInfo:
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'email': 'str',
        'phone_number': 'str',
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'email': 'email',
        'phone_number': 'phoneNumber',
    }

    def __init__(self, name: str, id):
        self.name = name
        self.id = id
        self.email = ''
        self.phone_number = ''

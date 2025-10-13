from scheduler.utils import parse_object


class DummyClass:
    def __init__(self, property):
        self.property = property


def test_parse_object():
    dummy_object = DummyClass(property="test")

    # No parsing for attribute
    object = parse_object(dummy_object, attribute=None)
    assert isinstance(object, DummyClass)
    assert vars(object) == vars(dummy_object)

    # Parsing for attribute
    attribute = parse_object(dummy_object, attribute="property")
    assert attribute == "test"

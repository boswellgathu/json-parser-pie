import pytest
from json_parser import JsonParser


def test_json_parser_parses_empty_dictionary():
    json_string = "{}"
    json_parser = JsonParser(json_string)

    actual = json_parser.parse()

    assert isinstance(actual, dict)
    assert not actual # check it is empty


@pytest.mark.parametrize(
    "json_string",
    [
        "{'key': 'value'}",
        "{\n  \"key\": \"value\"\n}"
    ]
)
def test_json_parser_parses_key_value_dictionary(json_string):
    json_parser = JsonParser(json_string)

    actual = json_parser.parse()

    assert isinstance(actual, dict)
    assert actual['key'] == 'value'


@pytest.mark.parametrize(
    "json_string, expected_key_values",
    [
        (
            '{"key1": true, "key2": false, "key3": null, "key4": "value", "key5": 101}',
            [('key1', True), ('key2', False), ('key3', None), ('key4', 'value'), ('key5', 101)]
        ),
        (
            "{\n  \"key1\": true,\n  \"key2\": false,\n  \"key3\": null,\n  \"key4\": \"value\",\n  \"key5\": 101\n}",
            [('key1', True), ('key2', False), ('key3', None), ('key4', 'value'), ('key5', 101)]
        )
    ]
)
def test_json_parser_parses_primitive_values_unescaped_string(json_string, expected_key_values):
    json_parser = JsonParser(json_string)

    actual = json_parser.parse()

    assert isinstance(actual, dict)
    assert [(k, v) for k, v in actual.items()] == expected_key_values


def test_json_parser_parses_dicts_and_lists(json_string):
    pass


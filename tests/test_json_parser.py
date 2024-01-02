from json_parser import JsonParser


def test_json_parser_parses_empty_dictionary():
    json_string = "{}"
    json_parser = JsonParser(json_string)

    actual = json_parser.parse()

    assert isinstance(actual, dict)
    assert not actual # check it is empty


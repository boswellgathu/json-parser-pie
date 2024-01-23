import os
import subprocess

import pytest

CLI_COMMAND = 'python json_parser_cli.py'
TEST_DATA_DIR = './json_test_files'


def gen_test_from_test_files():
    test_files = []
    for filename in os.listdir(TEST_DATA_DIR):
        test_files.append(
            (filename, 0 if filename.startswith('pass') else -1)
        )
    return test_files


@pytest.mark.parametrize(
    "test_file_path, expected_return_code",
    gen_test_from_test_files()
)
def test_parser_parses_test_files(test_file_path: str, expected_return_code: int):
    command = f"python json_parser_cli.py {test_file_path}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    actual_output = output.decode().strip()

    assert process.returncode == expected_return_code


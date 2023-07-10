from datetime import date
import os
from unittest.mock import patch
from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_validation_for_file_existance(capsys):
    context = {
        "base_path": "/home/trybe/????"
    }
    expected_output = "File '????' does not exist"

    show_details(context)

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == expected_output


def test_show_details_no_extension(capsys):
    context = {
        "base_path": "/path/to/file"
    }
    expected_output = "File extension: [no extension]"

    def mock_getsize(file_path):
        return 100

    def mock_getmtime(file_path):
        return 1640995200  # Corresponds to 2022-01-01

    with patch("os.path.exists", return_value=True), \
         patch("os.path.getsize", side_effect=mock_getsize), \
         patch("os.path.getmtime", side_effect=mock_getmtime):

        show_details(context)

        captured = capsys.readouterr()
        output = captured.out.strip()

        assert expected_output in output


def test_show_details_date_time(capsys, tmp_path):
    file = tmp_path / "file.txt"
    file.touch()

    file_extension = os.path.splitext(file)[1]
    context = {"base_path": str(file)}

    show_details(context)
    captured = capsys.readouterr()

    expected = (
        f"File name: file.txt\n"
        f"File size in bytes: 0\n"
        f"File type: file\n"
        f"File extension: {file_extension}\n"
        f"Last modified date: {date.today()}\n"
    )

    assert captured.out == expected

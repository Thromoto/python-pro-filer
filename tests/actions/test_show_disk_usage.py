from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import patch, Mock


def test_show_disk_usage_empty_files(capsys):
    context = {
        "all_files": []
    }
    expected_output = "Total size: 0"

    show_disk_usage(context)

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == expected_output


def test_show_disk_usage_no_sorted_result(tmp_path, capsys):
    mock_file_path = Mock()

    file_1 = tmp_path / "file1.txt"
    file_1.touch()
    file_1.write_text("Trybe")

    file_2 = tmp_path / "file2.txt"
    file_2.touch()
    file_2.write_text("Xablaaau")

    context = {"all_files": [str(file_1), str(file_2)]}

    with patch(
        "pro_filer.cli_helpers._get_printable_file_path",
        mock_file_path,
    ):
        show_disk_usage(context)

    captured = capsys.readouterr()
    output = captured.out.strip()

    file1_index = output.index("file1.txt")
    file2_index = output.index("file2.txt")

    assert file1_index > file2_index

from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_empty(capsys):
    context = {
        "all_files": [],
        "all_dirs": []
    }
    expected_output = "Found 0 files and 0 directories"

    show_preview(context)

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == expected_output


def test_show_preview_max_files_dirs(capsys):
    context = {
        "all_files": [
            "file1.txt", "file2.txt",
            "file3.txt", "file4.txt", "file5.txt", "file6.txt"
        ],
        "all_dirs": [
            "dir1", "dir2", "dir3", "dir4", "dir5", "dir6"
        ]
    }
    expected_files = ("First 5 files: ['file1.txt', 'file2.txt', "
                      "'file3.txt', 'file4.txt', 'file5.txt']")

    expected_dirs = ("First 5 directories: ['dir1', "
                     "'dir2', 'dir3', 'dir4', 'dir5']")

    show_preview(context)

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert expected_files in output
    assert expected_dirs in output

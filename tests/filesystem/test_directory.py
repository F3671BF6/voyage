from unittest.mock import patch

from voyage.filesystem import Directory


class _MockPath:
    def __init__(self, name: str, is_file: bool):
        self.name = name
        self.is_file = is_file

    def is_dir(self):
        return not self.is_file

    def __repr__(self):
        return self.name

    def mkdir(self):
        return

    def __lt__(self, other):
        return self.name < other.name


@patch(
    "pathlib.Path.iterdir",
    lambda x: [
        _MockPath("Afile1", True),
        _MockPath("Bdir", False),
        _MockPath("Afile2", True),
        _MockPath("Cdir", False),
    ],
)
def test_list():
    directory = Directory("a")
    contents = directory.list()
    assert [str(x) for x in contents] == ["Bdir", "Cdir", "Afile1", "Afile2"]


_mkdir_calls = []


@patch("pathlib.Path.mkdir", lambda x: _mkdir_calls.append(x))
def test_make_dir():
    _mkdir_calls.clear()
    directory = Directory("a/b")
    directory.make_dir()
    assert str(_mkdir_calls[-1]).replace("\\", "/").split("/")[-1] == "b"

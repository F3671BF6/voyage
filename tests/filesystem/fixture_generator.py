from typing import List, Tuple

from voyage.filesystem.directory import Directory
from voyage.filesystem.file import File

_AbstractFile = Tuple[str, str]
_AbstractDir = Tuple[str, List["_AbstractDir" | _AbstractFile]]
_AbstractFileSystem = List[_AbstractDir | _AbstractFile]


def generate_mock_file_and_dir(root_dir: _AbstractFileSystem):
    class MockFile(File):
        def read(self):
            content = _find_in_abstract_filesystem(root_dir, self._parts)
            if not isinstance(content, str):
                raise TypeError(f"{self._path_str} is not a string in the abstract filesystem.")
            return content

    class MockDirectory(Directory):
        def list(self):
            content = _find_in_abstract_filesystem(root_dir, self._parts)
            if not isinstance(content, list):
                raise TypeError(f"{self._path_str} is not a list in the abstract filesystem.")
            content = sorted(content, key=lambda x: x[0])
            directories = []
            files = []
            for name, contents in content:
                if isinstance(contents, list):
                    directories.append(name)
                else:
                    files.append(name)
            return directories + files

    # @fixture(autouse=True)
    # def fixture_filesystem():
    #     MockFile, MockDirectory = generate_mock_file_and_dir(...)
    #     with (
    #         patch("voyage.filesystem.directory.Directory", MockDirectory),
    #         patch("voyage.filesystem.file.File", MockFile),
    #     ):
    #         yield

    return MockFile, MockDirectory


# helper functions
# ==================================================================================================


def _find_in_abstract_filesystem(
    abstract_filesystem: _AbstractFileSystem, path: Tuple[str, ...]
) -> str | List[_AbstractDir | _AbstractFile]:
    sub_dir = abstract_filesystem
    depth = 0
    for part in path:
        depth += 1
        found = False
        for element in sub_dir:
            name, contents = element
            if isinstance(contents, list):
                if isinstance(name, str) and name == part:
                    sub_dir = contents
                    found = True
                    break
            elif isinstance(contents, str):
                if isinstance(name, str) and name == part and depth == len(path):
                    return contents
            else:
                raise TypeError(f"Error in retrieving {'/'.join(path)} in the abstract filesystem.")

        if not found:
            raise FileNotFoundError(f"Did not find {part} in {'/'.join(path)}.")
    return sub_dir

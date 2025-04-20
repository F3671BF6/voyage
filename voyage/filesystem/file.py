import voyage.filesystem.base as _b


class File(_b.Path):
    """File object, allows for reading, writing, deleting"""

    def read(self) -> str:
        """Read content of file into a string

        Returns
        -------
        str
            File content
        """
        with open(self._path_str, "r") as file:
            content = file.read()
        return content

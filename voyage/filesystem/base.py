import pathlib as _p


class Path:
    """Base class for both directories and files"""

    def __init__(self, path: str | _p.Path) -> None:
        """Initialize a path object

        Parameters
        ----------
        path : str | pathlib.Path
            String or pathlib.Path object.
        """
        self._parts = _p.Path(path).parts
        self._path_str = str(_p.Path(path))

    def __repr__(self) -> str:
        """Representation depends on the system running the code"""
        return self._path_str

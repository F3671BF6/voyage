import pathlib as _p


class Path:
    """Base class for both directories and files"""

    def __init__(self, path: "str | _p.Path | Path") -> None:
        """Initialize a path object

        Parameters
        ----------
        path : voyage.filesystem.base.Path | str | pathlib.Path
            String or pathlib.Path object.
        """
        unix_path = str(path).replace("\\", "/")
        self._parts = _p.Path(unix_path).parts
        self._path_str = str(_p.Path(unix_path))

    def __repr__(self) -> str:
        """Representation depends on the system running the code"""
        return self._path_str

    def __eq__(self, value: "Path | str") -> bool:
        """Equality between paths

        Parameters
        ----------
        value : voyage.filesystem.base.Path | str
            Other path object or string

        Returns
        -------
        bool
            Equality.
        """
        return self._parts == _p.Path(str(value)).parts

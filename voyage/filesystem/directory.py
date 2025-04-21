import logging as _log
import pathlib as _p
import typing as _t

import voyage.filesystem.base as _b
import voyage.filesystem.file as _f


class Directory(_b.Path):
    """Directory object, allows for listing"""

    def list(self) -> _t.List[_b.Path]:
        """List elements of the directory

        Returns
        -------
        List[voyage.filesystem.base.Path]
            List of elements, alphabetically sorted, directories coming before files.
        """
        path = _p.Path(*self._parts)
        items = sorted(list(path.iterdir()))
        directories = []
        files = []
        for item in items:
            if item.is_dir():
                directories.append(Directory(item))
            else:
                files.append(_f.File(item))
        return directories + files

    def make_dir(self) -> bool:
        """Create directory at this path

        Returns
        -------
        bool
            Whether the operation was successful.
        """
        path = _p.Path(self._path_str)
        try:
            path.mkdir()
            return True
        except Exception as exc:
            _LOGGER.warning(exc)
            return False

    def __truediv__(self, item: str) -> _b.Path:
        """Append a directory/file to self

        Parameters
        ----------
        item : str
            Directory/file to concatenate.

        Returns
        -------
        voyage.filesystem.base.Path
            Path to the directory/file.
        """
        return _b.Path(_p.Path(str(self)) / item)


_LOGGER = _log.getLogger(__name__)

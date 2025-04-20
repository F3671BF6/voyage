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
        List[Path]
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


def run():
    pass

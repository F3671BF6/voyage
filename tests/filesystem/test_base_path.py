from pathlib import Path as pathlibPath

from voyage.filesystem.base import Path


def test_path_init():
    _ = Path("a/b/c/")
    _ = Path("a\\b\\c\\")
    _ = Path(pathlibPath("a/b/c"))
    _ = Path(Path("a/b/c"))


def test_equality():
    pathA = Path("a/b/c/")
    pathB = Path("a\\b\\c\\")
    pathC = Path(pathlibPath("a/b/c"))
    pathD = Path(Path("a/b/c"))
    wrong_path = Path("a")
    strA = "a/b/c"
    strB = "a/b/c"
    strC = "a/b/c"
    wrong_str = "a/"

    assert pathA == pathA
    assert pathA == pathB
    assert pathA == pathC
    assert pathA == pathD
    assert pathA == strA
    assert pathA == strB
    assert pathA == strC

    assert pathA != wrong_path
    assert pathA != wrong_str

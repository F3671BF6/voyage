from unittest.mock import patch

from pytest import fixture, raises

from tests.filesystem.fixture_generator import generate_mock_file_and_dir
from voyage.notes.vault import Vault


@fixture(autouse=True)
def fixture_filesystem():
    MockFile, MockDirectory = generate_mock_file_and_dir(
        [
            (
                "vaults",
                [
                    (
                        "valid_vault",
                        [
                            ("notes", []),
                            ("attachments", []),
                            ("data", []),
                        ],
                    ),
                    (
                        "incomplete",
                        [
                            ("attachments", []),
                            ("data", []),
                        ],
                    ),
                ],
            )
        ]
    )

    with (
        patch("voyage.filesystem.Directory", MockDirectory),
        patch("voyage.filesystem.File", MockFile),
    ):
        yield


def test_open_valid_vault():
    _ = Vault("vaults/valid_vault")


def test_open_non_existing_vault():
    with raises(ValueError):
        _ = Vault("vaults/does_not_exist")


def test_open_incomplete_vault():
    with raises(ValueError):
        _ = Vault("vaults/incomplete")


def test_create_valid_vault():
    _ = Vault.create("vaults", "new_vault")
    _ = Vault("vaults/new_vault")

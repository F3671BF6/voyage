import enum as _e

import voyage.filesystem as _fs


class Vault:
    """A vault contains everything needed to fully render the notes"""

    def __init__(self, location: _fs.Directory | str) -> None:
        """Open a location with the correct directory structure for a vault

        Parameters
        ----------
        location : voyage.filesystem.Directory | str
            Root location of the vault.

        Raises
        ------
        ValueError
            If the vault does not have a valid directory structure.
        """
        self.location = _fs.Directory(location)
        self.__component_to_location = {
            component: _fs.Directory(self.location / component.value) for component in Components
        }
        self._validate()

    @classmethod
    def create(cls, vault_location: _fs.Directory | str, vault_name: str) -> "Vault":
        """Create a new vault in a directory

        Parameters
        ----------
        vault_location : voyage.filesystem.Directory | str
            Location in which to place the vault.
        vault_name : str
            Name of the vault, will also be the directory name inside `vault_location`.

        Returns
        -------
        Vault
            Created vault.

        Raises
        ------
        OSError
            If failed to create a directory.
        """
        root_dir = _fs.Directory(_fs.Directory(vault_location) / vault_name)
        _create_dir(root_dir)
        for sub_dir in Components:
            _create_dir(_fs.Directory(root_dir / sub_dir.value))
        return cls(root_dir)

    def _validate(self) -> None:
        """Check that all directories were successfully created

        Raises
        ------
        ValueError
            If not all directories are present.
        """
        for component in Components:
            try:
                directory = self.__component_to_location[component]
                _ = directory.list()
            except Exception as exc:
                raise ValueError(
                    f"{self.location} is not a valid vault, raised "
                    f"{type(exc)} for {component.value}."
                )


class Components(_e.Enum):
    """Components required to make a vault"""

    NOTES = "notes"
    ATTACHMENTS = "attachments"
    DATA = "data"


def _create_dir(directory: _fs.Directory) -> None:
    """Create a directory and raise failures

    Parameters
    ----------
    directory : voyage.filesystem.Directory
        Directory to create.

    Raises
    ------
    OSError
        If unable to create the directory.
    """
    success = directory.make_dir()
    if not success:
        raise OSError(f"Unable to create {directory}.")

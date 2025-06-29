import pandas as _pd

import voyage.core.typing as _b


class DateTime(_b.DateTime):
    """DateTime object to store all representations in a single object"""

    def __init__(self, value: _b.IntoDateTime) -> None:
        """Convert any Python datetime representation to the same format

        Parameters
        ----------
        value : IntoDateTime
            Anything that can be parsed as a datetime
        """
        if isinstance(value, _b.DateTime):
            value = value._timestamp
        else:
            value = _pd.Timestamp(value)

        self._timestamp = value

    def __eq__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp == value._timestamp

    def __ne__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp != value._timestamp

    def __le__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp <= value._timestamp

    def __lt__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp < value._timestamp

    def __ge__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp >= value._timestamp

    def __gt__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp > value._timestamp

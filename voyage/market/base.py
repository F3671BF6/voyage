import abc as _abc
import enum as _e
import typing as _t

import polars as _pl

import voyage.core.time as _vt


class Field(_e.Enum):
    BID = "BID"
    ASK = "ASK"
    LAST = "LAST"
    DATE = "DATE"
    INSTRUMENT = "INSTRUMENT"


class MarketObject(_abc.ABC):
    _name: str

    def __repr__(self) -> str:
        return f"<{self._name}>"

    def __eq__(self, other: "MarketObject") -> bool:
        return self._name == other._name


class Currency(MarketObject):
    def __init__(self, name: str) -> None:
        self._name = name


class Instrument(MarketObject): ...


class Market(MarketObject):
    def get(
        self,
        instrument: Instrument | _t.Sequence[Instrument],
        field: Field | _t.Sequence[Field],
        datetime: _vt.IntoDateTime | _t.Sequence[_vt.IntoDateTime] | _vt.DateTimeRange,
    ) -> _pl.DataFrame:
        # all to lists
        if isinstance(instrument, Instrument):
            instrument = [instrument]
        if isinstance(field, Field):
            field = [field]
        if isinstance(datetime, _vt.DateTimeRange):
            datetime = datetime.to_sequence()
        elif isinstance(datetime, _vt.IntoDateTime):
            datetime = [_vt.DateTime(datetime)]
        else:
            datetime = [_vt.DateTime(x) for x in datetime]

        if len(instrument) == 1:
            return self._get_single_instrument(instrument[0], field, datetime)
        if len(field) == 1:
            return self._get_single_field(field[0], instrument, datetime)
        if len(datetime) == 1:
            return self._get_single_date(datetime[0], instrument, field)
        raise ValueError(
            f"Passed {len(instrument)} instruments, {len(field)} fields, "
            f"and {len(datetime)} datetimes."
        )

    @_abc.abstractmethod
    def _get_single_instrument(
        self,
        instrument: Instrument,
        fields: _t.Sequence[Field],
        datetimes: _t.Sequence[_vt.DateTime],
    ) -> _pl.DataFrame: ...

    @_abc.abstractmethod
    def _get_single_field(
        self,
        field: Field,
        instruments: _t.Sequence[Instrument],
        datetimes: _t.Sequence[_vt.DateTime],
    ) -> _pl.DataFrame: ...

    @_abc.abstractmethod
    def _get_single_date(
        self,
        datetime: _vt.DateTime,
        instruments: _t.Sequence[Instrument],
        fields: _t.Sequence[Field],
    ) -> _pl.DataFrame: ...

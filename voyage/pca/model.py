import typing as _t

import polars as _pl


class PCA:
    def __init__(self, X: _pl.DataFrame) -> None:
        """Initialize the PCA instance

        Parameters
        ----------
        X : _pl.DataFrame
            DataFrame with the `DATE` column containing the index of the observations, and the other
            columns representing the original variables.
        """

        self.X = X

    def compute_factors(self, weight_function: _t.Callable | None = None) -> _pl.DataFrame: ...

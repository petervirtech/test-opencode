"""Shared helpers for pm_buddy tests."""

import tempfile
from pathlib import Path


class TempDB:
    """A temp-file SQLite database path, isolated per instance.

    Tests cannot use ``Path(":memory:")`` because the service opens a new
    connection per operation and each ``:memory:`` connection is private;
    a temp file gives the same isolation without side effects.
    """

    def __init__(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name) / "test.db"

    def close(self):
        self._tmp.cleanup()

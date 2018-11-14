from ._base import DataSource
from .apt import AptSource
from .travis import TravisSource
from .pip import PipSource
from .python import PythonSource
from .operating_system import OperatingSystemSource
from .git import GitSource

__all__ = [
    "DataSource",
    "AptSource",
    "TravisSource",
    "PipSource",
    "PythonSource",
    "OperatingSystemSource",
    "GitSource",
]


from enum import Enum


class Accessor(Enum):
    """Accessor types

    Define the accessor symbols used in PlantUML.
    For more details, see the documentation.

    """

    Public = "+"
    Protected = "#"
    Private = "-"

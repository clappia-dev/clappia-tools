from enum import Enum

class FilterOperator(Enum):
    CONTAINS = "CONTAINS"
    NOT_IN = "NOT_IN"
    EQ = "EQ"
    NEQ = "NEQ"
    EMPTY = "EMPTY"
    NON_EMPTY = "NON_EMPTY"
    STARTS_WITH = "STARTS_WITH"
    BETWEEN = "BETWEEN"
    GT = "GT"
    LT = "LT"
    GTE = "GTE"
    LTE = "LTE"


class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"


class FilterKeyType(Enum):
    STANDARD = "STANDARD"
    CUSTOM = "CUSTOM"


class AggregationType(Enum):
    COUNT = "count"
    SUM = "sum"
    AVERAGE = "average"
    MINIMUM = "minimum"
    MAXIMUM = "maximum"
    UNIQUE = "unique"


class DimensionType(Enum):
    STANDARD = "STANDARD"
    CUSTOM = "CUSTOM"


class SortDirection(Enum):
    ASC = "asc"
    DESC = "desc"
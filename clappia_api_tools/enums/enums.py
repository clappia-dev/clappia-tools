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


class FieldType(Enum):
    SINGLE_LINE_TEXT = "singleLineText"
    MULTI_LINE_TEXT = "multiLineText"
    SINGLE_SELECTOR = "singleSelector"
    MULTI_SELECTOR = "multiSelector"
    DROP_DOWN = "dropDown"
    DATE_SELECTOR = "dateSelector"
    TIME_SELECTOR = "timeSelector"
    PHONE_NUMBER = "phoneNumber"
    UNIQUE_NUMBERING = "uniqueNumbering"
    FILE = "file"
    GPS_LOCATION = "gpsLocation"
    HTML = "html"
    CALCULATIONS_AND_LOGIC = "calculationsAndLogic"
    CODE_SCANNER = "codeScanner"
    COUNTER = "counter"
    SLIDER = "slider"
    SIGNATURE = "signature"
    VALIDATION = "validation"
    LIVE_TRACKING = "liveTracking"
    NFC_READER = "nfcReader"
    ADDRESS = "address"


class ImageQuality(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class AllowedFileTypes(Enum):
    IMAGES_CAMERA_UPLOAD = "images_camera_upload"
    IMAGES_GALLERY_UPLOAD = "images_gallery_upload"
    VIDEOS = "videos"
    DOCUMENTS = "documents"


class ChipType(Enum):
    STANDARD = "standard"
    CHIPS = "chips"


class ValidationType(Enum):
    NONE = "none"
    NUMBER = "number"
    EMAIL = "email"
    URL = "url"
    CUSTOM = "custom"


class ExcelFormat(Enum):
    EXCEL = "excel"
    CSV = "csv"


class TriggerType(Enum):
    SUBMISSION_CREATED = "newSubmission"
    SUBMISSION_EDITED = "editSubmission"
    SUBMISSION_STATUS_EDITED = "reviewSubmission"


class NodeType(Enum):
    EMAIL = "email"
    WAIT = "wait"
    CONDITION = "condition"
    SMS = "sms"
    LOOP = "loop"
    MOBILE_NOTIFICATION = "mobileNotification"
    WHATSAPP = "whatsApp"
    SLACK = "slack"
    EDIT_SUBMISSION = "editSubmission"
    DELETE_SUBMISSION = "deleteSubmission"
    REST_API = "restApi"
    DATABASE = "database"
    CREATE_SUBMISSION = "createSubmission"
    APPROVAL = "approval"
    FIND_SUBMISSION = "findSubmission"
    AI = "ai"
    CODE = "code"
    PASS = "pass"
    SYNC = "sync"
    MSTEAMS = "msteams"


class ChartType(Enum):
    PIE_CHART = "pieChart"
    BAR_CHART = "barGraph"
    LINE_CHART = "lineChart"
    DOUGHNUT_CHART = "doughnutChart"
    DATA_TABLE = "dataTable"
    SUMMARY_CARD = "summary"
    MAP_CHART = "maps"
    GANTT_CHART = "gantt"


class WorkplaceUserRole(Enum):
    ADMIN = "Workplace Manager"
    DEVELOPER = "App Builder"
    USER = "User"


class AppUserRole(Enum):
    ADMIN = "Admin"
    DEVELOPER = "Developer"
    USER = "User"

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
    # Data Input Blocks
    SINGLE_LINE_TEXT = "singleLineText"
    MULTI_LINE_TEXT = "multiLineText"
    RICH_TEXT_EDITOR = "richTextEditor"
    NUMBER_INPUT = "numberInput"
    URL_INPUT = "urlInput"
    EMAIL_INPUT = "emailInput"
    DROP_DOWN = "dropDown"
    SINGLE_SELECTOR = "singleSelector"
    MULTI_SELECTOR = "multiSelector"
    TAGS = "tags"
    DATE_SELECTOR = "dateSelector"
    TIME_SELECTOR = "timeSelector"
    CODE_SCANNER = "codeScanner"
    NFC_READER = "nfcReader"
    RATINGS = "ratings"
    TOGGLE = "toggle"
    RANGE = "range"
    COUNTER = "counter"
    SLIDER = "slider"
    PHONE_NUMBER = "phoneNumber"
    ADDRESS = "address"
    GEO_ADDRESS = "geoAddress"
    PAYMENT_GATEWAY = "paymentGateway"
    
    # Data Upload Blocks
    FILE = "file"  # Camera, Image & Files
    AUDIO = "audio"
    GPS_LOCATION = "gpsLocation"
    LIVE_TRACKING = "liveTracking"
    SIGNATURE = "signature"
    
    # Data Processing Blocks
    CALCULATIONS_AND_LOGIC = "calculationsAndLogic"
    UNIQUE_NUMBERING = "uniqueNumbering"
    GET_DATA_FROM_OTHER_APPS = "getDataFromOtherApps"
    GET_DATA_FROM_REST_APIS = "getDataFromRestApis"
    GET_DATA_FROM_DATABASE = "getDataFromDatabase"
    AI = "ai"
    
    # Content Blocks
    HTML = "html"  # Text, HTML & Embedding
    ATTACHED_FILES = "attachedFiles"
    IMAGE_VIEWER = "imageViewer"
    VIDEO_VIEWER = "videoViewer"
    PDF_VIEWER = "pdfViewer"
    PROGRESS_BAR = "progressBar"
    VALIDATION = "validation"
    BUTTON = "button"
    CODE = "code"
    
    # Additional field types
    DATABASE = "database"


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
    STANDARD = "Standard"
    CHIPS = "Chips"


class ValidationType(Enum):
    NONE = "none"
    NUMBER = "number"
    EMAIL = "email"
    URL = "url"
    CUSTOM = "custom"


class DatabaseType(Enum):
    MYSQL = "MySql"
    POSTGRESQL = "PostgreSql"
    AZURE_SQL = "AzureSql"

class WatermarkPosition(Enum):
    TOP_RIGHT = "TR"
    BOTTOM_RIGHT = "BR"
    BOTTOM_LEFT = "BL"
    TOP_LEFT = "TL"


class ExcelFormat(Enum):
    EXCEL = "excel"
    CSV = "csv"


class TriggerType(Enum):
    SUBMISSION_CREATED = "newSubmission"
    SUBMISSION_EDITED = "editSubmission"
    SUBMISSION_STATUS_EDITED = "reviewSubmission"


class NodeType(Enum):
    """Enumeration of supported workflow node types"""
    EMAIL_NODE = 'email'
    WAIT_NODE = 'wait'
    CONDITION_NODE = 'condition'    
    SMS_NODE = 'sms'
    LOOP_NODE = 'loop'
    MOBILE_NOTIFICATION_NODE = 'mobileNotification'
    WHATSAPP_NODE = 'whatsApp'
    SLACK_NODE = 'slack'
    EDIT_SUBMISSION_NODE = 'editSubmission'
    DELETE_SUBMISSION_NODE = 'deleteSubmission'     
    REST_API_NODE = 'restApi'   
    DATABASE_NODE = 'database'  
    CREATE_SUBMISSION_NODE = 'createSubmission' 
    APPROVAL_NODE = 'approval'  
    FIND_SUBMISSION_NODE = 'findSubmission'
    AI_NODE = 'ai'
    CODE_NODE = 'code'

class ChartType(Enum):
    PIE_CHART = "pieChart"
    BAR_CHART = "barGraph"
    LINE_CHART = "lineChart"
    DOUGHNUT_CHART = "doughnutChart"
    DATA_TABLE = "dataTable"
    SUMMARY_CARD = "summary"
    MAP_CHART = "maps"
    GANTT_CHART = "gantt"


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


class SectionType(Enum):
    SECTION = "Section"
    TABLE = "Table"
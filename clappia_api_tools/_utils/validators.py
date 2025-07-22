import re
from typing import Tuple, List
from clappia_api_tools._models.model import Section
from clappia_api_tools._enums.enums import FilterOperator, FilterKeyType, LogicalOperator, AggregationType, DimensionType

class ClappiaInputValidator:
    """Validates user inputs like app IDs, emails, etc."""

    EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    APP_ID_PATTERN = r"^[A-Z0-9]+$"
    SUBMISSION_ID_PATTERN = r"^[A-Z0-9]+$"
    
    STANDARD_FIELDS = {
        "$submissionId",
        "$owner",
        "$status",
        "$lastUpdatedAt",
        "$lastModifiedAt",
        "$createdAt",
        "$updatedAt",
        "$state",
    }

    @staticmethod
    def validate_app_name(app_name: str) -> Tuple[bool, str]:
        if not app_name or not app_name.strip():
            return False, "App name is required and cannot be empty"
        if len(app_name.strip()) < 3:
            return False, "App name must be at least 3 characters long"
        return True, ""

    @staticmethod
    def validate_email(email: str) -> bool:
        if not email or not email.strip():
            return False
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_pattern, email.strip()):
            return False
        return True

    @staticmethod
    def validate_app_structure(sections: List[Section]) -> Tuple[bool, str]:
        create_app_field_types = [
            "singleLineText",
            "multiLineText",
            "singleSelector",
            "multiSelector",
            "dropDown",
            "dateSelector",
            "timeSelector",
            "phoneNumber"  
        ]
        options_field_types = [
            "singleSelector",
            "multiSelector",
            "dropDown"
        ]
        
        if not sections or not isinstance(sections, list):
            return False, "Sections must be a non-empty list"
        for section in sections:
            if not section.sectionName or not section.sectionName.strip():
                return False, "Section name is required and cannot be empty"
            if not section.fields or not isinstance(section.fields, list):
                return False, f"Section '{section.sectionName}' must have a non-empty list of fields with fieldType, label and options (optional) as keys and fieldType must be one of {create_app_field_types} and options must be a list of strings if fieldType is one of {options_field_types}"
            for field in section.fields:
                if field.fieldType not in create_app_field_types:
                    return False, f"Invalid field type '{field.fieldType}' in section '{section.sectionName}, allowed field types are {create_app_field_types}"
                if not field.label or not field.label.strip():
                    return False, f"Field label is required in section '{section.sectionName}'"
        return True, ""

    @staticmethod
    def validate_email_list(email_ids: List[str]) -> Tuple[bool, str, List[str]]:
        """Validate a list of email addresses and return valid ones"""
        if not isinstance(email_ids, list):
            return False, "email_ids must be a list", []

        if not email_ids:
            return False, "email_ids cannot be empty", []

        valid_emails = []
        invalid_emails = []

        for email in email_ids:
            if not isinstance(email, str):
                invalid_emails.append(str(email))
                continue

            if ClappiaInputValidator.validate_email(email.strip()):
                valid_emails.append(email.strip())
            else:
                invalid_emails.append(email)

        if not valid_emails:
            return (
                False,
                f"No valid email addresses found. Invalid emails: {invalid_emails}",
                [],
            )

        if invalid_emails:
            return (
                True,
                f"Some emails were invalid and skipped: {invalid_emails}",
                valid_emails,
            )

        return True, "", valid_emails

    @staticmethod
    def validate_app_id(app_id: str) -> Tuple[bool, str]:
        """Validate Clappia app ID format"""
        if not app_id or not isinstance(app_id, str) or not app_id.strip():
            return False, "App ID is required and cannot be empty"

        if not re.match(ClappiaInputValidator.APP_ID_PATTERN, app_id.strip()):
            return False, "App ID must contain only uppercase letters and numbers"

        return True, ""

    @staticmethod
    def validate_submission_id(submission_id: str) -> Tuple[bool, str]:
        """Validate Clappia submission ID format"""
        if (
            not submission_id
            or not isinstance(submission_id, str)
            or not submission_id.strip()
        ):
            return False, "Submission ID is required and cannot be empty"

        if not re.match(
            ClappiaInputValidator.SUBMISSION_ID_PATTERN, submission_id.strip()
        ):
            return (
                False,
                "Submission ID must contain only uppercase letters and numbers",
            )

        return True, ""

    @staticmethod
    def validate_condition(condition: dict) -> Tuple[bool, str]:
        """Validate a filter condition"""
        required_fields = ["operator", "filterKeyType", "key", "value"]
        for field in required_fields:
            if field not in condition:
                return False, f"Condition missing required field: {field}"

        operator = condition["operator"]
        if operator not in [op.value for op in FilterOperator]:
            return False, f"Invalid operator: {operator}"

        if condition["filterKeyType"] not in [fkt.value for fkt in FilterKeyType]:
            return False, f"Invalid filterKeyType: {condition['filterKeyType']}"

        key = condition["key"]
        if len(key.strip()) == 0:
            return False, "Key must be a non-empty string"

        if (
            condition["filterKeyType"] == FilterKeyType.STANDARD.value
            and key not in ClappiaInputValidator.STANDARD_FIELDS
        ):
            return (
                False,
                f"Standard filterKeyType used but key '{key}' is not a standard field",
            )

        operator = condition["operator"]
        value = condition["value"]

        if operator in [FilterOperator.EMPTY.value, FilterOperator.NON_EMPTY.value]:
            if value and value.strip():
                return False, f"Operator {operator} should have empty value"
        else:
            if len(value.strip()) == 0:
                return False, f"Operator {operator} requires a non-empty value"

        return True, ""

    @staticmethod
    def validate_filters(filters: dict) -> Tuple[bool, str]:
        """Validate filter structure"""
        if "queries" not in filters:
            return False, "Filters must contain 'queries' key"

        queries = filters["queries"]
        if len(queries) == 0:
            return False, "Queries must be a non-empty list"

        for query_group in queries:
            if "queries" not in query_group:
                return False, "Each query group must contain 'queries' key"

            inner_queries = query_group["queries"]
            for inner_query in inner_queries:
                if "conditions" not in inner_query:
                    return False, "Each query must contain 'conditions'"

                conditions = inner_query["conditions"]
                if len(conditions) == 0:
                    return False, "Conditions must be a non-empty list"

                for condition in conditions:
                    is_valid, error_msg = ClappiaInputValidator.validate_condition(condition)
                    if not is_valid:
                        return False, error_msg

                if "operator" in inner_query:
                    logical_op = inner_query["operator"]
                    if logical_op not in [op.value for op in LogicalOperator]:
                        return False, f"Invalid logical operator: {logical_op}"

        return True, ""

    @staticmethod
    def validate_aggregation_type(agg_type: str) -> bool:
        """Validate aggregation type"""
        return agg_type in [at.value for at in AggregationType]

    @staticmethod
    def validate_dimension_type(dim_type: str) -> bool:
        """Validate dimension type"""
        return dim_type in [dt.value for dt in DimensionType]

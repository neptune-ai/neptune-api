from enum import Enum


class DependencyOnInaccessibleProjectsErrorDTOErrorType(str, Enum):
    ACCESS_DENIED = "ACCESS_DENIED"
    ATTEMPTED_CHANGE_OF_A_VERSION_AUTHOR = "ATTEMPTED_CHANGE_OF_A_VERSION_AUTHOR"
    ATTEMPTED_CONVERSION_FROM_PUBLISHED_VERSION_TO_DRAFT = "ATTEMPTED_CONVERSION_FROM_PUBLISHED_VERSION_TO_DRAFT"
    ATTEMPTED_DELETION_OF_PUBLISHED_VERSION = "ATTEMPTED_DELETION_OF_PUBLISHED_VERSION"
    ATTRIBUTES_CONTAINER_NOT_FOUND = "ATTRIBUTES_CONTAINER_NOT_FOUND"
    ATTRIBUTES_PER_EXPERIMENT_LIMIT_EXCEEDED = "ATTRIBUTES_PER_EXPERIMENT_LIMIT_EXCEEDED"
    ATTRIBUTE_PATH_NOT_FOUND = "ATTRIBUTE_PATH_NOT_FOUND"
    AUTHORIZATION_TOKEN_EXPIRED = "AUTHORIZATION_TOKEN_EXPIRED"
    BAD_REQUEST = "BAD_REQUEST"
    CANNOT_DELETE_LAST_CHECKPOINT = "CANNOT_DELETE_LAST_CHECKPOINT"
    CHANNEL_ALREADY_EXISTS = "CHANNEL_ALREADY_EXISTS"
    CHANNEL_NOT_FOUND = "CHANNEL_NOT_FOUND"
    CHECKPOINT_NOT_FOUND = "CHECKPOINT_NOT_FOUND"
    CONFLICT = "CONFLICT"
    DASHBOARD_NOT_FOUND = "DASHBOARD_NOT_FOUND"
    DEPENDENCY_ON_INACCESSIBLE_PROJECTS = "DEPENDENCY_ON_INACCESSIBLE_PROJECTS"
    DOWNLOAD_REQUEST_NOT_FOUND = "DOWNLOAD_REQUEST_NOT_FOUND"
    DRAFT_ALREADY_EXISTS = "DRAFT_ALREADY_EXISTS"
    ES_ENTITY_CONTENT_TOO_LONG = "ES_ENTITY_CONTENT_TOO_LONG"
    EXPERIMENT_ALREADY_EXISTS = "EXPERIMENT_ALREADY_EXISTS"
    EXPERIMENT_NOT_FOUND = "EXPERIMENT_NOT_FOUND"
    FILE_NOT_FOUND = "FILE_NOT_FOUND"
    INCORRECT_IDENTIFIER = "INCORRECT_IDENTIFIER"
    INGEST_SUSPENDED = "INGEST_SUSPENDED"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    INVALID_ATTRIBUTE_TYPE = "INVALID_ATTRIBUTE_TYPE"
    INVALID_GROUPING_PARAMS = "INVALID_GROUPING_PARAMS"
    INVALID_OFFSET = "INVALID_OFFSET"
    INVALID_SORT_PARAMS = "INVALID_SORT_PARAMS"
    LEADERBOARD_ENTRY_NOT_FOUND = "LEADERBOARD_ENTRY_NOT_FOUND"
    MALFORMED_JSON_REQUEST = "MALFORMED_JSON_REQUEST"
    NOTEBOOK_NOT_FOUND = "NOTEBOOK_NOT_FOUND"
    ORGANIZATION_NOT_FOUND = "ORGANIZATION_NOT_FOUND"
    PROJECT_LIMITS_EXCEEDED = "PROJECT_LIMITS_EXCEEDED"
    PROJECT_NOT_FOUND = "PROJECT_NOT_FOUND"
    PROJECT_NOT_READY = "PROJECT_NOT_READY"
    REPORT_DRAFT_NOT_FOUND = "REPORT_DRAFT_NOT_FOUND"
    REPORT_NOT_FOUND = "REPORT_NOT_FOUND"
    REPORT_PUBLISHING_CONFLICT = "REPORT_PUBLISHING_CONFLICT"
    REPORT_VERSION_NOT_FOUND = "REPORT_VERSION_NOT_FOUND"
    REPORT_VERSION_OWNER_MISMATCH = "REPORT_VERSION_OWNER_MISMATCH"
    REPORT_WITH_NO_VERSIONS = "REPORT_WITH_NO_VERSIONS"
    REQUEST_TIMEOUT = "REQUEST_TIMEOUT"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    TOO_MANY_OPERATIONS = "TOO_MANY_OPERATIONS"
    TOO_MANY_REQUESTS_PER_USER = "TOO_MANY_REQUESTS_PER_USER"
    UNAUTHORIZED = "UNAUTHORIZED"
    VERSION_BRANCH_NOT_FOUND = "VERSION_BRANCH_NOT_FOUND"
    VIEW_NOT_FOUND = "VIEW_NOT_FOUND"
    WORKSPACE_IN_READ_ONLY_MODE = "WORKSPACE_IN_READ_ONLY_MODE"
    WRITE_ACCESS_DENIED_TO_ARCHIVED_PROJECT = "WRITE_ACCESS_DENIED_TO_ARCHIVED_PROJECT"

    def __str__(self) -> str:
        return str(self.value)
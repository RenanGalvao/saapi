from enum import IntEnum
from typing import TypedDict, Optional, List, Dict, Any


class Extensions(TypedDict):
    code: int
    message: str


class SaAPIErrorCode(IntEnum):
    SYSTEM_ERROR = 10_000
    REQUEST_PARSING_ERROR = 10_010
    IDENTITY_AUTHENTICATION_ERROR = 10_020
    TRIGGER_TRAFFIC_LIMITING = 10_030
    ACCESS_DENY = 10_031
    INVALID_AFFILIATE_ID = 10_032
    ACCOUNT_IS_FROZEN = 10_033
    AFFILIATE_ID_BLACK_LIST = 10_034
    UNAUTHORIZED_ERROR = 10_035
    BUSINESS_PROCESSING_ERROR = 11_000
    PARAMS_ERROR = 11_001
    BIND_ACCOUNT_ERROR = 11_002


class SaAPIError(BaseException):
    def __init__(
        self,
        message: str,
        extensions: Extensions,
        locations: Optional[List[Dict[str, Any]]] = None
    ):
        super().__init__(message)
        self.message = message
        self.locations = locations
        self.extensions = {
            "code": SaAPIErrorCode(extensions["code"]),
            "message": extensions["message"]
        }

from enum import StrEnum
from typing import TypedDict, NotRequired
from ..query_base import QueryBase
from ..authentication import Authentication


class ReportPageInfoResParams(StrEnum):
    limit = "limit"
    hasNextPage = "hasNextPage"
    scrollId = "scrollId"


class ReportNode(StrEnum):
    purchaseTime = "purchaseTime"
    clickTime = "clickTime"
    conversionId = "conversionId"
    shopeeCommission_capped = "shopeeCommissionCapped"
    sellerCommission = "sellerCommission"
    totalCommission = "totalCommission"
    buyerType = "buyerType"
    utmContent = "utmContent"
    device = "device"
    referrer = "referrer"
    orders = "orders"
    linkedMcnName = "linkedMcnName"
    mcnContractId = "mcnContractId"
    mcnManagementFeeRate = "mcnManagementFeeRate"
    mcnManagementFee = "mcnManagementFee"
    netCommission = "netCommission"
    campaignType = "campaignType"


class ReportQueryParamsBase(TypedDict):
    limit: NotRequired[int]
    scrollId: NotRequired[str]


class ReportQueryBase(QueryBase):
    def __init__(self, url: str, auth: Authentication):
        super().__init__(url, auth)

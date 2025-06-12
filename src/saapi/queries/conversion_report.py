from enum import StrEnum
from typing import TypedDict, Required, NotRequired, List
from .report_query_base import ReportQueryBase, ReportQueryParamsBase, \
    ReportNode as ConversionReportNode
from ..query_base import PageInfoResParams
from ..authentication import Authentication


class ConversionReportShopType(StrEnum):
    ALL = "ALL"
    SHOPEE_MALL_CB = "SHOPEE_MALL_CB"
    SHOPEE_MALL_NON_CB = "SHOPEE_MALL_NON_CB"
    C2C_CB = "C2C_CB"
    C2C_NON_CB = "C2C_NON_CB"
    PREFERRED_CB = "PREFERRED_CB"
    PREFERRED_NON_CB = "PREFERRED_NON_CB"


class ConversionReportOrderStatus(StrEnum):
    ALL = "ALL"
    UNPAID = "UNPAID"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class ConversionReportBuyerType(StrEnum):
    ALL = "ALL"
    NEW = "NEW"
    EXISTING = "EXISTING"


class ConversionReportAttributionType(StrEnum):
    ORDER_IN_SAME_SHOP = "Ordered in Same Shop"
    ORDER_IN_DIFFERENT_SHOP = "Ordered in Different Shop"


class ConversionReportDevice(StrEnum):
    ALL = "ALL"
    APP = "APP"
    WEB = "WEB"


class ConversionReportFraudStatus(StrEnum):
    ALL = "ALL"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    FRAUD = "FRAUD"


class ConversionReportCampaignType(StrEnum):
    ALL = "ALL"
    SELLER_OPEN_CAMPAIGN = "Seller Open Campaign"
    SELLER_TARGET_CAMPAIGN = "Seller Target Campaign"
    MCN_CAMPAIGN = "MCN Campaign"
    NON_SELLER_CAMPAIGN = "Non-Seller Campaign"


class ConversionReportQueryParams(ReportQueryParamsBase):
    purchaseTimeStart: NotRequired[int]
    purchaseTimeEnd: NotRequired[int]
    completeTimeStart: NotRequired[int]
    completeTimeEnd: NotRequired[int]
    shopName: NotRequired[str]
    shopId: NotRequired[int]
    shopType: NotRequired[List[str]]
    conversionId: NotRequired[int]
    orderId: NotRequired[str]
    productName: NotRequired[str]
    productId: NotRequired[int]
    categoryLv1Id: NotRequired[int]
    categoryLv2Id: NotRequired[int]
    categoryLv3Id: NotRequired[int]
    orderStatus: NotRequired[str]
    buyerType: NotRequired[str]
    attributionType: NotRequired[str]
    device: NotRequired[str]
    fraudStatus: NotRequired[str]
    campaignPartnerName: NotRequired[str]
    campaignType: NotRequired[str]


class ConversionReportResParams(TypedDict):
    nodes: Required[List[ConversionReportNode | str]]
    pageInfo: NotRequired[List[PageInfoResParams | str]]


class ConversionReport(ReportQueryBase):
    query_name = "conversionReport"

    query_params = {
        "purchaseTimeStart": None,
        "purchaseTimeEnd": None,
        "completeTimeStart": None,
        "completeTimeEnd": None,
        "shopName": None,
        "shopId": None,
        "shopType": None,
        "conversionId": None,
        "orderId": None,
        "productName": None,
        "productId": None,
        "categoryLv1Id": None,
        "categoryLv2Id": None,
        "categoryLv3Id": None,
        "orderStatus": ConversionReportOrderStatus.ALL,
        "buyerType": ConversionReportBuyerType.ALL,
        "attributionType": None,
        "device": ConversionReportDevice.ALL,
        "limit": 20,
        "fraudStatus": None,
        "scrollId": None,
        "campaignPartnerName": None,
        "campaignType": ConversionReportCampaignType.ALL
    }

    res_params = {
        "nodes": list(ConversionReportNode),
        "pageInfo": list(PageInfoResParams)
    }

    def __init__(self, url: str, auth: Authentication):
        super().__init__(url, auth)

    def make_request(
            self,
            params: ConversionReportQueryParams,
            res_params: ConversionReportResParams
    ):
        return super()._make_request(params, res_params)

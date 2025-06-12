from enum import IntEnum, StrEnum
from typing import TypedDict, Required, NotRequired, List
from ..query_base import QueryBase, QueryParamsBase, PageInfoResParams
from ..authentication import Authentication


class ProductOfferV2ListType(IntEnum):
    HIGHEST_COMMISSION = 1
    TOP_PERFORMING = 2
    LANDING_CATEGORY = 3
    DETAIL_CATEGORY = 4
    DETAIL_SHOP = 5


class ProductOfferV2SortType(IntEnum):
    RELEVANCE_DESC = 1
    ITEM_SOLD_DESC = 2
    PRICE_DESC = 3
    PRICE_ASC = 4
    COMMISSION_DESC = 5


class ProductOfferV2QueryParams(QueryParamsBase):
    shopId: NotRequired[int]
    itemId: NotRequired[int]
    productCatId: NotRequired[int]
    listType: NotRequired[int]
    matchId: NotRequired[int]
    isAMSOffer: NotRequired[bool]
    isKeySeller: NotRequired[bool]


class ProductOfferV2Node(StrEnum):
    itemId = "itemId"
    commissionRate = "commissionRate"
    sellerCommissionRate = "sellerCommissionRate"
    shopeeCommissionRate = "shopeeCommissionRate"
    commission = "commission"
    sales = "sales"
    priceMax = "priceMax"
    priceMin = "priceMin"
    productCatIds = "productCatIds"
    ratingStar = "ratingStar"
    priceDiscountRate = "priceDiscountRate"
    imageUrl = "imageUrl"
    productName = "productName"
    shopId = "shopId"
    shopName = "shopName"
    shopType = "shopType"
    productLink = "productLink"
    offerLink = "offerLink"
    periodStartTime = "periodStartTime"
    periodEndTime = "periodEndTime"


class ProductOfferV2ResParams(TypedDict):
    nodes: Required[List[ProductOfferV2Node | str]]
    pageInfo: NotRequired[List[PageInfoResParams | str]]


class ProductOfferV2(QueryBase):
    query_name = "productOfferV2"

    query_params = {
        "shopId": None,
        "itemId": None,
        "productCatId": None,
        "listType": None,
        "matchId": None,
        "isAMSOffer": None,
        "isKeySeller": None,
        "keyword": "",
        "sortType": 1,
        "page": 1,
        "limit": 20
    }

    res_params = {
        "nodes": list(ProductOfferV2Node),
        "pageInfo": list(PageInfoResParams)
    }

    def __init__(self, url: str, auth: Authentication):
        super().__init__(url, auth)

    def make_request(
            self,
            params: ProductOfferV2QueryParams,
            res_params: ProductOfferV2ResParams
    ):
        return super()._make_request(params, res_params)

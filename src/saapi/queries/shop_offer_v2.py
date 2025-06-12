from enum import IntEnum, StrEnum
from typing import TypedDict, Required, NotRequired, List
from ..query_base import QueryBase, QueryParamsBase, PageInfoResParams
from ..authentication import Authentication


class ShopOfferV2ShopType(IntEnum):
    OFFICIAL_SHOP = 1
    PREFERRED_SHOP = 2
    PREFERRED_PLUS_SHOP = 4


class ShopOfferV2SortType(IntEnum):
    SHOP_LIST_SORT_TYPE_LATEST_DESC = 1
    SHOP_LIST_SORT_TYPE_HIGHEST_COMMISSION_DESC = 2
    SHOP_LIST_SORT_TYPE_POPULAR_SHOP_DESC = 3


class ShopOfferV2QueryParams(QueryParamsBase):
    shopId: NotRequired[int]
    shopType: NotRequired[List[int]]
    isKeySeller: NotRequired[bool]
    sellerCommCoveRatio: NotRequired[str]


class ShopOfferV2Node(StrEnum):
    commissionRate = "commissionRate"
    imageUrl = "imageUrl"
    offerLink = "offerLink"
    originalLink = "originalLink"
    shopId = "shopId"
    shopName = "shopName"
    ratingStar = "ratingStar"
    shopType = "shopType"
    remainingBudget = "remainingBudget"
    periodStartTime = "periodStartTime"
    periodEndTime = "periodEndTime"
    sellerCommCoveRatio = "sellerCommCoveRatio"
    bannerInfo = "bannerInfo"


class ShopOfferV2ResParams(TypedDict):
    nodes: Required[List[ShopOfferV2Node | str]]
    pageInfo: NotRequired[List[PageInfoResParams | str]]


class ShopOfferV2(QueryBase):
    query_name = "shopOfferV2"

    query_params = {
        "shopId": None,
        "shopType": None,
        "isKeySeller": None,
        "sellerCommCoveRatio": None,
        "keyword": "",
        "sortType": 1,
        "page": 1,
        "limit": 20
    }

    res_params = {
        "nodes": list(ShopOfferV2Node),
        "pageInfo": list(PageInfoResParams)
    }

    def __init__(self, url: str, auth: Authentication):
        super().__init__(url, auth)

    def make_request(
            self,
            params: ShopOfferV2QueryParams,
            res_params: ShopOfferV2ResParams
    ):
        return super()._make_request(params, res_params)

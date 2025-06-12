from enum import IntEnum, StrEnum
from typing import TypedDict, Required, NotRequired, List
from ..query_base import QueryBase, QueryParamsBase, PageInfoResParams
from ..authentication import Authentication


class ShopeeOfferV2SortType(IntEnum):
    LATEST_DESC = 1
    HIGHEST_COMMISSION_DESC = 2


class ShopeeOfferV2QueryParams(QueryParamsBase):
    pass


class ShopeeOfferV2Node(StrEnum):
    commissionRate = "commissionRate"
    imageUrl = "imageUrl"
    offerLink = "offerLink"
    originalLink = "originalLink"
    offerName = "offerName"
    offerType = "offerType"
    categoryId = "categoryId"
    collectionId = "collectionId"
    periodStartTime = "periodStartTime"
    periodEndTime = "periodEndTime"


class ShopeeOfferV2ResParams(TypedDict):
    nodes: Required[List[ShopeeOfferV2Node | str]]
    pageInfo: NotRequired[List[ShopeeOfferV2Node | str]]


class ShopeeOfferV2(QueryBase):
    query_name = "shopeeOfferV2"

    query_params = {
        "keyword": "",
        "sortType": 1,
        "page": 1,
        "limit": 20
    }

    res_params = {
        "nodes": list(ShopeeOfferV2Node),
        "pageInfo": list(PageInfoResParams)
    }

    def __init__(self, url: str, auth: Authentication):
        super().__init__(url, auth)

    def make_request(
            self,
            params: ShopeeOfferV2QueryParams,
            res_params: ShopeeOfferV2ResParams
    ):
        return super()._make_request(params, res_params)

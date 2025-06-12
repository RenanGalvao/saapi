from enum import StrEnum
from typing import TypedDict, Required, NotRequired, List
from ..query_base import QueryBase, QueryType
from ..authentication import Authentication


class GenerateShortLinkInput(TypedDict):
    originUrl: Required[str]
    subIds: NotRequired[List[str]]


class GenerateShortLinkQueryParams(TypedDict):
    input: GenerateShortLinkInput


class GenerateShortLinkResParams(StrEnum):
    shortLink = "shortLink"


class GenerateShortLink(QueryBase):
    query_type = QueryType.MUTATION
    query_name = "generateShortLink"

    query_params = {
        "input": {
            "originUrl": None,
            "subIds": None
        }
    }

    res_params = list(GenerateShortLinkResParams)

    def __init__(self, url: str, auth: Authentication):
        super().__init__(url, auth)

    def make_request(
        self,
        params: GenerateShortLinkQueryParams,
        res_params: GenerateShortLinkResParams
    ):
        return super()._make_request(params, res_params)

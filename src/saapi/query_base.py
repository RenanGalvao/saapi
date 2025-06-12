import json
import requests
from enum import StrEnum
from typing import TypedDict, NotRequired, List, Dict, Any
from .authentication import Authentication
from .errors import SaAPIError


class PageInfoResParams(StrEnum):
    page = "page"
    limit = "limit"
    hasNextPage = "hasNextPage"
    scrollId = "scrollId"


class QueryParamsBase(TypedDict):
    keyword: NotRequired[str]
    sortType: NotRequired[int]
    page: NotRequired[int]
    limit: NotRequired[int]


class ResParams(TypedDict):
    nodes: NotRequired[List[str]]
    pageInfo: NotRequired[List[str]]


class QueryType(StrEnum):
    QUERY = ""
    MUTATION = "mutation"


class QueryBase:
    query_type = QueryType.QUERY

    @property
    def query_name(self):
        raise NotImplementedError

    @property
    def query_params(self):
        raise NotImplementedError

    @property
    def res_params(self):
        raise NotImplementedError

    def __init__(self, url: str, auth: Authentication):
        self.url = url
        self.auth = auth

    @property
    def make_request():
        raise NotImplementedError

    def _make_request(
            self,
            params: Any,
            res_params: ResParams
    ):
        payload = json.dumps({
            "query": self._get_query(params, res_params),
        })
        headers = self.auth.get_headers(payload)

        res = requests.post(self.url, payload, headers=headers)
        res_json = res.json()
        if res.status_code == 200 and "data" in res_json:
            return res_json["data"][self.query_name]
        else:
            raise SaAPIError(**res_json["errors"][0])

    def _get_query(self, params: Any, res_params: ResParams):
        return f"""
{self.query_type} {{
    {self.query_name} ({self._get_query_params(params, self.query_params)}) {{
        {self._get_res_params(res_params, self.res_params)}
    }}
}}"""

    def _get_query_params(
        self,
        params: Dict,
        whitelist:  Dict,
        key: str = None
    ):
        if not params:
            return ""

        self._fields_check(params, whitelist)

        query_str = ""
        last_index = len(params) - 1
        for index, key_value in enumerate(params):
            if self._has_sub_items(params, key_value, False):
                query_str += "{0}".format(self._get_query_params(
                    params[key_value], whitelist[key_value], key_value
                ))
                continue

            comma = "," if index < last_index else ""
            new_line = "\n" if key and index < last_index else ""
            quoted_str = self._quote_str(params[key_value])
            query_str += f"{key_value}:{quoted_str}{comma}{new_line}"

        if not key:
            return query_str

        return "\n{0}: {{\n{1}\n}}".format(key, query_str)

    def _get_res_params(
        self,
        params: Dict | List,
        whitelist: Dict | List,
        key: str = None
    ):
        if not params:
            return ""

        self._fields_check(params, whitelist)

        fields_str = ""
        last_index = len(params) - 1
        for index, key_value in enumerate(params):
            if self._has_sub_items(params, key_value):
                fields_str += "{0}".format(self._get_res_params(
                    params[key_value], whitelist[key_value], key_value
                ))
                continue

            new_line = "\n" if index < last_index else ""
            fields_str += f"{key_value}{new_line}"

        if not key:
            return fields_str

        return "\n{0} {{\n{1}\n}}".format(key, fields_str)

    def _quote_str(self, source):
        if type(source) is str:
            return f"\"{source}\""
        else:
            return source

    def _has_sub_items(self, source: Dict, key: str, allow_list=True):
        if type(source) is not dict or key not in source:
            return False

        if allow_list:
            return type(source[key]) is dict or type(source[key]) is list
        return type(source[key]) is dict

    def _fields_check(self, source: Dict | List, whitelist: Dict | List):
        any_value_is_valid = whitelist is None
        if any_value_is_valid:
            return

        for index, key_value in enumerate(source):
            if key_value not in whitelist:
                raise ValueError(
                    "Value \"{0}\" not allowed. Allowed values: {1}".format(
                        key_value, list(whitelist)
                    )
                )

            if self._has_sub_items(source, key_value):
                self._fields_check(
                    source[key_value], whitelist[key_value]
                )

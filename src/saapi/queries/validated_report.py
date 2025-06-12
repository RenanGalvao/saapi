from typing import TypedDict, Required, NotRequired, List
from ..query_base import PageInfoResParams
from .report_query_base import ReportQueryBase, ReportQueryParamsBase, \
    ReportNode as ValidatedReportNode
from ..authentication import Authentication


class ValidatedReportQueryParams(ReportQueryParamsBase):
    validationId: Required[int]


class ValidatedReportResParams(TypedDict):
    nodes: Required[List[ValidatedReportNode | str]]
    pageInfo: NotRequired[List[PageInfoResParams | str]]


class ValidatedReport(ReportQueryBase):
    query_name = "validatedReport"

    query_params = {
        "validationId": None,
        "limit": 20,
        "scrollId": None
    }

    res_params = {
        "nodes": list(ValidatedReportNode),
        "pageInfo": list(PageInfoResParams)
    }

    def __init__(self, url: str, auth: Authentication):
        super().__init__(url, auth)

    def make_request(
        self,
        params: ValidatedReportQueryParams,
        res_params: ValidatedReportResParams
    ):
        return super()._make_request(params, res_params)

from functools import cached_property
from typing import Protocol, Dict, Any
from ..authentication import Authentication
from .shopee_offer_v2 import ShopeeOfferV2, ShopeeOfferV2QueryParams, \
    ShopeeOfferV2ResParams
from .shop_offer_v2 import ShopOfferV2, ShopOfferV2QueryParams, \
    ShopOfferV2ResParams
from .product_offer_v2 import ProductOfferV2, ProductOfferV2QueryParams, \
    ProductOfferV2ResParams
from .conversion_report import ConversionReport, ConversionReportQueryParams, \
    ConversionReportResParams
from .validated_report import ValidatedReport, ValidatedReportQueryParams, \
    ValidatedReportResParams


class ShopeeOfferV2Interface(Protocol):
    def __call__(
        self,
        params: ShopeeOfferV2QueryParams,
        res_params: ShopeeOfferV2ResParams
    ) -> Dict[str, Any]:
        pass


class ShopOfferV2Interface(Protocol):
    def __call__(
        self,
        params: ShopOfferV2QueryParams,
        res_params: ShopOfferV2ResParams
    ) -> Dict[str, Any]:
        pass


class ProductOfferV2Interface(Protocol):
    def __call__(
        self,
        params: ProductOfferV2QueryParams,
        res_params: ProductOfferV2ResParams
    ) -> Dict[str, Any]:
        pass


class ConversionReportInterface(Protocol):
    def __call__(
        self,
        params: ConversionReportQueryParams,
        res_params: ConversionReportResParams
    ) -> Dict[str, Any]:
        pass


class ValidatedReportInterface(Protocol):
    def __call__(
        self,
        params: ValidatedReportQueryParams,
        res_params: ValidatedReportResParams
    ) -> Dict[str, Any]:
        pass


class Queries:
    def __init__(self, url: str, auth: Authentication):
        self.url = url
        self.auth = auth

    @cached_property
    def shopee_offer_v2(self) -> ShopeeOfferV2Interface:
        return ShopeeOfferV2(self.url, self.auth).make_request

    @cached_property
    def shop_offer_v2(self) -> ShopOfferV2Interface:
        return ShopOfferV2(self.url, self.auth).make_request

    @cached_property
    def product_offer_v2(self) -> ProductOfferV2Interface:
        return ProductOfferV2(self.url, self.auth).make_request

    @cached_property
    def conversion_report(self) -> ConversionReportInterface:
        return ConversionReport(self.url, self.auth).make_request

    @cached_property
    def validated_report(self) -> ValidatedReportInterface:
        return ValidatedReport(self.url, self.auth).make_request

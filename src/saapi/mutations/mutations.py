from functools import cached_property
from typing import Protocol, Dict, Any
from ..authentication import Authentication
from .generate_short_link import GenerateShortLink, \
    GenerateShortLinkQueryParams, GenerateShortLinkResParams


class GenerateShortLinkInterface(Protocol):
    def __call__(
        self,
        params: GenerateShortLinkQueryParams,
        res_params: GenerateShortLinkResParams
    ) -> Dict[str, Any]:
        pass


class Mutations:
    def __init__(self, url: str, auth: Authentication):
        self.url = url
        self.auth = auth

    @cached_property
    def generate_short_link(self) -> GenerateShortLinkInterface:
        return GenerateShortLink(self.url, self.auth).make_request

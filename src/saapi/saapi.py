from functools import cached_property
from typing import TypedDict, Required, NotRequired
from .authentication import Authentication
from .countries import Country
from .queries.queries import Queries
from .mutations.mutations import Mutations


class SaAPIConfig(TypedDict):
    app_id: Required[str]
    secret: Required[str]
    country: NotRequired[str]


class SaAPI:
    def __init__(self, config: SaAPIConfig):
        self.auth = Authentication(config.get("app_id"), config.get("secret"))

        if config.get("country"):
            if not isinstance(config.get("country"), Country):
                raise ValueError(
                    f"Allowed country values: {list(Country)}"
                )
            country = config.get("country")
        else:
            country = Country.BRAZIL

        self.url = "https://open-api.affiliate.shopee.{0}/graphql".format(
            country
        )

    @cached_property
    def queries(self):
        return Queries(self.url, self.auth)

    @cached_property
    def mutations(self) -> Mutations:
        return Mutations(self.url, self.auth)

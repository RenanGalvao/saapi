# SaAPI
> :warning: **Esse pacote não é oficial.**

Um simples wrapper para a API de afiliados da Shopee[^1].

```python
from saapi import SaAPI

client = SaAPI({
    "app_id": "seu_app_id",
    "secret": "seu_secret"
})
res = client.queries.product_offer_v2(
    {"keyword": "tênis"},
    {"nodes": ["itemId", "productName"]}
)

print(res)
# { "nodes": [
#    {'itemId': 22093519050, 'productName': 'Tênis Sapatênis Polo Masculino'},
#    ...
#   ]
# }
```
Todas as queries e mutations que não estão depreciados foram implementados, os 
campos que foram depreciados não foram implementados.

[![Downloads](https://static.pepy.tech/badge/saapi/month)](https://pepy.tech/project/saapi)
[![Supported Versions](https://img.shields.io/pypi/pyversions/saapi.svg)](https://pypi.org/project/saapi)
[![Contributors](https://img.shields.io/github/contributors/renangalvao/saapi.svg)](https://github.com/renangalvao/saapi/graphs/contributors)

## Instalação
```console
$ pip install saapi
```
Versão mínima do python 3.9.


## Uso com tipos
Todas as operações possuem tipos para facilitar o uso e evitar erros, seja argumentos
ou campos de retorno.

```python
from saapi import SaAPI
from saapi.queries.product_offer_v2 import ProductOfferV2Node, ProductOfferV2SortType
from saapi.queries import PageInfoResParams

client = SaAPI({
    "app_id": "seu_app_id",
    "secret": "seu_secret"
})
res = client.queries.product_offer_v2(
    {
        "keyword": "blusa",
        "limit": 10,
        "sortType": ProductOfferV2SortType.COMMISSION_DESC
    },
    {
        "nodes": [
            ProductOfferV2Node.itemId,
            ProductOfferV2Node.productName,
            ProductOfferV2Node.offerLink
        ],
        "pageInfo": [
            PageInfoResParams.hasNextPage
        ]
    }
)
```


## Lidando com erros
```python
import logging
from saapi import SaAPI
from saapi.errors import SaAPIError, SaAPIErrorCode

client = SaAPI({
    "app_id": "seu_app_id",
    "secret": "seu_secret"
})
try:
    res = client.queries.product_offer_v2({},{"nodes": [...]})
    # seu código
except SaAPIError as err:
    if err.extensions["code"] == SaAPIErrorCode.IDENTITY_AUTHENTICATION_ERROR:
        logging.exception(err.message)
    else:
        logging.exception("algo deu errado")
```

## Outros países
Caso as credenciais sejam de outro país, é possível configurar:
```python
from saapi import SaAPI
from saapi.countries import Country

client = SaAPI({
    ...,
    "country": Country.INDONESIA
})
```


## Desenvolvimento
Faça um clone, configure um ambiente virtual e instale ``pip install --editable .[all]``. Para fazer
testes você deve utilizar o comando ``tox``. Tenha em mente que para testar em todas as versões você
precisa tê-las instaladas e com acesso global/local. Particularmente utilizei o asdf[^2] para isso.

[^1]: [Documentação](https://affiliate.shopee.com.br/open_api/home). É preciso estar logado para visualizar a documentação.
[^2]: [asdf](https://asdf-vm.com/)

import pytest
from pytest_mock import MockFixture
import re
from saapi.query_base import QueryBase
from saapi.authentication import Authentication
from saapi.errors import SaAPIError


@pytest.fixture
def query_base():
    return QueryBase("url", Authentication("app_id", "secret"))


def test__make_request(query_base, mocker: MockFixture):
    query_name = "testName"
    mocker.patch.object(
        QueryBase,
        "query_name",
        new_callable=mocker.PropertyMock,
        return_value=query_name
    )

    mocker.patch.object(
        query_base,
        "_get_query",
        return_value="query"
    )

    # auth
    mock_auth = mocker.Mock()
    mock_auth.get_headers = "headers"
    mocker.patch.object(
        query_base,
        "auth",
        new_callable=mocker.PropertyMock,
        return_value=mock_auth
    )

    # requests
    mock_post = mocker.patch("requests.post")

    class MockedResponse:
        def __init__(self, status_code=200, data={}):
            self.status_code = status_code
            self.data = data

        def json(self):
            return self.data

    # tests
    status_code = 200
    returned_value = 1
    data = {
        "data": {
            query_name: returned_value
        }
    }
    mock_post.return_value = MockedResponse(status_code, data)
    res = query_base._make_request({}, {})
    assert res == returned_value

    status_code = 400
    returned_value = {
        "message": "error[erroCode]: message",
        "extensions": {
            "code": 10_010,
            "message": "message"
        }
    }
    data = {
        "errors": [returned_value]
    }
    mock_post.return_value = MockedResponse(status_code, data)
    with pytest.raises(SaAPIError):
        res = query_base._make_request({}, {})
        assert isinstance(res, SaAPIError) is True


def test__get_query(query_base, mocker: MockFixture):
    query_type = "testType"
    mocker.patch.object(
        query_base,
        "query_type",
        query_type
    )

    query_name = "testName"
    mocker.patch.object(
        QueryBase,
        "query_name",
        new_callable=mocker.PropertyMock,
        return_value=query_name
    )

    query_params = {"itemId": None, "page": 1, "limit": 20}
    mocker.patch.object(
        QueryBase,
        "query_params",
        new_callable=mocker.PropertyMock,
        return_value=query_params
    )

    res_params = {
        "nodes": ["itemId", "productName", "imageUrl"],
        "pageInfo": ["page", "limit", "hasNextPage", "scrollId"]
    }
    mocker.patch.object(
        QueryBase,
        "res_params",
        new_callable=mocker.PropertyMock,
        return_value=res_params
    )

    user_params = {"limit": 50}
    user_res_params = {
        "nodes": ["itemId", "productName"]
    }
    query = query_base._get_query(user_params, user_res_params)

    for param in user_params:
        assert query.find(param) >= 0

    for param in user_res_params:
        assert query.find(param) >= 0

    assert len(re.findall(query_type, query)) == 1
    assert len(re.findall(query_name, query)) == 1


def test__get_query_params(query_base):
    params = {"productName": "teste", "limit": 10}
    whitelist = {"productName": None, "page": 1, "limit": 20}
    query_params = query_base._get_query_params(params, whitelist)
    for param in params:
        assert query_params.find(param) >= 0
    assert len(re.findall(",", query_params)) == 1

    params = {"collectionId": 1231}
    with pytest.raises(ValueError):
        query_params = query_base._get_query_params(params, whitelist)

    #
    params = {
        "input": {
            "originUrl": "https://kek.com",
            "subIds": ["sub1", "sub2", "sub3"]
        }
    }
    whitelist = {"input": {
        "originUrl": None,
        "subIds": None
    }}
    query_params = query_base._get_query_params(params, whitelist)
    for param in params:
        if query_base._has_sub_items(params, param):
            for sub_param in params[param]:
                assert query_params.find(sub_param) >= 0
        assert query_params.find(param) >= 0
    assert len(re.findall("{|}", query_params)) == 2
    assert len(re.findall("\\[|\\]", query_params)) == 2

    params = {
        "input": {
            "productName": "audio",
            "subIds": ["sub1", "sub2", "sub3"]
        }
    }
    with pytest.raises(ValueError):
        query_base._get_query_params(params, whitelist)


def test__get_res_params(query_base):
    params = ["field1", "field2", "field3"]
    whitelist = ["field5", "field1", "field2", "field6", "field3", "field4"]
    res_params = query_base._get_res_params(params, whitelist)
    for param in params:
        assert res_params.find(param) >= 0

    params = ["field3", "field7"]
    with pytest.raises(ValueError):
        query_base._get_res_params(params, whitelist)

    #
    params = {"nodes": ["shopId"], "pageInfo": ["page", "limit"]}
    whitelist = {
        "nodes": ["shopId", "shopName"],
        "pageInfo": ["page", "hasNextPage", "limit"]
    }
    res_params = query_base._get_res_params(params, whitelist)
    for param in params:
        if query_base._has_sub_items(params, param):
            for sub_param in params[param]:
                assert res_params.find(sub_param) >= 0
        assert res_params.find(param) >= 0

    params = {"nodes": ["collectionId"], "pageInfo": ["hasNextPage"]}
    with pytest.raises(ValueError):
        query_base._get_res_params(params, whitelist)


def test__quote_str(query_base):
    original_text = "s"
    text = query_base._quote_str(original_text)
    assert len(re.findall("\"", text)) == 2

    original_data = 10
    data = query_base._quote_str(original_data)
    assert type(data) is int


def test__has_sub_items(query_base):
    source = {"a": {"c": 1}, "b": [1, 2, 3], "c": 1}
    key = "a"
    assert query_base._has_sub_items(source, key) is True

    key = "b"
    assert query_base._has_sub_items(source, key) is True

    key = "c"
    assert query_base._has_sub_items(source, key) is False

    source = {"a": [1, 2, 3]}
    key = "a"
    assert query_base._has_sub_items(source, key, False) is False


def test__fields_check(query_base):
    source = {"field1": 1, "field2": 2, "field3": 3}
    whitelist = {"field1": 1, "field2": 2, "field3": 3}
    query_base._fields_check(source, whitelist)

    #
    source = {"withinWhitelist": 1, "notInWhitelist": 2, }
    whitelist = {"anotherKey": 1, "whitinWhitList": 2}

    with pytest.raises(ValueError):
        query_base._fields_check(source, whitelist)

    #
    source = {"dict": {"itemA": {"aList": ["hello"]}}}
    whitelist = {"dict": {"itemA": {"aList": ["world", "hello"]}}}
    query_base._fields_check(source, whitelist)

    #
    source = {"dict": {"itemA": 2}, "list": ["validValue", "notValid"]}
    whitelist = {
        "dict": {"itemA": 1},
        "list": ["validValue", "anotherValue"]
    }

    with pytest.raises(ValueError):
        query_base._fields_check(source, whitelist)

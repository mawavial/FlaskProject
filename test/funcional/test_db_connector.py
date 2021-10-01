import json
import pytest
from repository.db_connector import DBConnector


@pytest.fixture()
def fixture_db_connector(mocker):
    object_to_save = {"123": {"a":"a"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.path("redis.Redis.get").return_value = json.dumps(object_to_save)
    db_conn = DBConnector()
    return db_conn


def test_get_by_id(fixture_db_connector):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    # mocker.patch("db_connector.DBConnector.get_by_id").return_value = object_to_save
    # mocker.patch("db_connector.DBConnector.save").result_value = True
    # db_connector = DBConnector()
    db_connector = fixture_db_connector
    db_connector.save(id_test, object_to_save)
    result = db_connector.get_by_id(id_test)
    assert result == object_to_save


def test_save_mock(mocker):
    object_to_save = {"123": {"a": "a"}}
    id_test = "123"
    mocker.patch("db_connector.DBConnector.save").result_value = True
    db_connector = DBConnector()
    result_save = db_connector.save(id_test, object_to_save)
    assert result_save

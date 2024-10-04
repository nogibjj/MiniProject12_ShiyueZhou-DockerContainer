"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_data, read_data, update_data, delete_data


def test_extract():
    test = extract()
    return test


def test_transform():
    test = load()
    return test


def test_create():
    test = create_data()
    return test


def test_read():
    test = read_data()
    return test


def test_update():
    test = update_data()
    return test


def test_delete():
    test = delete_data()
    return test


if __name__ == "__main__":
    # assert test_func()["extract"] == "data/murder_2015_final.csv"
    # assert test_func()["transform"] == "Murder2015.db"
    # assert test_func()["create"] == "Create Success"
    # assert test_func()["read"] == "Read Success"
    # assert test_func()["update"] == "Update Success"
    # assert test_func()["delete"] == "Delete Success"
    check = test_extract()
    assert check == "data/murder_2015_final.csv"
    check = test_transform()
    assert check == "Murder2015.db"
    check = test_create()
    assert check == "Create Success"
    check = test_read()
    assert check == "Read Success"
    check = test_update()
    assert check == "Update Success"
    check = test_delete()
    assert check == "Delete Success"

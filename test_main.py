"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_extract():
    test = extract()
    return test


def test_transform():
    test = load()
    return test


def test_query():
    test = query()
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
    check = test_query()
    assert check == "Execure Success"


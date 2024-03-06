import pytest
from main import ChainingHashTable, LinearProbingHashTable

@pytest.fixture
def chaining_table():
    return ChainingHashTable(size=10)

@pytest.fixture
def probing_table():
    return LinearProbingHashTable(size=10)

def test_chaining_insert_and_get(chaining_table):
    chaining_table.insert("key1", "value1")
    chaining_table.insert("key2", "value2")
    assert chaining_table.get("key1") == "value1"
    assert chaining_table.get("key2") == "value2"

def test_probing_insert_and_get(probing_table):
    probing_table.insert("key1", "value1")
    probing_table.insert("key2", "value2")
    assert probing_table.get("key1") == "value1"
    assert probing_table.get("key2") == "value2"

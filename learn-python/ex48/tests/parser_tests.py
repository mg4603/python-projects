from ex48.lexicon import scan
from ex48.parser import *
from nose.tools import *

def test_peek():
    assert_equal(peek(scan("kill the bear")), "verb")
    assert_equal(peek(scan("bear")), "noun")

def test_match():
    assert_equal(match(scan("kill the bear"), "verb"), ("verb", "kill"))
    assert_equal(match(scan("kill the bear"), "noun"), None)
    assert_equal(match(scan(""), "noun"), None)
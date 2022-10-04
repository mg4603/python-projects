from ex48.lexicon import scan
from ex48.parser import *
from nose.tools import *

def test_peek():
    assert_equal(peek(scan("kill the bear")), "verb")
    assert_equal(peek(scan("bear")), "noun")

def test_match():
    assert_equal(match(scan("kill the bear"), "verb"), 
                 ("verb", "kill"))
    assert_equal(match(scan("kill the bear"), "noun"), 
                 None)
    assert_equal(match(scan(""), "noun"), None)

def test_skip():
    word_list = [("stop", "the"),
                 ("noun", "player"),
                 ("verb", "kill"),
                 ("stop", "the"),
                 ("noun", "bear")]
    skip(word_list, "stop")
    assert_equal(match(word_list, peek(word_list)),
                 ("noun", "player"))

def test_parse_verb():
    assert_equal(Parser(scan("the kill bear")).parse_verb(), ("verb", "kill"))
    assert_raises(ParserError, Parser(scan("the player kill the bear")).parse_verb)
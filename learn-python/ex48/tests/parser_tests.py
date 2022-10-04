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
    assert_equal(Parser(scan("the kill bear")).parse_verb(),
                 ("verb", "kill"))
    assert_raises(ParserError, 
                  Parser(scan("the player kill the bear")).parse_verb)

def test_parse_object():
    assert_equal(Parser(scan("the door kills the bear")).parse_object(),
                 ("noun", "door"))
    assert_equal(Parser(scan("the west of east")).parse_object(),
                 ("direction", "west"))
    assert_raises(
            ParserError,
            Parser(scan("kill the bear")).parse_object
            )

def test_parse_subject():
    assert_equal(Parser(scan("kills the bear")).
                 parse_subject(("noun", "door")).get(),
                 Sentence(("noun", "door"),
                          ("verb", "kill"),
                          ("noun", "bear")).get())
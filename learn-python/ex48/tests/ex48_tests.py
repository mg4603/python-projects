from nose.tools import *
from ex48.lexicon import scan

def test_directions():
    assert_equal(scan("north"), [("direction", "north")])
    result = scan("north south east")
    assert_equal(result, [("direction", "north"),
                          ("direction", "south")
                          ("direction", "east")])

def test_verbs():
    assert_equal(lexicon.scan("go"), [("verb", "go")])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [("verb", "go"),
                          ("verb", "kill"),
                          ("verb", "eat")])

def test_stops():
    assert_equal(lexicon.scan("the"), [("stop", "the")])
    result = lexicon.scan("the in of")
    assert_equal(result, [("stop", "the"),
                          ("stop", "in"),
                          ("stop", "of")])

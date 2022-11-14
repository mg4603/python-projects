from logging import basicConfig, debug, DEBUG, disable, CRITICAL
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def q1():
    spam = 9
    assert spam >= 10

def q2():
    eggs = 'hello'
    bacon = 'HeLLo'
    assert eggs.lower() != bacon.lower()

def q3():
    assert False


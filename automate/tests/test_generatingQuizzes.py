from scripts.generatingQuizes import get_banner, make_question, get_answer_banner

def test_get_banner():
    assert get_banner(1) == '''Name:

Date:

Period:

                    State Capitals Quiz (Form2)

'''

def test_get_answer_banner():
    assert get_answer_banner(1) == '''                    State Capitals Quiz (Form2)

'''

def test_make_question():
    assert make_question(
        1, {'question': 'asdf', 'answer': 'asdf'}, ['1asdf', '2asdf', '3asdf']
    ) == \
"""2. What is the capital of asdf?
    A. 1asdf
    B. 2asdf
    C. 3asdf
    D. asdf

"""
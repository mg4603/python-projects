from scripts.generatingQuizes import get_banner, make_question

def test_get_banner():
    assert get_banner(1) == '''Name:

Date:

Period:

                    State Capitals Quiz (Form2)

'''

def test_make_question():
    assert make_question(
        1, {'question': 'asdf', 'answer': 'asdf'}, ['1asdf', '2asdf', '3asdf']
    )
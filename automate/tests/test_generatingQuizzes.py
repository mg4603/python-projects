from scripts.generatingQuizes import get_banner

def test_get_banner():
    assert get_banner(1) == '''Name:

Date:

Period:

                    State Capitals Quiz (Form2)

'''
from time_deretardator import correct_time

def test_deretardator():
    assert correct_time('1:00 PM') == '13:00'
import pytest
from project import is_mobile_no, extract_country_code,find_the_country,play_country_music

def test_is_mobile_no():
    assert is_mobile_no("+919876543210") == True
    assert is_mobile_no("+819012345678") == True
    assert is_mobile_no("+11234567890") == True
    assert is_mobile_no("+821012345678") == True
    assert is_mobile_no("9876543210") == False
    assert is_mobile_no("+91987654321") == False
    assert is_mobile_no("+81901234567") == False
    assert is_mobile_no("+123456789") == False
    assert is_mobile_no("+8210123456") == False
    assert is_mobile_no("+659876543") == False

def test_extract_country_code():
    assert extract_country_code("+919876543210") == "91"
    assert extract_country_code("+819012345678") == "81"
    assert extract_country_code("+1234567890") == "1"
    assert extract_country_code("+82101234567") == "82"
    assert extract_country_code("+6598765432") == "65"
    assert extract_country_code("9876543210") == None

def test_find_the_country():
    assert find_the_country("91") == "IN"
    assert find_the_country("81") == "JP"
    assert find_the_country("1") == "US"
    assert find_the_country("82") == "KR"
    assert find_the_country("65") == "SG"

def test_play_country_music():
    play_country_music("IN")
    play_country_music("JP")
    play_country_music("US")
    play_country_music("KR")
    play_country_music("SG")
    with pytest.raises(Exception):
        play_country_music("XX")

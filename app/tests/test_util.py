import pytest

import util

def test_util_squeeze_starts_with_slash():
    expect = "/hoge/huga/com"
    actual = util.squeeze("///hoge/huga//com", "/")

    assert(actual == expect)


def test_util_squeeze_ends_with_slash():
    expect = "/h/o/g/e/huga/com/"
    actual = util.squeeze("///h//o/g/e/huga//com///", "/")

    assert(actual == expect)


def test_util_dom_to_path_starts_ends_with_dot():
    with pytest.raises(ValueError) as e:
        actual = util.dom_to_path(".hoge.huga.com.")

        assert e.value.message == "'.hoge.huga.com.' starts/ends with dot."


def test_util_dom_to_path_includes_consecutive_dots_raise_exception():
    with pytest.raises(ValueError) as e:
        util.dom_to_path("hoge.huga...com")

        assert e.value.message == "'hoge.huga...com' includes consecutive dots."

def test_util_make_A_record_with_kwargs():
     actual = util.make_A_record("1.1.1.1", ttl=800, weight=1)
     expect = { "host": "1.1.1.1", "ttl": 800, "weight": 1 }

     assert actual == expect

def test_util_make_A_record_without_kwargs():
     actual = util.make_A_record("1.1.1.1")
     expect = { "host": "1.1.1.1", "ttl": 600 }

     assert actual == expect

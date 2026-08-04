import pytest

from day05.exact_match import exact_match, normalize_text


@pytest.mark.parametrize(
    ("original", "expected"),
    [
        ("Hello", "hello"),
        (" HELLO ", "hello"),
        ("hello!", "hello"),
        ("你好。", "你好"),
        ("你好，世界！", "你好世界"),
        ("  hello   world  ", "hello world"),
        ("\thello\nworld\t", "hello world"),
        ("Python？", "python"),
        ("北京；", "北京"),
        ("", ""),
    ],
)
def test_normalize_text(original, expected):
    assert normalize_text(original) == expected


@pytest.mark.parametrize(
    ("actual", "expected", "result"),
    [
        ("Hello", "hello", True),
        (" Hello ", "hello", True),
        ("北京。", "北京", True),
        ("你好，世界！", "你好世界", True),
        ("hello   world", "hello world", True),
        ("Python", "Java", False),
        ("北京", "上海", False),
        ("", "", True),
        (None, None, True),
        (None, "", False),
        ("", None, False),
    ],
)
def test_exact_match_normal_mode(actual, expected, result):
    assert exact_match(actual, expected) is result


@pytest.mark.parametrize(
    ("actual", "expected", "result"),
    [
        ("Hello", "hello", False),
        (" hello", "hello", False),
        ("hello!", "hello", False),
        ("hello", "hello", True),
        ("北京", "北京", True),
        (None, None, True),
    ],
)
def test_exact_match_strict_mode(actual, expected, result):
    assert exact_match(actual, expected, strict=True) is result


def test_normalize_text_can_keep_case():
    assert normalize_text("Hello", lower=False) == "Hello"


def test_normalize_text_can_keep_punctuation():
    assert normalize_text(
        "Hello!",
        strip_punctuation=False,
    ) == "hello!"


def test_normalize_text_none():
    assert normalize_text(None) is None


def test_normalize_text_rejects_integer():
    with pytest.raises(TypeError):
        normalize_text(123)


def test_exact_match_rejects_invalid_actual():
    with pytest.raises(TypeError):
        exact_match(123, "123")


def test_exact_match_rejects_invalid_expected():
    with pytest.raises(TypeError):
        exact_match("123", 123)


def test_exact_match_without_normalizer():
    assert exact_match(
        "Hello",
        "hello",
        normalizer=None,
    ) is False
import re
import unicodedata
from collections.abc import Callable


def normalize_text(
    text: str | None,
    lower: bool = True,
    strip_punctuation: bool = True,
) -> str | None:
    """
    对文本进行标准化。

    处理规则：
    1. 如果输入为None，返回None
    2. 去除字符串首尾空格
    3. 根据lower参数决定是否转换成小写
    4. 根据strip_punctuation参数决定是否去除中英文标点
    5. 将多个连续空白字符合并成一个普通空格

    Args:
        text: 需要标准化的文本。
        lower: 是否转换成小写，默认为True。
        strip_punctuation: 是否去除标点，默认为True。

    Returns:
        标准化后的文本；输入为None时返回None。

    Raises:
        TypeError: 当text既不是字符串也不是None时抛出。
    """
    if text is None:
        return None

    if not isinstance(text, str):
        raise TypeError("text必须是字符串或None")

    normalized = text.strip()

    if lower:
        normalized = normalized.lower()

    if strip_punctuation:
        normalized = "".join(
            character
            for character in normalized
            if not unicodedata.category(character).startswith("P")
        )

    normalized = re.sub(r"\s+", " ", normalized)

    return normalized.strip()


def exact_match(
    actual: str | None,
    expected: str | None,
    normalizer: Callable[[str | None], str | None] | None = normalize_text,
    strict: bool = False,
) -> bool:
    """
    判断模型实际回答是否与标准答案匹配。

    Args:
        actual: 模型实际输出。
        expected: 测试集中的标准答案。
        normalizer: 使用的文本标准化函数。
        strict: 是否启用严格匹配模式。

    Returns:
        匹配成功返回True，否则返回False。
    """
    if actual is None or expected is None:
        return actual is expected

    if not isinstance(actual, str):
        raise TypeError("actual必须是字符串或None")

    if not isinstance(expected, str):
        raise TypeError("expected必须是字符串或None")

    if strict or normalizer is None:
        return actual == expected

    return normalizer(actual) == normalizer(expected)
if __name__ == "__main__":
    actual_answer = " Hello，World！ "
    expected_answer = "hello world"

    normal_result = exact_match(
        actual=actual_answer,
        expected=expected_answer,
    )

    strict_result = exact_match(
        actual=actual_answer,
        expected=expected_answer,
        strict=True,
    )

    print("模型实际回答：", repr(actual_answer))
    print("测试集标准答案：", repr(expected_answer))
    print("普通匹配结果：", normal_result)
    print("严格匹配结果：", strict_result)
from __future__ import annotations

from collections import Counter, defaultdict
from typing import TypedDict


class EvaluationSample(TypedDict):
    """
    单条评测样本的数据格式。

    每条样本必须包含：
    1. id：样本编号
    2. category：样本类别
    3. input：输入问题
    4. expected：期望答案
    """

    id: int
    category: str
    input: str
    expected: str


# 每条样本必须拥有的字段
REQUIRED_FIELDS = {
    "id",
    "category",
    "input",
    "expected",
}


# ============================================================
# 12条评测样本
# ============================================================
#
# 设计说明：
# 1. 第3条和第11条数据的ID都是3，用于测试重复ID检测；
# 2. 第12条数据的expected为空，用于测试失败数据检测；
# 3. category数量：
#    math       4条
#    general    3条
#    python     3条
#    translation 2条

EVALUATION_SAMPLES: list[EvaluationSample] = [
    {
        "id": 1,
        "category": "math",
        "input": "1 + 1 等于多少？",
        "expected": "2",
    },
    {
        "id": 2,
        "category": "math",
        "input": "5 × 6 等于多少？",
        "expected": "30",
    },
    {
        "id": 3,
        "category": "math",
        "input": "10 - 3 等于多少？",
        "expected": "7",
    },
    {
        "id": 4,
        "category": "python",
        "input": "Python中使用什么函数输出内容？",
        "expected": "print",
    },
    {
        "id": 5,
        "category": "python",
        "input": "Python中使用什么关键字定义函数？",
        "expected": "def",
    },
    {
        "id": 6,
        "category": "python",
        "input": "Python列表使用什么符号表示？",
        "expected": "[]",
    },
    {
        "id": 7,
        "category": "general",
        "input": "中国的首都是哪里？",
        "expected": "北京",
    },
    {
        "id": 8,
        "category": "general",
        "input": "一年有多少个月？",
        "expected": "12",
    },
    {
        "id": 9,
        "category": "translation",
        "input": "把apple翻译成中文。",
        "expected": "苹果",
    },
    {
        "id": 10,
        "category": "translation",
        "input": "把book翻译成中文。",
        "expected": "书",
    },

    # 故意重复ID=3，用来测试重复ID检测功能
    {
        "id": 3,
        "category": "math",
        "input": "8 ÷ 2 等于多少？",
        "expected": "4",
    },

    # 故意将expected留空，用来测试失败数据检测功能
    {
        "id": 12,
        "category": "general",
        "input": "这是一条缺少标准答案的测试样本。",
        "expected": "",
    },
]


def group_by_category(
    samples: list[EvaluationSample],
) -> dict[str, list[EvaluationSample]]:
    """
    按category对样本进行分组。

    参数：
        samples：评测样本列表。

    返回：
        category和对应样本列表组成的字典。

    返回结果示例：
        {
            "math": [样本1, 样本2],
            "python": [样本3]
        }
    """
    grouped: defaultdict[str, list[EvaluationSample]] = defaultdict(list)

    for sample in samples:
        category = sample["category"].strip()
        grouped[category].append(sample)

    return dict(grouped)


def find_duplicate_ids(
    samples: list[EvaluationSample],
) -> dict[int, list[int]]:
    """
    查找重复ID，并返回重复ID的全部位置。

    注意：
        返回的位置从1开始计算，而不是从0开始。
        这样更符合“第几条数据”的阅读习惯。

    返回结果示例：
        {
            3: [3, 11]
        }

    含义：
        ID=3出现在第3条和第11条数据中。
    """
    id_positions: defaultdict[int, list[int]] = defaultdict(list)

    for position, sample in enumerate(samples, start=1):
        sample_id = sample["id"]
        id_positions[sample_id].append(position)

    duplicate_ids = {
        sample_id: positions
        for sample_id, positions in id_positions.items()
        if len(positions) > 1
    }

    return duplicate_ids


def find_failed_cases(
    samples: list[EvaluationSample],
) -> list[EvaluationSample]:
    """
    查找格式不合格的失败样本。

    本任务只有id、category、input和expected，
    没有实际模型回答actual，因此这里的“失败样本”
    指数据格式不合格，而不是模型回答错误。

    以下情况会被认定为失败样本：
    1. 缺少必要字段；
    2. ID不是正整数；
    3. category不是非空字符串；
    4. input不是非空字符串；
    5. expected不是非空字符串。
    """
    failed_cases: list[EvaluationSample] = []

    for sample in samples:
        # 检查是否缺少必要字段
        if not REQUIRED_FIELDS.issubset(sample.keys()):
            failed_cases.append(sample)
            continue

        sample_id = sample["id"]
        category = sample["category"]
        input_text = sample["input"]
        expected = sample["expected"]

        # ID必须是正整数
        if not isinstance(sample_id, int) or sample_id <= 0:
            failed_cases.append(sample)
            continue

        # category必须是非空字符串
        if not isinstance(category, str) or not category.strip():
            failed_cases.append(sample)
            continue

        # input必须是非空字符串
        if not isinstance(input_text, str) or not input_text.strip():
            failed_cases.append(sample)
            continue

        # expected必须是非空字符串
        if not isinstance(expected, str) or not expected.strip():
            failed_cases.append(sample)

    return failed_cases


def count_by_category(
    samples: list[EvaluationSample],
) -> list[tuple[str, int]]:
    """
    统计每个category的样本数量。

    排序规则：
    1. 首先按照样本数量降序排列；
    2. 数量相同时，按照category名称升序排列。

    返回结果示例：
        [
            ("math", 4),
            ("general", 3),
            ("python", 3),
            ("translation", 2),
        ]
    """
    category_counter = Counter(
        sample["category"].strip()
        for sample in samples
        if isinstance(sample.get("category"), str)
        and sample["category"].strip()
    )

    sorted_statistics = sorted(
        category_counter.items(),
        key=lambda item: (-item[1], item[0]),
    )

    return sorted_statistics


def print_report(samples: list[EvaluationSample]) -> None:
    """把数据处理结果打印到控制台。"""

    print("=" * 56)
    print("Day04：评测数据处理结果")
    print("=" * 56)

    print(f"\n1. 样本总数：{len(samples)}条")

    print("\n2. 按category分组：")
    grouped = group_by_category(samples)

    for category, category_samples in grouped.items():
        print(f"   {category}: {len(category_samples)}条")

    print("\n3. 重复ID检测：")
    duplicate_ids = find_duplicate_ids(samples)

    if duplicate_ids:
        for sample_id, positions in duplicate_ids.items():
            position_text = "、".join(
                f"第{position}条"
                for position in positions
            )

            print(
                f"   ID={sample_id}重复，"
                f"出现位置：{position_text}"
            )
    else:
        print("   没有发现重复ID")

    print("\n4. 失败样本检测：")
    failed_cases = find_failed_cases(samples)

    if failed_cases:
        for sample in failed_cases:
            print(
                "   失败样本："
                f"id={sample.get('id')!r}，"
                f"category={sample.get('category')!r}，"
                f"input={sample.get('input')!r}，"
                f"expected={sample.get('expected')!r}"
            )
    else:
        print("   没有发现失败样本")

    print("\n5. category数量降序统计：")
    category_statistics = count_by_category(samples)

    for category, count in category_statistics:
        print(f"   {category}: {count}条")

    print("\nDay04任务代码运行完成。")


def main() -> None:
    """程序入口。"""
    print_report(EVALUATION_SAMPLES)


if __name__ == "__main__":
    main()
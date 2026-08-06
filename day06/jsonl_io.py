import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Union


REQUIRED_FIELDS = (
    "id",
    "input",
    "expected",
    "category",
)


def load_jsonl(
    file_path: Union[str, Path],
) -> List[Dict[str, Any]]:
    """
    读取 JSONL 评测数据。

    要求：
    1. 使用 UTF-8 编码；
    2. 每行必须是合法的 JSON 对象；
    3. 每条数据必须包含规定字段；
    4. 报错时必须显示文件名和行号。
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"文件不存在：{path.name}"
        )

    if not path.is_file():
        raise ValueError(
            f"目标路径不是文件：{path.name}"
        )

    records: List[Dict[str, Any]] = []

    with path.open(
        mode="r",
        encoding="utf-8",
    ) as file:
        for line_number, raw_line in enumerate(
            file,
            start=1,
        ):
            line = raw_line.strip()

            if not line:
                raise ValueError(
                    f"JSONL 读取失败：文件 {path.name}，"
                    f"line {line_number} 是空行"
                )

            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"JSONL 解析失败：文件 {path.name}，"
                    f"line {line_number}，"
                    f"column {error.colno}："
                    f"{error.msg}"
                ) from error

            if not isinstance(record, dict):
                raise ValueError(
                    f"JSONL 校验失败：文件 {path.name}，"
                    f"line {line_number} "
                    f"必须是 JSON 对象"
                )

            missing_fields = [
                field
                for field in REQUIRED_FIELDS
                if field not in record
            ]

            if missing_fields:
                missing_text = ", ".join(
                    missing_fields
                )

                raise ValueError(
                    f"JSONL 校验失败：文件 {path.name}，"
                    f"line {line_number} "
                    f"缺少字段：{missing_text}"
                )

            records.append(record)

    return records


def save_results_jsonl(
    results: Iterable[Dict[str, Any]],
    file_path: Union[str, Path],
) -> int:
    """
    把评测结果保存为 JSONL 文件。

    返回值是成功保存的结果数量。
    """
    path = Path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    saved_count = 0

    with path.open(
        mode="w",
        encoding="utf-8",
        newline="\n",
    ) as file:
        for result in results:
            if not isinstance(result, dict):
                raise TypeError(
                    "每条评测结果必须是字典"
                )

            json_text = json.dumps(
                result,
                ensure_ascii=False,
            )

            file.write(json_text + "\n")
            saved_count += 1

    return saved_count


def main() -> None:
    """
    Day06 最小运行演示。

    暂时让 prediction 等于 expected，
    用于验证数据读取和结果保存流程。
    """
    project_root = (
        Path(__file__).resolve().parent.parent
    )

    dataset_path = (
        project_root
        / "data"
        / "eval_dataset.jsonl"
    )

    result_path = (
        project_root
        / "outputs"
        / "day06_results.jsonl"
    )

    dataset = load_jsonl(dataset_path)

    results: List[Dict[str, Any]] = []

    for item in dataset:
        prediction = item["expected"]

        result = {
            "id": item["id"],
            "prediction": prediction,
            "expected": item["expected"],
            "category": item["category"],
            "exact_match": (
                prediction == item["expected"]
            ),
        }

        results.append(result)

    saved_count = save_results_jsonl(
        results=results,
        file_path=result_path,
    )

    print("=" * 60)
    print("Day06 JSONL 数据集运行成功")
    print("=" * 60)
    print(f"读取文件：{dataset_path.name}")
    print(f"读取数量：{len(dataset)} 条")
    print(f"保存数量：{saved_count} 条")
    print(f"结果位置：{result_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
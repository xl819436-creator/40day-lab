import json
from pathlib import Path

import pytest

from day06.jsonl_io import (
    REQUIRED_FIELDS,
    load_jsonl,
    save_results_jsonl,
)


PROJECT_ROOT = (
    Path(__file__).resolve().parent.parent
)

DATASET_PATH = (
    PROJECT_ROOT
    / "data"
    / "eval_dataset.jsonl"
)


def test_dataset_has_exactly_ten_records():
    records = load_jsonl(DATASET_PATH)

    assert len(records) == 10


def test_every_record_has_required_fields():
    records = load_jsonl(DATASET_PATH)

    for record in records:
        for field in REQUIRED_FIELDS:
            assert field in record


def test_chinese_text_uses_utf8():
    records = load_jsonl(DATASET_PATH)

    inputs = [
        record["input"]
        for record in records
    ]

    expected_answers = [
        record["expected"]
        for record in records
    ]

    assert "中国的首都是哪里？" in inputs
    assert "北京" in expected_answers
    assert "你好" in expected_answers


def test_invalid_json_reports_line_six(
    tmp_path,
):
    broken_file = (
        tmp_path
        / "broken_dataset.jsonl"
    )

    lines = []

    for number in range(1, 11):
        record = {
            "id": f"case-{number:03d}",
            "input": f"问题 {number}",
            "expected": f"答案 {number}",
            "category": "test",
        }

        lines.append(
            json.dumps(
                record,
                ensure_ascii=False,
            )
        )

    lines[5] = (
        '{"id":"case-006",'
        '"input":"损坏的数据",'
        '"expected":"答案",'
        '"category":"test}'
    )

    broken_file.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
    ) as error_info:
        load_jsonl(broken_file)

    error_message = str(
        error_info.value
    )

    assert "broken_dataset.jsonl" in error_message
    assert "line 6" in error_message


def test_save_results_keeps_chinese(
    tmp_path,
):
    output_file = (
        tmp_path
        / "results.jsonl"
    )

    results = [
        {
            "id": "case-001",
            "prediction": "北京",
            "expected": "北京",
            "exact_match": True,
        }
    ]

    saved_count = save_results_jsonl(
        results=results,
        file_path=output_file,
    )

    saved_text = output_file.read_text(
        encoding="utf-8",
    )

    assert saved_count == 1
    assert "北京" in saved_text
    assert "\\u5317" not in saved_text
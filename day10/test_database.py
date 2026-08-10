from pathlib import Path

from evalhub_core.database import (
    create_dataset,
    create_evaluation_job,
    create_evaluation_run,
    get_job,
    get_runs_by_job,
    init_database,
    list_table_names,
    update_job_progress,
)


def create_test_database_path(tmp_path: Path) -> Path:
    """为每个测试创建独立的临时数据库。"""
    return tmp_path / "test_evalhub.db"


def create_sample_job(database_path: Path) -> int:
    """创建一个包含3个测试用例的示例任务。"""
    dataset_id = create_dataset(
        name="Day10测试数据集",
        description="用于验证SQLite数据库关系",
        version="v1.0",
        file_path="data/eval_dataset.jsonl",
        database_path=database_path,
    )

    job_id = create_evaluation_job(
        dataset_id=dataset_id,
        name="MockProvider评测任务",
        provider_name="MockProvider",
        total_cases=3,
        status="running",
        database_path=database_path,
    )

    return job_id


def test_create_three_tables(tmp_path: Path) -> None:
    """实战一：验证三张核心表是否创建成功。"""
    database_path = create_test_database_path(tmp_path)

    init_database(database_path)

    table_names = list_table_names(database_path)

    assert table_names == [
        "datasets",
        "evaluation_jobs",
        "evaluation_runs",
    ]

    print("\n三张数据表创建成功：")

    for table_name in table_names:
        print(f"- {table_name}")


def test_one_job_has_three_runs(tmp_path: Path) -> None:
    """实战二：给一个job插入3个run并查询。"""
    database_path = create_test_database_path(tmp_path)

    init_database(database_path)
    job_id = create_sample_job(database_path)

    create_evaluation_run(
        job_id=job_id,
        case_name="case_001",
        prompt="1+1等于多少？",
        expected_output="2",
        actual_output="2",
        status="success",
        latency_ms=101.5,
        database_path=database_path,
    )

    create_evaluation_run(
        job_id=job_id,
        case_name="case_002",
        prompt="中国的首都是哪里？",
        expected_output="北京",
        actual_output="北京",
        status="success",
        latency_ms=120.8,
        database_path=database_path,
    )

    create_evaluation_run(
        job_id=job_id,
        case_name="case_003",
        prompt="请返回JSON对象。",
        expected_output='{"result": "ok"}',
        actual_output=None,
        status="pending",
        latency_ms=None,
        database_path=database_path,
    )

    runs = get_runs_by_job(
        job_id=job_id,
        database_path=database_path,
    )

    assert len(runs) == 3

    for run in runs:
        assert run["job_id"] == job_id

    print(f"\njob_id={job_id}对应{len(runs)}条run记录：")

    for run in runs:
        print(
            f"run_id={run['id']}, "
            f"case_name={run['case_name']}, "
            f"status={run['status']}"
        )


def test_update_job_progress_to_two_of_three(
    tmp_path: Path,
) -> None:
    """实战三：把任务进度更新为2/3并查询验证。"""
    database_path = create_test_database_path(tmp_path)

    init_database(database_path)
    job_id = create_sample_job(database_path)

    update_job_progress(
        job_id=job_id,
        completed_cases=2,
        status="running",
        database_path=database_path,
    )

    job = get_job(
        job_id=job_id,
        database_path=database_path,
    )

    assert job is not None
    assert job["completed_cases"] == 2
    assert job["total_cases"] == 3
    assert job["status"] == "running"

    print(
        f"\n任务进度更新成功："
        f"{job['completed_cases']}/{job['total_cases']}"
    )
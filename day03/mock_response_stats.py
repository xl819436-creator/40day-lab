# 程序能够明确识别的四种状态
KNOWN_STATUS_ORDER = (
    "success",
    "timeout",
    "429",
    "500"
)

KNOWN_STATUSES = set(KNOWN_STATUS_ORDER)

# 最终统计时包含unknown分类
CATEGORY_ORDER = (
    "success",
    "timeout",
    "429",
    "500",
    "unknown"
)


def create_mock_responses():
    """
    创建模拟接口响应。

    前10条为正常的四类状态，
    第11条故意使用未知状态bad_status。
    """
    responses = [
        {"id": "request_001", "status": "success"},
        {"id": "request_002", "status": "success"},
        {"id": "request_003", "status": "timeout"},
        {"id": "request_004", "status": "success"},
        {"id": "request_005", "status": "429"},
        {"id": "request_006", "status": "success"},
        {"id": "request_007", "status": "500"},
        {"id": "request_008", "status": "timeout"},
        {"id": "request_009", "status": "success"},
        {"id": "request_010", "status": "429"},
        {"id": "request_011", "status": "bad_status"}
    ]

    return responses


def validate_response_structure(responses):
    """
    校验响应的基本结构。

    注意：
    本函数只检查数据结构，不拒绝未知状态。
    未知状态会在统计时归入unknown。
    """
    if not isinstance(responses, list):
        raise TypeError("响应数据必须是列表。")

    response_ids = []

    for index, response in enumerate(responses, start=1):
        if not isinstance(response, dict):
            raise TypeError(
                f"第{index}条响应必须是字典。"
            )

        if "id" not in response:
            raise ValueError(
                f"第{index}条响应缺少id字段。"
            )

        if "status" not in response:
            raise ValueError(
                f"第{index}条响应缺少status字段。"
            )

        response_id = response["id"]

        if not isinstance(response_id, str):
            raise TypeError(
                f"第{index}条响应的id必须是字符串。"
            )

        if response_id.strip() == "":
            raise ValueError(
                f"第{index}条响应的id不能为空。"
            )

        response_ids.append(response_id)

    if len(response_ids) != len(set(response_ids)):
        raise ValueError("响应ID存在重复。")

    return True


def classify_status(status):
    """
    对响应状态进行分类。

    已知状态保持不变；
    其他状态全部归入unknown。
    """
    if status in KNOWN_STATUSES:
        return status

    return "unknown"


def calculate_statistics(responses):
    """
    遍历响应并完成统计。

    支持：
    1. 四种已知状态
    2. 未知状态归入unknown
    3. 空列表成功率为0.0
    """
    status_counts = {
        category: 0
        for category in CATEGORY_ORDER
    }

    failure_ids = []
    unknown_responses = []

    for response in responses:
        original_status = response["status"]
        category = classify_status(original_status)

        status_counts[category] += 1

        if category != "success":
            failure_ids.append(response["id"])

        if category == "unknown":
            unknown_responses.append(
                {
                    "id": response["id"],
                    "original_status": original_status
                }
            )

    total_responses = len(responses)
    success_count = status_counts["success"]

    if total_responses == 0:
        success_rate = 0.0
    else:
        success_rate = (
            success_count / total_responses
        ) * 100

    statistics = {
        "total": total_responses,
        "status_counts": status_counts,
        "success_rate": success_rate,
        "failure_ids": failure_ids,
        "unknown_responses": unknown_responses
    }

    return statistics


def validate_statistics(statistics):
    """
    校验所有分类数量之和是否等于总数。
    """
    category_total = sum(
        statistics["status_counts"].values()
    )

    response_total = statistics["total"]

    if category_total != response_total:
        raise ValueError(
            "分类数量校验失败："
            f"分类数量之和为{category_total}，"
            f"响应总数为{response_total}。"
        )

    return True


def print_report(statistics, report_title):
    """
    输出统计报告。
    """
    status_counts = statistics["status_counts"]
    failure_ids = statistics["failure_ids"]
    unknown_responses = statistics["unknown_responses"]

    category_total = sum(status_counts.values())

    print("=" * 60)
    print(report_title)
    print("=" * 60)
    print(f"响应总数：{statistics['total']}")
    print(f"success数量：{status_counts['success']}")
    print(f"timeout数量：{status_counts['timeout']}")
    print(f"429数量：{status_counts['429']}")
    print(f"500数量：{status_counts['500']}")
    print(f"unknown数量：{status_counts['unknown']}")
    print(f"分类数量之和：{category_total}")
    print(f"成功率：{statistics['success_rate']:.2f}%")
    print(f"失败数量：{len(failure_ids)}")

    if failure_ids:
        print(f"失败ID：{', '.join(failure_ids)}")
    else:
        print("失败ID：无")

    if unknown_responses:
        print("未知状态详情：")

        for response in unknown_responses:
            print(
                f"  ID={response['id']}，"
                f"原始状态={response['original_status']}"
            )
    else:
        print("未知状态详情：无")

    print("分类数量校验：通过")
    print("=" * 60)


def main():
    # 实战1：包含bad_status的模拟响应
    responses = create_mock_responses()

    validate_response_structure(responses)

    statistics = calculate_statistics(responses)

    validate_statistics(statistics)

    print_report(
        statistics,
        "包含未知状态的模拟响应统计报告"
    )

    print()

    # 实战2：空列表统计
    empty_responses = []

    validate_response_structure(empty_responses)

    empty_statistics = calculate_statistics(
        empty_responses
    )

    validate_statistics(empty_statistics)

    print_report(
        empty_statistics,
        "空列表统计报告"
    )


if __name__ == "__main__":
    main()
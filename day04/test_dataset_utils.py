import unittest

from day04.dataset_utils import (
    EVALUATION_SAMPLES,
    REQUIRED_FIELDS,
    count_by_category,
    find_duplicate_ids,
    find_failed_cases,
    group_by_category,
)


class TestDatasetUtils(unittest.TestCase):
    """自动检查Day04图片中的编程任务是否全部完成。"""

    def test_samples_are_stored_in_list(self):
        """检查所有样本是否使用list保存。"""
        self.assertIsInstance(EVALUATION_SAMPLES, list)

    def test_sample_count_is_12(self):
        """检查是否正好有12条评测样本。"""
        self.assertEqual(len(EVALUATION_SAMPLES), 12)

    def test_every_sample_is_dictionary(self):
        """检查每条样本是否都是dict。"""
        for sample in EVALUATION_SAMPLES:
            self.assertIsInstance(sample, dict)

    def test_every_sample_has_required_fields(self):
        """检查每条样本是否都有4个必要字段。"""
        for sample in EVALUATION_SAMPLES:
            self.assertTrue(
                REQUIRED_FIELDS.issubset(sample.keys()),
                msg=f"样本缺少必要字段：{sample}",
            )

    def test_group_by_category(self):
        """检查group_by_category分组是否正确。"""
        grouped = group_by_category(EVALUATION_SAMPLES)

        self.assertEqual(len(grouped["math"]), 4)
        self.assertEqual(len(grouped["general"]), 3)
        self.assertEqual(len(grouped["python"]), 3)
        self.assertEqual(len(grouped["translation"]), 2)

    def test_find_all_duplicate_positions(self):
        """检查是否找到重复ID的全部位置。"""
        duplicate_ids = find_duplicate_ids(EVALUATION_SAMPLES)

        self.assertEqual(
            duplicate_ids,
            {
                3: [3, 11],
            },
        )

    def test_find_failed_cases(self):
        """检查是否能找到expected为空的失败样本。"""
        failed_cases = find_failed_cases(EVALUATION_SAMPLES)

        self.assertEqual(len(failed_cases), 1)
        self.assertEqual(failed_cases[0]["id"], 12)
        self.assertEqual(failed_cases[0]["expected"], "")

    def test_category_count_is_descending(self):
        """检查分类结果是否按照样本数量降序排列。"""
        statistics = count_by_category(EVALUATION_SAMPLES)

        self.assertEqual(
            statistics,
            [
                ("math", 4),
                ("general", 3),
                ("python", 3),
                ("translation", 2),
            ],
        )

        counts = [
            count
            for _, count in statistics
        ]

        self.assertEqual(
            counts,
            sorted(counts, reverse=True),
        )

    def test_functions_do_not_modify_original_samples(self):
        """检查函数是否意外修改原始数据。"""
        samples_before = [
            sample.copy()
            for sample in EVALUATION_SAMPLES
        ]

        group_by_category(EVALUATION_SAMPLES)
        find_duplicate_ids(EVALUATION_SAMPLES)
        find_failed_cases(EVALUATION_SAMPLES)
        count_by_category(EVALUATION_SAMPLES)

        self.assertEqual(
            EVALUATION_SAMPLES,
            samples_before,
        )


if __name__ == "__main__":
    unittest.main()

from decimal import Decimal, InvalidOperation


def get_non_negative_integer(prompt):
    """
    获取一个大于等于 0 的整数。
    主要用于接收 Token 数量。
    """
    while True:
        user_input = input(prompt).strip()

        try:
            value = int(user_input)

            if value < 0:
                print("输入错误：Token 数量不能是负数，请重新输入。")
                continue

            return value

        except ValueError:
            print("输入错误：Token 数量必须是整数，例如 1000。")


def get_non_negative_decimal(prompt):
    """
    获取一个大于等于 0 的小数。
    主要用于接收模型单价。
    """
    while True:
        user_input = input(prompt).strip()

        try:
            value = Decimal(user_input)

            if value < 0:
                print("输入错误：模型单价不能是负数，请重新输入。")
                continue

            return value

        except InvalidOperation:
            print("输入错误：模型单价必须是数字，例如 0.002。")


def calculate_cost(
    input_tokens,
    output_tokens,
    input_price,
    output_price
):
    """
    计算模型调用成本。

    单价单位：元 / 1000 Tokens
    """
    token_unit = Decimal("1000")

    input_cost = (
        Decimal(input_tokens) / token_unit
    ) * input_price

    output_cost = (
        Decimal(output_tokens) / token_unit
    ) * output_price

    total_cost = input_cost + output_cost

    return input_cost, output_cost, total_cost


def main():
    print("=" * 50)
    print("LLM Token 成本计算器")
    print("单价单位：元 / 1000 Tokens")
    print("=" * 50)

    input_tokens = get_non_negative_integer(
        "请输入输入 Token 数量："
    )

    output_tokens = get_non_negative_integer(
        "请输入输出 Token 数量："
    )

    input_price = get_non_negative_decimal(
        "请输入输入单价（元/千 Tokens）："
    )

    output_price = get_non_negative_decimal(
        "请输入输出单价（元/千 Tokens）："
    )

    input_cost, output_cost, total_cost = calculate_cost(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        input_price=input_price,
        output_price=output_price
    )

    print("\n计算结果")
    print("-" * 50)
    print(f"输入 Token 数量：{input_tokens}")
    print(f"输出 Token 数量：{output_tokens}")
    print(f"输入成本：{input_cost:.6f} 元")
    print(f"输出成本：{output_cost:.6f} 元")
    print(f"总成本：{total_cost:.6f} 元")
    print("-" * 50)


if __name__ == "__main__":
    main()
import pytest
from coinchange import CoinChange


@pytest.mark.parametrize(
    "setting",
    [
        ['£0-5', 3],
        ['£0-50', 225],
        ['£2-', 36840],
        ['£10-', ?], # TODO: run for £10
        ['£100-', ?], # TODO: run for £100
    ]
)
def test_setting(setting):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    odd_changed_ways = CoinChange(coins=coins, amount=setting[0])

    assert odd_changed_ways.coin_change_solutions() == setting[1]

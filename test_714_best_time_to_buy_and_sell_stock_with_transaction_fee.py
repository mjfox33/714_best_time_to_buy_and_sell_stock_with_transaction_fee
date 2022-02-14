import code_714_best_time_to_buy_and_sell_stock_with_transaction_fee as c

def test_example_1():
    s = c.Solution()
    assert s.maxProfit([1,3,2,8,4,9], 2 ) == 8

def test_example_2():
    s = c.Solution()
    assert s.maxProfit([1,3,7,5,10,3], 3) == 6
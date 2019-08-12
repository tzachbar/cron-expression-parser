from cron_parser import CronExpressionParser


def test_all_asterisk():

    expected_result = {
        'minute':           set(range(60)),     # 0 - 59
        'hour':             set(range(24)),     # 0 - 23
        'days_of_month':    set(range(1,32)),   # 1 - 31
        'months':           set(range(1,13)),   # 1 - 12
        'days_of_week':     set(range(7)),      # 0 - 6
    }

    cron_parser = CronExpressionParser(['*', '*', '*', '*', '*', 'test'])
    cron_parser.parse()

    assert cron_parser.parsed_elements == expected_result



def test_comma_range_step():

    expected_result = {
        'minute':           {1,7,8},
        'hour':             set(range(3,18)),
        'days_of_month':    set(range(5,32,3)),
        'months':           {1,4,5,6,7,8},
        'days_of_week':     set(range(0,7,2)),
    }

    cron_parser = CronExpressionParser(['1,7,8', '3-17', '5-31/3', '1,4-8', '*/2', 'test'])
    cron_parser.parse()

    assert cron_parser.parsed_elements == expected_result

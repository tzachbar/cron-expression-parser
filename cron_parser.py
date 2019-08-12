import sys
import collections


class CronExpressionParser:

    all_values = collections.OrderedDict({
        'minute':           set(range(60)),     # 0 - 59
        'hour':             set(range(24)),     # 0 - 23
        'days_of_month':    set(range(1, 32)),   # 1 - 31
        'months':           set(range(1, 13)),   # 1 - 12
        'days_of_week':     set(range(7)),      # 0 - 6
    })

    def __init__(self, cron_str_elements):

        self.cron_str_elements = cron_str_elements

        if len(self.cron_str_elements) < 6:
            raise ValueError('Malformed input, please insert cron expression (5 values seperated by spaces) followed by a command to run')

        self.parsed_elements = {}
        self.command = self.cron_str_elements.pop()


    def parse(self):

        key_names = list(CronExpressionParser.all_values.keys())   # [minute, hour, days_of_month, months, days_of_week]

        for i, cron_str_element in enumerate(self.cron_str_elements):
            curr_key = key_names[i]
            self.parsed_elements[curr_key] = self.__parse_expression(cron_str_element, CronExpressionParser.all_values[curr_key])


    def __parse_expression(self, expression, all_options):
        """
        split cron expression by comma, and parse each part separately
        if no '/' character exists, we can assume step function of 1 (as if we had '/1' at the end of expression)
        then we look at each of the expressions and aggregate the results in a set which will drop duplications
        """

        aggregated = set()

        try:
            for e in expression.split(','):

                step = 1
                if '/' in e:
                    e, step = e.split('/')
                    step = int(step)

                if e == '*':
                    start, end = min(all_options), max(all_options)

                elif '-' in e:
                    start, end = e.split('-')
                    start, end = int(start), int(end)

                else:   # simple int
                    start, end = int(e), int(e)

                e = set(range(start, end + 1, step))

                aggregated = aggregated.union(e)

        except ValueError:
            raise ValueError("Expression: '" + str(expression) + "' is invalid!")

        if not aggregated.issubset(all_options):
            raise ValueError("Expression: '" + expression + "' numbers are out of bounds!")

        return aggregated


def print_table(elements, command):

    for name, value in elements.items():
        spaces = '\t\t\t'
        if name in ['days_of_month', 'days_of_week']:       # smaller space for longer name
            spaces = '\t'
        print(name + spaces + ' '.join(map(str, list(value))))

    print('command\t\t\t' + command)



def main(cron_str_elements):
    try:
        cron_parser = CronExpressionParser(cron_str_elements)
        cron_parser.parse()
        print_table(cron_parser.parsed_elements, cron_parser.command)
    except ValueError as e:
        print("An Error occured, " + str(e))


if __name__ == "__main__":

    if len(sys.argv) < 7:
        print('Malformed input, please pass cron expression (5 values seperated by spaces followed by a command) as a parameter. e.g. 2,3 22 * 1-5 * pwd')

    main(sys.argv[1:7])

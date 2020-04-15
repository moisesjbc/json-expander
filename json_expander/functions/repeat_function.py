
class RepeatFunction:
    """
    JSON expander function. Repeats the given body a given number of times. Usage

        ["@repeat", <n>, <body>]

    where

        - (Integer) <n>:      Number of repetitions
        - (JSON)    <body>:   Body to be repeated

    Sample input

        ["@repeat", 3, {"foo": "bar"}]

    Sample output

        [{"foo": "bar"}, {"foo": "bar"}, {"foo": "bar"}]
    """
    @staticmethod
    def name():
        return 'repeat'

    def run(self, args):
        n_iterations = int(args[0])
        body = args[1]

        result = []
        for i in range(0, n_iterations):
            result.append(body)

        return result

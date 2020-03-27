import json
import argparse
from json_expander.json_dict_expander import JsonDictExpander
from json_expander.context import Context


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument('--var', action='append')
    args = parser.parse_args()

    context = Context()
    for var_def in args.var:
        [var, value] = var_def.split('=')
        context.set_var(var, value)

    with open(args.input_file, 'r') as input_file:
        with open(args.output_file, 'w') as output_file:
            json_expander = JsonDictExpander()
            src_json = json.load(input_file)
            dst_json = json_expander.expand(src_json, context)
            json.dump(dst_json, output_file)

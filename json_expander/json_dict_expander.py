from json_expander.context import Context
from json_expander.functions import functions


class JsonDictExpander:
    def __init__(self):
        self._functions = {function.name(): function() for function in functions()}

    def expand(self, json, context=None):
        if context is None:
            context = Context()

        if isinstance(json, dict):
            return {self.expand(key, context): self.expand(json[key], context) for key in json}
        elif isinstance(json, list):
            if len(json) and isinstance(json[0], str) and json[0].startswith("@"):
                return self._functions[json[0][1:]].run([self.expand(value, context) for value in json[1:]])
            else:
                return [self.expand(value, context) for value in json]
        elif isinstance(json, str):
            if json.startswith("$"):
                return context.get_var(json[1:], json)
            else:
                return json
        else:
            return json

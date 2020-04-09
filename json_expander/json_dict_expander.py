from json_expander.context import Context


class JsonDictExpander:
    def expand(self, json, context=None):
        if context is None:
            context = Context()

        if isinstance(json, dict):
            return {self.expand(key, context): self.expand(json[key], context) for key in json}
        elif isinstance(json, list):
            return [self.expand(value, context) for value in json]
        elif isinstance(json, str):
            if json.startswith("$"):
                return context.get_var(json[1:], json)
            else:
                return json
        else:
            return json

class Context:
    def __init__(self):
        self._vars = {}

    def set_var(self, key, value):
        self._vars[key] = value

    def get_var(self, key, default=None):
        return self._vars.get(key, default)

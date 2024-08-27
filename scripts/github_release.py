import json
import os
from rich.table import Table
from rich import print
from rich.console import Console


class GitHub_Release:
    def __init__(self):
        self.script_path = os.path.abspath(__file__)
        self.cwd = os.path.dirname(self.script_path)
        self.file_path = os.path.abspath(os.path.join(self.cwd, "..", "metadata.json"))

    def load(self):
        with open(self.file_path, "r") as f:
            data = json.load(f)
        return data

    def get(self, arg, subarg=None):
        data = self.load()
        if isinstance(arg, list) and subarg is None:
            required_value = [data[x] for x in arg]
        elif isinstance(arg, str) and subarg is None:
            required_value = data[arg]
        elif subarg:
            required_value = data[arg][subarg]
        return required_value

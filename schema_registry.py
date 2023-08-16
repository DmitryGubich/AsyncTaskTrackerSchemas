import json
from pathlib import Path

import jsonschema
from jsonschema import validate


class SchemaRegistry:
    @staticmethod
    def validate_event(event, body, version):
        domain, event_type = event.split(".")
        schema_location = (
            Path(__file__).absolute().parent / f"{domain}/{event_type}/{version}.json"
        )
        with open(schema_location) as file:
            schema = json.load(file)
            validate(instance=body, schema=schema)
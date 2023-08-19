import json
from pathlib import Path

from jsonschema import validate


class SchemaRegistry:
    @staticmethod
    def validate_event(event, body, version):
        domain, event_type = event.split(".")
        schema_location = (
            Path(__file__).absolute().parent
            / f"schemas/schemas/{domain}/{event_type}/{version}.json"
        )
        with open(schema_location) as file:
            schema = json.load(file)
            validate(instance=body, schema=schema)

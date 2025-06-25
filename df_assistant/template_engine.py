from typing import Any, Dict
from jinja2 import Template


def render_template(template_str: str, context: Dict[str, Any]) -> str:
    template = Template(template_str)
    return template.render(**context)

"""Utility for rendering answer templates."""

from typing import Any, Dict
from jinja2 import Template
import pandas as pd


def render_template(template_str: str, context: Dict[str, Any]) -> str:
    """Render a Jinja2 template with the given context.

    The context may include scalars, lists, or pandas objects. DataFrames are
    passed directly so templates can iterate over ``result`` or call methods
    such as ``to_markdown``.
    """

    # Convert Series to list for convenience
    for key, value in list(context.items()):
        if isinstance(value, pd.Series):
            context[key] = value.tolist()

    template = Template(template_str)
    return template.render(**context)

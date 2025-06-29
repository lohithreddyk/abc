import json
from typing import Dict

TEMPLATES_FILE = "templates.json"


def load_templates() -> Dict[str, str]:
    """Return a dictionary of template_name -> template_string."""
    try:
        with open(TEMPLATES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_templates(templates: Dict[str, str]):
    with open(TEMPLATES_FILE, "w") as f:
        json.dump(templates, f, indent=2)


def add_or_update_template(name: str, template: str):
    templates = load_templates()
    templates[name] = template
    save_templates(templates)


def delete_template(name: str):
    templates = load_templates()
    if name in templates:
        templates.pop(name)
        save_templates(templates)

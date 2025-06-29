import json
from typing import Dict, Any, List

TEST_FILE = "tests.json"


def load_tests() -> List[Dict[str, Any]]:
    try:
        with open(TEST_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tests(tests: List[Dict[str, Any]]):
    with open(TEST_FILE, "w") as f:
        json.dump(tests, f, indent=2)


def add_test(test: Dict[str, Any]):
    tests = load_tests()
    tests.append(test)
    save_tests(tests)


def update_test(index: int, test: Dict[str, Any]):
    tests = load_tests()
    if 0 <= index < len(tests):
        tests[index] = test
        save_tests(tests)


def delete_test(index: int):
    tests = load_tests()
    if 0 <= index < len(tests):
        tests.pop(index)
        save_tests(tests)


def duplicate_test(index: int):
    tests = load_tests()
    if 0 <= index < len(tests):
        tests.append(tests[index].copy())
        save_tests(tests)

"""
Approvals configuration example

Based on:
- https://github.com/approvals/ApprovalTests.Python
- https://github.com/approvals/ApprovalTests.Python/blob/master/docs/configuration.md

Collect reporters in reporters.json, i.e. every user adds
their diff tool. If none found, fall back to PythonNative
and notify user.
"""
import pytest
from approvaltests import set_default_reporter
from approvaltests.reporters import PythonNativeReporter
from approvaltests.reporters.generic_diff_reporter_factory import \
    GenericDiffReporterFactory


@pytest.fixture(scope="session", autouse=True)
def configure_approvaltests():
    factory = GenericDiffReporterFactory()
    factory.load("reporters.json")  # every user adds path to diff tool
    first_working = factory.get_first_working()
    if not first_working:
        print(
            "Review reporters.json and/or install a diff."
            "Falling back to native reporter."
        )
        first_working = PythonNativeReporter()

    set_default_reporter(first_working)

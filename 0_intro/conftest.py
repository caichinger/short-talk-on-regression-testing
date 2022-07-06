import pickle
from pathlib import Path


def assert_that_it_does_not_change(obj):
    file = Path("important.pickle")
    if not file.exists():
        _dump(obj, file)
        assert False, "Writing new file... Cannot assert if result has changed."

    saved_obj = _load(file)
    assert obj == saved_obj


def _load(file):
    with open(file, "rb") as f:
        saved_obj = pickle.load(f)
    return saved_obj


def _dump(obj, file):
    with open(file, "wb") as f:
        pickle.dump(obj, f)

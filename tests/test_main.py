import pytest
from unittest.mock import patch

from bbqbalance.main import BBQApp

class MockSettings:
    pass

@pytest.fixture
def mock_settings():
    with patch("bbqbalance.main.settings", new=MockSettings):
        yield

def test_main():
    app = BBQApp()
    assert True
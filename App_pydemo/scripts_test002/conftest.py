import pytest

# 优先级最高
@pytest.fixture()
def init_data():
    return 123
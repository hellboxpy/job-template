from unittest.mock import MagicMock

from hellbox.jobs.{{name}} import DoSomething


class TestDoSomething:
    def test_init(self):
        assert DoSomething()

    def test_process(self):
        file = MagicMock()
        copy = MagicMock()
        file.copy.return_value = copy

        result = DoSomething().process(file)

        assert result is copy

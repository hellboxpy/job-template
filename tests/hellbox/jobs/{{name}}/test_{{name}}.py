from hellbox.source_file import SourceFile
from hellbox.jobs.{{name}} import DoSomething


class TestDoSomething(object):
    def test_init(self):
        assert DoSomething()

    def test_run_without_files(self):
        assert DoSomething().run([]) == []

    def test_run(self):
        source = SourceFile("./source", "./content")

        result = DoSomething().run([source])

        assert result == [source]
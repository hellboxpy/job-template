from hellbox import Chute, Hellbox


class DoSomething(Chute):
    """DoSomething does something to each file."""

    def run(self, files):
        return [self._process(file) for file in files]

    def _process(self, file):
        Hellbox.info(f"Doing something: {file.basename}")
        return file

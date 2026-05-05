from hellbox import Chute, Hellbox


class DoSomething(Chute):
    """DoSomething does something to each file."""

    def process(self, file):
        Hellbox.info(f"Doing something: {file.name}")
        copy = file.copy()
        # TODO: modify copy
        return copy

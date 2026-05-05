# hellbox-{{name}}

A [hellbox](https://github.com/hellboxpy/hellbox) plugin that does something.

## Usage

```python
from hellbox import Hellbox
from hellbox.jobs.{{name}} import DoSomething

with Hellbox("build") as task:
    task.read("source/*") >> DoSomething() >> task.write("output")
```

## Installation

```sh
pip install hellbox-{{name}}
```

## Development

```sh
uv pip install -e .
pytest tests
```

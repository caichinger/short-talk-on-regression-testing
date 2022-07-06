# Creating and maintaining useful regression tests - with ease?

Talk at [Django Vienna 07/2022](https://www.meetup.com/django-vienna/events/286539435/)

If you want to discuss testing & design related topics, feel free to reach out (see slides)!

*Please keep in mind that these slides/notes were developed to facilitate a talk
with a live demo and are not indented to serve as standalone resources.*

## Abstract

Implementing tests and keeping them up to date can be a cumbersome task.
Not only but in particular if non-trivial data structures are involved.
Let's see what we can do to simplify matters and maybe even improve
test-feedback.

## Links

Related links:
- https://github.com/approvals/ApprovalTests.Python
  - https://github.com/approvals/ApprovalTests.Python.PytestPlugin
- https://github.com/ESSS/pytest-regressions
- https://github.com/kevin1024/vcrpy
- ...

## Environment

Create environment:

```console
conda env create -f environment.yml
conda activate demo
```

## Commands

Run tests:

```console
# from within one of the numbered directories
pytest
```

Format code:

```
black .
isort .
```

Build slides:

```console
npx @marp-team/marp-cli@latest --allow-local-files slides.md -o slides.pdf89:
```

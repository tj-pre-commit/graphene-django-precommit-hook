![Upload Python Package](https://github.com/jackton1/graphene-django-precommit-hook/workflows/Upload%20Python%20Package/badge.svg)
# graphene-django-precommit-hook
pre-commit hook to generate `.graphql` | `.json` graphql schema for [graphene-django](https://github.com/graphql-python/graphene-django).


## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions


Sample basic `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/jackton1/graphene-django-precommit-hook
    rev: v0.1.0
    hooks:
      - id: graphene-django-hook
        stages: [commit]
```


Sample complex `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/jackton1/graphene-django-precommit-hook
    rev: v0.1.0
    hooks:
      - id: graphene-django-hook
        stages: [commit]
        args: [
          '--managepy-path',
          '/path/to/manage.py', # Defaults to: manage.py
          '--settings',
          'project.settings'. # Defaults to: DJANGO_SETTINGS_MODULE
          '--indent',
          '4' # See https://docs.graphene-python.org/projects/django/en/latest/introspection/
          '--out',
          'path/to/schema.graphql',
          '--schema',
          'module.path.to.schema',
          '--verbosity', # OR '-v'
          '2', # Set the verbosity level {0,1,2,3}
        ]
```

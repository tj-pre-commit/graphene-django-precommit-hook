# graphene-django-precommit-hook
[pre-commit](https://pre-commit.com) hook to generate `.graphql` | `.json` graphql schema for [graphene-django](https://github.com/graphql-python/graphene-django).


## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions


Sample basic `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/tj-pre-commit/graphene-django-precommit-hook
    rev: v0.1.0
    hooks:
      - id: graphene-django-hook
        stages: [commit]
```


Sample complex `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/tj-pre-commit/graphene-django-precommit-hook
    rev: v0.1.0
    hooks:
      - id: graphene-django-hook
        stages: [commit]
        args: [
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

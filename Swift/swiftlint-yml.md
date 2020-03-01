# Swiftlint yaml file `swiftlint.yml`

```yaml
excluded: # paths to ignore during linting. Takes precedence over `included`.
  - Carthage
  - Pods
identifier_name:
  min_length: # only min_length
    error: 3 # only error
  excluded: # excluded via string array
    - id
    - URL
    - GlobalAPIKey
    - i
    - j
line_length:
  warning: 150
  ignores_function_declarations: true
  ignores_comments: true
  ignores_interpolated_strings: true
  ignores_urls: true
disabled_rules:
   - multiple_closures_with_trailing_closure

```

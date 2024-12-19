# GitHub Action Static Security Scan Analysis

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

GitHub Action that scans code changes and reports security findings on pull requests.
<!-- action-docs-description source="action.yaml" -->

<!-- action-docs-usage source="action.yaml" -->
## Usage

```yaml
- uses: @
  with:
    checkout-repo:
    # Perform checkout as the first step
    #
    # Required: false
    # Default: true

    semgrep-app-token:
    # Semgrep API token for fetching rule configurations.
    #
    # Required: true
    # Default: ""
```
<!-- action-docs-usage source="action.yaml" -->

<!-- prettier-ignore-end -->

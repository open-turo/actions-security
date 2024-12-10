# GitHub Action Static Security Scan Analysis

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

GitHub Action that scans code changes being made and posts security findings in form of comments on pull requests
<!-- action-docs-description source="action.yaml" -->

<!-- action-docs-usage source="action.yaml" -->
## Usage

```yaml
- uses: @
  with:
    checkout-repo:
    # Perform checkout as first step
    #
    # Required: false
    # Default: true

    semgrep-app-token:
    # SemGrep API token to be added to repo that allows pulling the latest rule config from ruleboard in Semgrep UI
    #
    # Required: true
    # Default: ""
```
<!-- action-docs-usage source="action.yaml" -->

<!-- prettier-ignore-end -->

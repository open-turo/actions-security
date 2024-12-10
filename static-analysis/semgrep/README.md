# GitHub Action Static Security Scan Analysis

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

Github Action that scans code changes being made and posts security findings in form of comments on pull requests
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
    # SemGrep API token to pull the latest rule configuration from Semgrep's ruleboard
    #
    # Required: true
    # Default: ""
```
<!-- action-docs-usage source="action.yaml" -->

<!-- prettier-ignore-end -->

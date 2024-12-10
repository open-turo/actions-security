# GitHub Action Static Security Scan Analysis

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

GitHub Action that scans code changes being made and posts security findings in the form of comments on pull requests
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
    # Semgrep API token to be added to the repo that allows pulling the latest rule config from the ruleboard in the Semgrep UI
    #
    # Required: true
    # Default: ""

    github-token:
    # GitHub token that can checkout the repository. e.g. 'secrets.GITHUB_TOKEN'
    #
    # Required: true
    # Default: ""
```
<!-- action-docs-usage source="action.yaml" -->

<!-- prettier-ignore-end -->

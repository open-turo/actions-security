# GitHub Action Static Security Scan Analysis

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

GitHub Action that scans code changes being made and posts security findings as comments on pull requests.
<!-- action-docs-description source="action.yaml" -->

<!-- action-docs-usage source="action.yaml" -->
## Usage

```yaml
- uses: @
  with:
    semgrep-app-token:
    # Semgrep API token to pull the latest rule configuration from the ruleboard in Semgrep UI.
    #
    # Required: true
    # Default: ""

    scan-mode:
    # Scan mode: "ci" for context-aware scanning (default), "scan" for full repository scans
    #
    # Required: false
    # Default: ci

    semgrep-version:
    # Semgrep version to use. Minimum 1.111.0 recommended for malicious dependency detection, 1.147.0 (latest) for optimal performance
    #
    # Required: false
    # Default: 1.147.0
```
<!-- action-docs-usage source="action.yaml" -->

<!-- prettier-ignore-end -->

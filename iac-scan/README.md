# GitHub Action IaC Security Scan

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

Scans IaC files for security misconfigurations using Wiz CLI with CIS Benchmark Enforcement
<!-- action-docs-description source="action.yaml" -->

<!-- action-docs-usage source="action.yaml" -->
## Usage

```yaml
- uses: @
  with:
    scan-path:
    # Path to scan for IaC files
    #
    # Required: false
    # Default: .

    wiz-client-id:
    # Wiz Client ID for service account authentication
    #
    # Required: true
    # Default: ""

    wiz-client-secret:
    # Wiz Client Secret for service account authentication
    #
    # Required: true
    # Default: ""

    policy:
    # Wiz policy to use for scanning
    #
    # Required: false
    # Default: CIS Benchmark Enforcement

    scan-types:
    # Narrow scan to specific IaC types (Terraform, CloudFormation, Kubernetes, Dockerfile, Ansible)
    #
    # Required: false
    # Default: ""

    enable-secrets-scan:
    # Enable secrets scanning
    #
    # Required: false
    # Default: true

    policy-hits-only:
    # Only show findings that violate the policy
    #
    # Required: false
    # Default: false

    output-format:
    # Output format (human, json, sarif)
    #
    # Required: false
    # Default: human

    fail-on-findings:
    # Fail the action if security issues are found
    #
    # Required: false
    # Default: false

    tags:
    # Tags to mark the scan with (KEY=VALUE format, comma-separated)
    #
    # Required: false
    # Default: ""

    timeout:
    # Scan timeout duration
    #
    # Required: false
    # Default: 10m
```
<!-- action-docs-usage source="action.yaml" -->
<!-- prettier-ignore-end -->

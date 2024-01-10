# GitHub Action Container-Scan

<!-- prettier-ignore-start -->
<!-- action-docs-description -->
## Description

GitHub Action for scanning container image for vulnerabilities using Lacework
<!-- action-docs-description -->
<!-- prettier-ignore-end -->

## Usage

To use this action in your GitHub Actions workflow, include the following steps:

```yaml
- name: Lacework Container Scan
  uses: open-turo/actions-security/container-scan@v1 # Specify the path to the action in your repository
  with:
    lw-account-name: ${{ secrets.LW_ACCOUNT_NAME }}
    lw-access-token: ${{ secrets.LW_ACCESS_TOKEN }}
    github-token: <your-secret-for-github-token>
    image-tag: <your-docker-image-tag>
```

<!-- prettier-ignore-start -->
<!-- action-docs-inputs -->
## Inputs

| parameter | description | required | default |
| --- | --- | --- | --- |
| docker-config-file | Path to the docker config file (defaults to .docker-config.json) Must contain imageName, may contain dockerfile | `false` | .docker-config.json |
| github-token | GitHub token | `true` |  |
| lw-account-name | Lacework account name | `true` |  |
| lw-access-token | Lacework access token | `true` |  |
| image-tag | Docker image tag | `true` |  |
<!-- action-docs-inputs -->

<!-- action-docs-outputs -->
## Outputs

| parameter | description |
| --- | --- |
| comment-id | Comment ID of the test report |
| image-name | Docker image name |
<!-- action-docs-outputs -->

<!-- action-docs-runs -->
## Runs

This action is a `composite` action.
<!-- action-docs-runs -->

<!-- action-docs-usage -->
<!-- prettier-ignore-end -->

# Example

Here's an example of how to integrate this action into your workflow:

```yaml
name: Container Security Scan Workflow

on:
  push:
    branches:
      - main

jobs:
  container-scan:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Lacework Container Scan
        uses: open-turo/actions-security/container-scan@v1 # Specify the path to the action in your repository
        with:
          lw-account-name: ${{ secrets.LW_ACCOUNT_NAME }}
          lw-access-token: ${{ secrets.LW_ACCESS_TOKEN }}
          image-tag: <your-docker-image-tag>
```

## Notes

- By default, this action will perform actions/checkout as its first step.

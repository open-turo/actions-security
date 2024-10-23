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
    dockerhub-user: ${{ secrets.DOCKER_USERNAME }}
    dockerhub-password: ${{ secrets.DOCKER_PASSWORD }}
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
| dockerhub-user | username for dockerhub | `false` |  |
| dockerhub-password | password for dockerhub | `false` |  |
| docker-config-file | Path to the docker config file (defaults to .docker-config.json) Must contain imageName, may contain dockerfile | `false` | .docker-config.json |
| github-token | GitHub token | `true` |  |
| lw-account-name | Lacework account name | `true` |  |
| lw-access-token | Lacework access token | `true` |  |
| image-name | Docker image name | `false` |  |
| image-tag | Docker image tag | `true` |  |
| image-platform | Target platform to build image for (eg. linux/amd64 (default), linux/arm64, etc) | `false` | linux/amd64 |
| build-args | List of build arguments for docker build as key-value pairs (e.g., KEY=VALUE) | `false` |  |
| build-contexts | List of additional build contexts (e.g., name=path) | `false` |  |
| secrets | List of secrets for docker build as key-value pairs (e.g., SECRET_KEY=VALUE) | `false` |  |
| enable-docker-build | Docker image tag | `false` | true |
| image-tags | List of tags as key-value pair attributes | `false` |  |
<!-- action-docs-inputs -->

<!-- action-docs-outputs -->
## Outputs

| parameter | description |
| --- | --- |
| comment-id | Comment ID of the test report |
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
          dockerhub-user: ${{ secrets.DOCKER_USERNAME }}
          dockerhub-password: ${{ secrets.DOCKER_PASSWORD }}
          lw-account-name: ${{ secrets.LW_ACCOUNT_NAME }}
          lw-access-token: ${{ secrets.LW_ACCESS_TOKEN }}
          github-token: <your-secret-for-github-token>
          image-tag: <your-docker-image-tag>
```

## Notes

- By default, this action will perform actions/checkout as its first step.

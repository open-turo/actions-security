# GitHub Action Container-Scan

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

Scans container images for vulnerabilities using Wiz CLI
<!-- action-docs-description source="action.yaml" -->

## Smart Scan Triggers

This action automatically skips container scanning on pull requests when no container-related files have changed. This optimization reduces CI time for PRs that don't affect the container image.

### How it works

- **On `pull_request` events**: The action checks if any container-related files changed compared to the base branch. If no relevant files changed, the scan is skipped.
- **On `push` events**: The action checks if any container-related files changed compared to the previous commit. If no relevant files changed, the scan is skipped.
- **On `workflow_dispatch` events**: The scan always runs (user explicitly requested it).
- **On `schedule` events**: The scan always runs (designed to catch new CVEs and base image updates).

### Files that trigger a scan

The following file patterns will trigger a container scan:

- `Dockerfile`, `*.dockerfile`
- `docker-compose*.yml`, `docker-compose*.yaml`
- `.docker-config.json`
- Lockfiles: `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `Gemfile.lock`, `requirements.txt`, `poetry.lock`, `Pipfile.lock`, `go.sum`, `Cargo.lock`, `composer.lock`

### Outputs

The action provides a `scan-skipped` output that indicates whether the scan was skipped:

```yaml
- uses: open-turo/actions-security/container-scan@v4
  id: scan
  with:
    # ... inputs

- name: Check if scan was skipped
  if: steps.scan.outputs.scan-skipped == 'true'
  run: echo "Scan was skipped because no container-related files changed"
```

### Security Note

This optimization is safe because:
- Registry scanning (Wiz) continuously monitors images for new vulnerabilities
- Scheduled scans catch base image updates and new CVE publications
- Manual triggers (`workflow_dispatch`) always run a full scan

<!-- action-docs-usage source="action.yaml" -->
## Usage

```yaml
- uses: @
  with:
    image-name:
    # Docker image name
    #
    # Required: false
    # Default: ""

    image-tag:
    # Docker image tag
    #
    # Required: true
    # Default: ""

    image-platform:
    # Target platform to build image for (eg. linux/amd64 (default), linux/arm64, etc)
    #
    # Required: false
    # Default: ""

    enable-docker-build:
    # Enable Docker build
    #
    # Required: false
    # Default: true

    image-tags:
    # List of tags as key-value pair attributes
    #
    # Required: false
    # Default: ""

    artifactory-username:
    # Artifactory username
    #
    # Required: false
    # Default: ""

    artifactory-auth-token:
    # Artifactory auth token
    #
    # Required: false
    # Default: ""

    build-args:
    # List of build arguments for docker build as key-value pairs
    #
    # Required: false
    # Default: ""

    build-contexts:
    # List of additional build contexts (e.g., name=path)
    #
    # Required: false
    # Default: ""

    docker-config-file:
    # Path to the docker config file (defaults to .docker-config.json) Must contain imageName, may contain dockerfile
    #
    # Required: false
    # Default: .docker-config.json

    github-token:
    # GitHub token
    #
    # Required: false
    # Default: ""

    secrets:
    # List of secrets for docker build as key-value pairs (e.g., SECRET_KEY=VALUE)
    #
    # Required: false
    # Default: ""

    dockerhub-user:
    # DockerHub username
    #
    # Required: true
    # Default: ""

    dockerhub-password:
    # DockerHub password
    #
    # Required: true
    # Default: ""

    target:
    # Target build stage for multi-stage Docker builds
    #
    # Required: false
    # Default: ""

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

    container-setup-commands:
    # Commands to set up the container environment
    #
    # Required: false
    # Default: ""

    s3-bucket-name:
    # S3 bucket name for caching Wiz CLI binary
    #
    # Required: false
    # Default: ""

    s3-bucket-region:
    # S3 bucket region for caching
    #
    # Required: false
    # Default: us-east-1

    wiz-cli-version:
    # Specific Wiz CLI version to download (defaults to latest)
    #
    # Required: false
    # Default: latest

    container-setup-env:
    # Environment variables for container setup as key-value pairs (e.g., AWS_ACCESS_KEY_ID=value,ARTIFACTORY_USERNAME=value)
    #
    # Required: false
    # Default: ""

    debug:
    # Enable debug output to display full scan results in the workflow logs
    #
    # Required: false
    # Default: false
```
<!-- action-docs-usage source="action.yaml" -->

## Usage

```yaml
- uses: @
  with:
    dockerhub-user:
    # username for dockerhub
    #
    # Required: false
    # Default: ""

    dockerhub-password:
    # password for dockerhub
    #
    # Required: false
    # Default: ""

    docker-config-file:
    # Path to the docker config file (defaults to .docker-config.json) Must contain imageName, may contain dockerfile
    #
    # Required: false
    # Default: .docker-config.json

    github-token:
    # GitHub token
    #
    # Required: true
    # Default: ""

    lw-account-name:
    # Lacework account name
    #
    # Required: true
    # Default: ""

    lw-access-token:
    # Lacework access token
    #
    # Required: true
    # Default: ""

    image-name:
    # Docker image name
    #
    # Required: false
    # Default: ""

    image-tag:
    # Docker image tag
    #
    # Required: true
    # Default: ""

    image-platform:
    # Target platform to build image for (eg. linux/amd64 (default), linux/arm64, etc)
    #
    # Required: false
    # Default: linux/amd64

    build-args:
    # List of build arguments for docker build as key-value pairs (e.g., KEY=VALUE)
    #
    # Required: false
    # Default: ""

    secrets:
    # List of secrets for docker build as key-value pairs (e.g., SECRET_KEY=VALUE)
    #
    # Required: false
    # Default: ""

    enable-docker-build:
    # Docker image tag
    #
    # Required: false
    # Default: true
```

<!-- prettier-ignore-end -->

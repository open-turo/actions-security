# GitHub Action Container-Scan

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

GitHub Action for scanning container images for vulnerabilities using Lacework.
<!-- action-docs-description source="action.yaml" -->

<!-- action-docs-usage source="action.yaml" -->
## Usage

```yaml
- uses: @
  with:
    dockerhub-user:
    # DockerHub username for authentication.
    #
    # Required: false
    # Default: ""

    dockerhub-password:
    # DockerHub password for authentication.
    #
    # Required: false
    # Default: ""

    docker-config-file:
    # Path to the Docker config file (default is .docker-config.json) Must contain imageName and optionally the Dockerfile path.
    #
    # Required: false
    # Default: .docker-config.json

    github-token:
    # GitHub token for accessing repositories.
    #
    # Required: true
    # Default: ""

    lw-account-name:
    # Lacework account name for scanning.
    #
    # Required: true
    # Default: ""

    lw-access-token:
    # Lacework access token for scanning.
    #
    # Required: true
    # Default: ""

    image-name:
    # Name of the Docker image to scan.
    #
    # Required: false
    # Default: ""

    image-tag:
    # Tag of the Docker image to scan.
    #
    # Required: true
    # Default: ""

    image-platform:
    # Target platform for Docker image (e.g., linux/amd64, linux/arm64).
    #
    # Required: false
    # Default: linux/amd64

    build-args:
    # Build arguments for the Docker build as key-value pairs.
    #
    # Required: false
    # Default: ""

    secrets:
    # Secrets for the Docker build as key-value pairs.
    #
    # Required: false
    # Default: ""

    enable-docker-build:
    # Whether to enable Docker image building (default is true).
    #
    # Required: false
    # Default: true
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

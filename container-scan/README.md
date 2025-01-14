# GitHub Action Container-Scan

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

Scans container images for vulnerabilities using Lacework
<!-- action-docs-description source="action.yaml" -->

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

    MAX_MIND_USER:
    # MaxMind User ID
    #
    # Required: false
    # Default: ""

    MAX_MIND_LICENSE_KEY:
    # MaxMind License Key
    #
    # Required: false
    # Default: ""

    VFUNCTION_FILE_NAME:
    # Vfunction file name
    #
    # Required: false
    # Default: ""
```
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
```

<!-- prettier-ignore-end -->

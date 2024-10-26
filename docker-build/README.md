# GitHub Action Integration-Test

<!-- prettier-ignore-start -->
<!-- action-docs-description source="action.yaml" -->
## Description

Only builds docker images for the input platform, tags and image version
<!-- action-docs-description source="action.yaml" -->

<!-- prettier-ignore-start -->

<!-- action-docs-usage source="action.yaml" -->
## Usage

```yaml
- uses: @
  with:
    docker-config-file:
    # Path to the docker config file (defaults to .docker-config.json) Must contain imageName, may contain dockerfile.
    #
    # Required: false
    # Default: .docker-config.json

    dockerhub-user:
    # username for dockerhub
    #
    # Required: true
    # Default: ""

    dockerhub-password:
    # password for dockerhub
    #
    # Required: true
    # Default: ""

    github-token:
    # Usually secrets.GITHUB_TOKEN
    #
    # Required: true
    # Default: ""

    image-version:
    # Docker image version
    #
    # Required: true
    # Default: ""

    image-platform:
    # Target platform to build image for (eg. linux/amd64 (default), linux/arm64, etc)
    #
    # Required: false
    # Default: linux/amd64

    docker-metadata-tags:
    # 'List of tags as key-value pair attributes' See: https://github.com/docker/metadata-action#tags-input
    #
    # Required: false
    # Default: ""

    push:
    # Do you want to push the image to the registry
    #
    # Required: false
    # Default: false

    load:
    # Do you want to load the single-platform build result to docker images
    #
    # Required: false
    # Default: true

    build-args:
    # List of build arguments as key-value pairs (e.g., KEY=VALUE)
    #
    # Required: false
    # Default: ""

    secrets:
    # List of secrets as key-value pairs (e.g., SECRET_KEY=VALUE)
    #
    # Required: false
    # Default: ""
```
<!-- action-docs-usage source="action.yaml" -->

<!-- prettier-ignore-end -->

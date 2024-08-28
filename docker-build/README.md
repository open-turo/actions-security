# GitHub Action Docker-build

<!-- prettier-ignore-start -->
<!-- action-docs-description -->
## Description

Only builds docker images for the input platform, tags and image version
<!-- action-docs-description -->
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
## Usage

This action will build a docker image with appropriate tags.

It assumes that the repo has a configuration file in `<repo-root>/.docker-config.json` with the following properties:

- `imageName`: the image name (org/image-name)
- `dockerfile`: the path to the dockerfile to build - defaults to `./Dockerfile`

Example:

```json
{
  "imageName": "turo/hello-world-msvc",
  "dockerfile": "./Dockerfile"
}
```

#### Basic Usage:

```yaml
steps:
  - uses: open-turo/actions-jvm/release@v3
    name: Release
    id: release
    with:
      checkout-repo: true
      github-token: ${{ secrets.GITHUB_TOKEN }}
      dry-run: false
  - uses: open-turo/actions-security/build-docker@v2
    id: docker-build
    with:
      dockerhub-user: ${{ secrets.DOCKER_USERNAME }}
      dockerhub-password: ${{ secrets.DOCKER_PASSWORD }}
      github-token: ${{ secrets.GITHUB_TOKEN }}
      image-version: ${{ steps.release.outputs.new-release-version }}
      docker-metadata-tags: |
        type=ref,event=branch
        type=ref,event=pr
        type=semver,pattern={{version}},value=${{ steps.release.outputs.new-release-version }}
```

#### Dynamically input multiple build arguments and secrets:

If you want to pass multiple build arguments and secrets, you can use the `build-args` and `secrets` input parameters.

```yaml
steps:
  - uses: open-turo/actions-jvm/release@v3
    name: Release
    id: release
    with:
      checkout-repo: true
      github-token: ${{ secrets.GITHUB_TOKEN }}
      dry-run: false
  - uses: open-turo/actions-security/build-docker@v2
    id: docker-build
    with:
      dockerhub-user: ${{ secrets.DOCKER_USERNAME }}
      dockerhub-password: ${{ secrets.DOCKER_PASSWORD }}
      github-token: ${{ secrets.GITHUB_TOKEN }}
      image-version: ${{ steps.release.outputs.new-release-version }}
      build-args: |
        KEY1=VALUE1
        KEY2=VALUE2
      secrets: |
        SECRET_KEY1=SECRET_VALUE1
        SECRET_KEY2=SECRET_VALUE2
      docker-metadata-tags: |
        type=ref,event=branch
        type=ref,event=pr
        type=semver,pattern={{version}},value=${{ steps.release.outputs.new-release-version }}
```
<!-- prettier-ignore-end -->

## Inputs

| parameter            | description                                                                                                      | required | default             |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- | -------- | ------------------- |
| docker-config-file   | Path to the docker config file (defaults to .docker-config.json) Must contain imageName, may contain dockerfile. | `false`  | .docker-config.json |
| dockerhub-user       | username for dockerhub                                                                                           | `true`   |                     |
| dockerhub-password   | password for dockerhub                                                                                           | `true`   |                     |
| github-token         | Usually secrets.GITHUB_TOKEN                                                                                     | `true`   |                     |
| image-version        | Docker image version                                                                                             | `true`   |                     |
| image-platform       | Target platform to build image for (eg. linux/amd64 (default), linux/arm64, etc)                                 | `false`  | linux/amd64         |
| docker-metadata-tags | 'List of tags as key-value pair attributes' See: https://github.com/docker/metadata-action#tags-input            | `false`  |                     |
| push                 | Do you want to push the image to the registry                                                                    | `false`  | false               |
| load                 | Do you want to load the single-platform build result to docker images                                            | `false`  | true                |
| build-args           | List of build arguments as key-value pairs (e.g., KEY=VALUE)                                                     | `false`  |                     |
| secrets              | List of secrets as key-value pairs (e.g., SECRET_KEY=VALUE)                                                      | `false`  |                     |

## Outputs

| parameter      | description                                        |
| -------------- | -------------------------------------------------- |
| image-name     | Docker image name                                  |
| image-with-tag | Full image with tag - <image-name>:<image-version> |
| image-tag      | Docker image tag                                   |

## Runs

This action is a `composite` action.

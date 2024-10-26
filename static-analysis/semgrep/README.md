# GitHub Action Static Security Scan Analysis

## Description

Github action that scans code changes being made and posts security findings in form of comments on pull requests

## Configuration

Step 1: Ensure Semgrep GitHub application is added to your repository. You can follow steps to add semgrep application from GitHub marketplace [here](https://semgrep.dev/docs/semgrep-ci/running-semgrep-ci-with-semgrep-cloud-platform/#granting-permissions-for-semgrep-cloud-platform-github-repositories-only)

Step 2: Ensure `SEMGREP_APP_TOKEN` is added to your respository as a repository secret. You must have a Semgrep Cloud Platform account to use this environment variable. To generate a token, see steps [here](https://semgrep.dev/docs/semgrep-ci/running-semgrep-ci-with-semgrep-cloud-platform/#creating-a-semgrep_app_token)

Step 3: Add a [Workflow File](https://help.github.com/en/articles/workflow-syntax-for-github-actions) to your repository to create custom automated processes.

## Usage

```yaml
# Name of this GitHub Actions workflow.
name: Security Scan

on:
  pull_request: {}
  workflow_dispatch: {}
  push:
    branches: ["master", "main"]
  schedule:
    - cron: "20 17 * * *" # Sets Semgrep to scan every day at 17:20 UTC.
    # It is recommended to change the schedule to a random time.

jobs:
  static-code-anaylsis:
    name: Security scan
    steps:
      - uses: actions/checkout@v4
      - uses: open-turo/security-actions/static-code-analysis@v2
        with:
          semgrep-app-token: ${{ secrets.SEMGREP_APP_TOKEN }}
```

## Inputs

| parameter         | description                                                                                              | required | default |
| ----------------- | -------------------------------------------------------------------------------------------------------- | -------- | ------- |
| checkout-repo     | Perform checkout as first step of action                                                                 | `false`  | `true`  |
| semgrep-app-token | API Token generated from Semgrep console to pull security rules config. e.g. `secrets.SEMGREP_APP_TOKEN` | `true`   |         |

## Outputs

N/A

## Runs

- This action is a `composite` action.

## Notes

- By default, this action will perform actions/checkout as its first step.

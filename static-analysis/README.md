# GitHub Action Static Analysis Preview

## Description

Github action that scans code changes being made and posts security findings in form of comments on pull requests

## Configuration

Step 1: Ensure Semgrep GitHub application is added to your repository. You can follow steps to add semgrep application from GitHub marketplace [here](https://semgrep.dev/docs/semgrep-ci/running-semgrep-ci-with-semgrep-cloud-platform/#granting-permissions-for-semgrep-cloud-platform-github-repositories-only)

Step 2: Ensure `SEMGREP_APP_TOKEN` is added to your respository as a repository secret. You must have a Semgrep Cloud Platform account to use this environment variable. To generate a token, see steps [here](https://semgrep.dev/docs/semgrep-ci/running-semgrep-ci-with-semgrep-cloud-platform/#creating-a-semgrep_app_token)

Step 3: Add a [Workflow File](https://help.github.com/en/articles/workflow-syntax-for-github-actions) to your repository to create custom automated processes.

## Usage

```yaml
# Name of this GitHub Actions workflow.
name: Static code analysis using Semgrep

on:
  # Scan changed files in PRs (diff-aware scanning):
  pull_request: {}
  # Scan on-demand through GitHub Actions interface:
  workflow_dispatch: {}
  # Scan mainline branches and report all findings:
  push:
    branches: ["master", "main"]
  # [optional] Schedule the CI job (this method uses cron syntax):
  schedule:
    - cron: "20 17 * * *" # Sets Semgrep to scan every day at 17:20 UTC.
    # It is recommended to change the schedule to a random time.

jobs:
  static-code-anaylsis:
    # User definable name of this GitHub Actions job.
    name: Static code analysis using Semgrep
    steps:
      # Fetch project source with GitHub Actions Checkout.
      - uses: actions/checkout@v3
      - uses: open-turo/security-actions/static-code-analysis@v1
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

N/A

# My First GitHub Actions Workflow

---

## Task 1: Set Up

Created a public GitHub repository named `github-actions-practice` and cloned it locally.

Created the workflow directory:

```bash
# Create the GitHub Actions workflow directory
mkdir -p .github/workflows

# Verify the directory structure
ls -la .github/workflows

# The commands create and check the workflow directory.
```

---

## Task 2: Hello Workflow

Created `.github/workflows/hello.yml` to run automatically on every push.

The workflow checks out the repository and prints:

```text
Hello from GitHub Actions!
```

---

## Task 3: Understand the Anatomy

- **`on:`** Defines the event that triggers the workflow. Here, every push triggers it.
- **`jobs:`** Defines the jobs that the workflow runs.
- **`runs-on:`** Specifies the runner environment. Here, it is `ubuntu-latest`.
- **`steps:`** Lists the actions and commands executed in a job.
- **`uses:`** Runs a reusable action, such as `actions/checkout@v4`.
- **`run:`** Executes a shell command on the runner.
- **`name:`** Gives a workflow, job, or step a readable name.

---

## Task 4: Add More Steps

Updated the workflow to:

- Print the current date and time.
- Print the branch name using `${{ github.ref_name }}`.
- List repository files using `ls -la`.
- Print the runner operating system using `${{ runner.os }}`.

Pushed the updated workflow to trigger another run.

---

## Task 5: Break It on Purpose

Temporarily added a step to make the workflow fail:

```yaml
- name: Test intentional failure
  run: exit 1
```

Pushed the change and checked the failed run in the GitHub Actions tab.

A failed step appears in red, and subsequent steps are skipped by default unless configured otherwise. The logs show which command failed.

Removed the intentional failure step and pushed the corrected workflow to trigger a new run.

---

## Key Takeaways

1. GitHub Actions automates workflows in response to events such as code pushes.
2. Workflow files are stored in the `.github/workflows/` directory and written in YAML.
3. A workflow contains jobs, and each job contains steps that run commands or reusable actions.
4. GitHub-hosted runners provide environments such as `ubuntu-latest` to execute workflow jobs.
5. The Actions tab displays workflow results and logs, helping identify failures and verify fixes.

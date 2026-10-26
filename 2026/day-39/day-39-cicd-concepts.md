# What is CI/CD?

---

## Task 1: The Problem

### 1. What can go wrong?

- Code changes from different developers may conflict.
- Bugs may reach production because testing was skipped.
- Manual deployments can cause human errors.
- Deployments may be inconsistent across environments.
- Finding the cause of a production issue can take time.

### 2. What does "It works on my machine" mean?

It means the application works on one developer's computer but fails in another environment because of differences in dependencies, configurations, software versions, or operating systems.

### 3. How many times a day can a team safely deploy manually?

There is no fixed number. However, frequent manual deployments increase the risk of mistakes and consume time. Automation makes frequent deployments more consistent and reliable.

---

## Task 2: CI vs CD

### 1. Continuous Integration (CI)

Developers frequently merge code into a shared repository. Automated builds and tests help detect bugs and integration issues early.

**Example:** A developer pushes code to GitHub, and automated tests run to check whether the changes work.

### 2. Continuous Delivery

Code is automatically built, tested, and prepared for release. Production deployment usually requires manual approval.

**Example:** After tests pass, the application image is built and stored in a container registry, ready for release.

### 3. Continuous Deployment

Every change that passes the required automated checks is automatically deployed to production without manual release approval.

**Example:** A successful code change passes automated tests and is automatically released to the production application.

---

## Task 3: Pipeline Anatomy

- **Trigger:** An event that starts a pipeline, such as a code push or pull request.
- **Stage:** A logical phase of the pipeline, such as build, test, or deploy.
- **Job:** A unit of work within a stage that runs on a runner.
- **Step:** An individual command or action inside a job.
- **Runner:** The machine or environment that executes a job.
- **Artifact:** An output produced by a job, such as a Docker image, application package, or test report.

---

## Task 4: Draw a Pipeline

Scenario: A developer pushes code to GitHub. The application is tested, built into a Docker image, and deployed to a staging server.

```text
Developer Pushes Code
         |
         v
+--------------------+
| Stage 1: Test      |
| Run automated tests|
+--------------------+
         |
         v
+--------------------+
| Stage 2: Build     |
| Build Docker Image |
+--------------------+
         |
         v
+--------------------+
| Stage 3: Deploy    |
| Deploy to Staging  |
+--------------------+
         |
         v
 Application Running
 in Staging
```

---

## Task 5: Explore in the Wild

**Repository:** [`github-actions-zero-to-hero`](https://github.com/TrainWithShubham/github-actions-zero-to-hero)

**Workflow file:** [`.github/workflows/cicd.yml`](https://github.com/TrainWithShubham/github-actions-zero-to-hero/blob/main/.github/workflows/cicd.yml)

### What triggers it?

The workflow uses `workflow_dispatch`, so it is triggered manually from the GitHub Actions tab. It accepts an `environment` input with three options: `dev`, `prod`, and `staging`. The default is `dev`.

### How many jobs does it have?

It has **4 jobs**:

1. `code`
2. `build`
3. `test`
4. `deploy`

### What does it do?

- **Code:** Runs on `ubuntu-latest` and represents checking out the code.
- **Build:** Depends on the `code` job and represents building the Docker container.
- **Test:** Depends on the `build` job and represents testing the container.
- **Deploy:** Depends on both `build` and `test`, but runs only when the selected environment is `dev`.

The workflow currently uses `echo` commands to demonstrate these steps rather than performing actual Docker builds, tests, or deployments.

### Pipeline Flow

```text
Manual Trigger
      |
      v
    Code
      |
      v
    Build
      |
      v
     Test
      |
      v
Deploy (dev only)
```

---

## Key Takeaways

1. **CI/CD automates software delivery** and reduces errors caused by manual processes.
2. **Continuous Integration (CI)** helps detect bugs early through automated builds and tests.
3. **Continuous Delivery** keeps code ready for release, while **Continuous Deployment** automatically releases changes to production.
4. **GitHub Actions workflows** use triggers, jobs, and steps to automate development tasks.
5. **Job dependencies** control execution order, and conditions can determine whether a job, such as deployment, should run.

# CSC 325 — Four-stage CI/CD demonstration

Small Django REST Framework backend to demonstrate Setup → Dependencies → Test → Deploy in GitHub Actions.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py test
python manage.py runserver
```

Visit http://127.0.0.1:8000/api/status/.

## CI/CD

The workflow at `.github/workflows/csc325_ci_cd.yml` runs on push to `main` and on pull requests into `main`. Four sequential jobs run in order. Each GitHub Actions job uses a new runner, so the Test job installs its own packages. The Deploy job uses the echo-only demonstration allowed by the assignment; it **does not host a live application**.

## Before recording

Create a feature branch and a ruleset protecting `main`. Prepare a small API response change and a matching test, but don't push the demonstration change until you are recording. Check the rubric for whether the running-example URL needs actual public hosting.

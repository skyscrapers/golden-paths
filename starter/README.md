# Golden Path Starter

A starter template for deploying an application on the Skyscrapers platform. Copy this directory to bootstrap a new service with all the golden path patterns built in.

## What's included

- `app/` - A sample Flask application with Dockerfile and Prometheus metrics
- `charts/my-app/` - Helm chart with templates for deployment, service, ingress, metrics, alerts, network policies, and PDB
- `deploy/` - Flux GitOps configuration with Kustomize overlays (base + production)
- `.github/workflows/` - GitHub Actions CI to build and push to ECR
- `.gitlab-ci.yml` - GitLab CI alternative
- `.sops.yaml` - SOPS configuration for secret encryption

Everything is **disabled by default** in `values.yaml`. Each golden path tells you which values to enable.

## Prerequisites

Before using this template, Skyscrapers will have provisioned:

- 1-n Kubernetes namespaces for your application
- 1-n ServiceAccounts with IRSA (AWS permissions your app needs)
- 1-n ECR repositories for your container images
- Kubernetes secrets with infrastructure credentials (if applicable)
- Flux watching your repository via a GitRepository + Kustomization

## Quick start

1. Copy this directory into a new repo
2. Rename `my-app` throughout to your service name
3. Replace the sample Flask app in `app/` with your application
4. Update `charts/my-app/values.yaml` with your app's defaults
5. Update `deploy/production/helmrelease-patch.yaml` with your ECR image URL and environment config
6. Encrypt your secrets: `sops -e -i deploy/production/secret.yaml`
7. Push to main -- CI builds, Flux deploys

## Python dependencies

`app/requirements.in` lists the direct dependencies of the sample app. `app/requirements.txt` is generated from it with [pip-tools](https://pip-tools.readthedocs.io/) and pins every package, so don't edit it by hand. Dependabot updates `requirements.txt` when a new version is out.

To add or change a dependency, edit `app/requirements.in`, then run `make requirements` in `starter/` to regenerate the pins. It uses Python 3.13, the version in the Dockerfile.

## Golden path documentation

Each feature in this starter is documented in detail:

- [Deploy Your Application](https://docs.skyscrapers.eu/docs/golden-paths/deploy-your-application/) - Dockerfile, Helm, Flux, CI
- Expose Your Application (TBD) - Ingress, TLS, DNS
- Manage Your Secrets (TBD) - SOPS, KMS
- Observe Your Application (TBD) - Metrics, logs, traces, alerts
- Protect Your Application (TBD) - Network policies, PDBs, backups
- Build a Well-Behaved Container (TBD) - Graceful shutdown, probes, signals

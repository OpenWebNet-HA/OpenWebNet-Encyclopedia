#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "usage: $0 ARTIFACT.json [COMMIT_MESSAGE]" >&2
  exit 2
fi

descriptor=$(readlink -f "$1")
commit_message=${2:-"Register external artifact"}

root=$(git rev-parse --show-toplevel)
cd "$root"

if [[ $(git branch --show-current) != main ]]; then
  echo "refusing: registry helper must run in the dedicated main worktree" >&2
  exit 2
fi
if [[ -n $(git status --porcelain) ]]; then
  echo "refusing: registry worktree is not clean" >&2
  git status --short >&2
  exit 2
fi

git fetch origin main --quiet
git merge --ff-only origin/main

python3 project/tools/register_artifact.py "$descriptor"

if git diff --quiet -- sources/artifact-manifest.yaml; then
  echo "artifact already present; nothing to commit"
  exit 0
fi

python3 project/review/checks/check_artifact_manifest.py
git diff --check -- sources/artifact-manifest.yaml
git add sources/artifact-manifest.yaml

staged=$(git diff --cached --name-only)
if [[ "$staged" != "sources/artifact-manifest.yaml" ]]; then
  echo "refusing: unexpected staged paths:" >&2
  printf '%s\n' "$staged" >&2
  exit 2
fi

git commit -m "$commit_message"
git push origin main
git rev-parse HEAD

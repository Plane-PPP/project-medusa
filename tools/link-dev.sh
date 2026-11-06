#!/usr/bin/env bash
# Links the Medusa content package into the OpenYAMM development worktree (no copying).
#   tools/link-dev.sh            link
#   tools/link-dev.sh --unlink   remove the link (Standard and MAW are unaffected)
# Only a symbolic link is created; no file of the engine or of MM6-MM8 is changed. The link path is listed in the
# worktree's git exclude file so it never shows up as a change.
set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
engine_root="${OPENYAMM_MEDUSA_ROOT:-$project_root/../openyamm-medusa}"
package_source="$project_root/content/engine/rulesets/medusa"
link_path="$engine_root/assets_dev/engine/rulesets/medusa"
exclude_entry="/assets_dev/engine/rulesets/medusa"

if [[ ! -d "$engine_root/.git" && ! -f "$engine_root/.git" ]]; then
    echo "OpenYAMM worktree not found: $engine_root" >&2
    exit 1
fi

if [[ "${1:-}" == "--unlink" ]]; then
    if [[ -L "$link_path" ]]; then
        rm -- "$link_path"
        echo "Removed $link_path"
    fi
    exit 0
fi

if [[ -e "$link_path" && ! -L "$link_path" ]]; then
    echo "Refusing to replace a real directory: $link_path" >&2
    exit 1
fi

ln -sfn -- "$package_source" "$link_path"
exclude_file="$(git -C "$engine_root" rev-parse --git-path info/exclude)"
case "$exclude_file" in /*) ;; *) exclude_file="$engine_root/$exclude_file" ;; esac
mkdir -p "$(dirname -- "$exclude_file")"
grep -qxF "$exclude_entry" "$exclude_file" 2>/dev/null || echo "$exclude_entry" >> "$exclude_file"
echo "Linked $link_path -> $package_source"

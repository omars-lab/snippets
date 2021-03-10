#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[1]}" )" >/dev/null 2>&1 && pwd )
REPO="${1:?Repo requird as first arg}"
REPO_URL=$(git -C "${REPO}" remote get-url origin)

function list_remote_branches() {
  git --no-pager -C "${1}" branch -rq | sed -E -e 's/^.* -> //g' | xargs -n 1 basename
}

list_remote_branches "${REPO}" \
  | xargs -I __ git clone --branch __ ${REPO_URL} ${DIR}/__


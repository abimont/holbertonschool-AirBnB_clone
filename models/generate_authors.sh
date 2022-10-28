#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

{
	cat <<- 'EOH'
		# This file lists all individuals having contributed content to the repository.
		# For how it is generated, see `models/generate_authors.sh`.
	EOH
	echo
	git log --format='%cn <%ce>' | LC_ALL=C.UTF-8 sort -uf | grep -v GitHub

} > AUTHORS

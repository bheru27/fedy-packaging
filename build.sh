#!/bin/bash

fedora_vers=(21 22)
top_dir=$(pwd)

if [[ "$1" == "repo" ]]; then
	build_repo="true"
elif [[ "$1" == "packages" ]]; then	
	build_packages="true"
	package_name="$2"
else
	echo "No target specified, e.g. - packages, repo"

	exit 1
fi

for version in ${fedora_vers[@]}; do
	repodir="${top_dir}/${version}"

	if [[ "$build_repo" == "true" ]]; then
		# Create repo data
		createrepo --delta $repodir
	elif [[ "$build_packages" == "true" ]]; then
		for spec in SPECS/*.spec; do
			if [[ "$package_name" != "" && "${package_name}.spec" != "$(basename $spec)" ]]; then
				continue
			fi

			rpmbuild -ba \
				--define "_topdir ${top_dir}" \
				--define "_rpmdir ${repodir}/RPMS" \
				--define "_srcrpmdir ${repodir}/SRPMS" \
				--define "dist .fc${version}" $spec
		done
	fi
done

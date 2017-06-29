mypy $1 \
	--python-version 3.5 \
	--ignore-missing-imports --follow-imports=skip \
	--check-untyped-defs

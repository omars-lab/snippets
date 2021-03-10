install:
	go mod download

to-string: install
	find . -name "stringer.go" -exec go run {} \;

parsing-strings: install
	find . -name "parsing-strings.go" -exec go run {} \;

adding-methods: install
	find . -name "adding-methods.go" -exec go run {} \;
	find . -name "adding-methods-bad-1-alternative.go" -exec go run {} \;
	find . -name "adding-methods-bad-1.go" -exec go run {} \; || true
	find . -name "adding-methods-bad-2.go" -exec go run {} \; || true

making-ids: install
	go run code-snippets/making-ids.go

yaml:
	go run code-snippets/understanding-yaml.go

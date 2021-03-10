# Hello World

What is the bare minimum to run a go program?
```
╰─$ echo 'package main\nimport (\n  "fmt"\n) \nfunc main() {\n  fmt.Println("hello")\n}' > test.go

╰─$ go run test.go
hello

╰─$ go build -o test.exe . && ./test.exe
hello
```

- https://yourbasic.org/golang/short-variable-declaration-outside-function/
- https://www.systutorials.com/how-to-print-a-line-to-stderr-and-stdout-in-go/

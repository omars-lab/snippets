
- Understanding Packages

What are the go.mod and go.sum?
    These are almost like the requirements.txt

How do I add new package to the go.mod?
    go get <packages>

What is the go path?
    ...

# Understanding Packages
- https://golang.org/cmd/go/#hdr-Vendor_Directories
- https://golang.org/cmd/go/

# Understanding GOPATH
- https://golang.org/doc/gopath_code.html

# Understanding Modules
- Maintaining go.mod and go.sum
- https://blog.golang.org/using-go-modules

## Adding Modules
- https://stackoverflow.com/questions/53682247/how-to-point-go-module-dependency-in-go-mod-to-a-latest-commit-in-a-repo
    - `go get github.com/google/uuid`

### Adding Specific Versions of Modules
- https://stackoverflow.com/questions/24855081/how-do-i-import-a-specific-version-of-a-package-using-go-get/33948752
    - `GO111MODULE=on go get github.com/rickar/cal@v1.0.1`

# Optimizing Builds
- http://dev.pawelsz.eu/2015/09/slow-go-compilation.html

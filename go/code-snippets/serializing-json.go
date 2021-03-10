package main

import (
	"encoding/json"
    "fmt"
)

type Dictionary map[string]interface{}

func test() []byte {
	json_data := Dictionary{"test": "ing"}
	raw_data, _ := json.Marshal(json_data)
	return raw_data
}

func main() {
    fmt.Println(string(test()))
}

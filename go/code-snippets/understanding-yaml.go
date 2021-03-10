package main

import (
	"fmt"
	"io/ioutil"
	"os"

	"gopkg.in/yaml.v2"
)

// CortexConfig ...
type InnerConfig struct {
	S string
	I int
}

// Config ...
type OutterConfig struct {
	InnerConfig       *InnerConfig
	CustomInnerConfig *InnerConfig `yaml:"custom"`
	DefaultedConfig   *InnerConfig
}

func fileExists(filename string) bool {
	info, err := os.Stat(filename)
	if os.IsNotExist(err) {
		return false
	}
	return !info.IsDir()
}

// LoadConfig ...
func LoadConfig(file string) (*OutterConfig, error) {

	if !fileExists(file) {
		return nil, fmt.Errorf("config file doesn't exist: %s", file)
	}

	data, err := ioutil.ReadFile(file)

	if err != nil {
		return nil, err
	}

	defaultInnerConfig := &InnerConfig{S: "a", I: 1}
	config := &OutterConfig{DefaultedConfig: defaultInnerConfig}
	err = yaml.Unmarshal(data, &config)

	if err != nil {
		return nil, err
	}

	return config, nil
}

func main() {
	config, e := LoadConfig("config-with-defaults.yaml")
	fmt.Println(config.DefaultedConfig)
	fmt.Println(e)
	bs, _ := yaml.Marshal(config)
	fmt.Println(string(bs))

	config, e = LoadConfig("config-without-defaults.yaml")
	fmt.Println(config.DefaultedConfig)
	fmt.Println(e)
	bs, _ = yaml.Marshal(config)
	fmt.Println(string(bs))

}

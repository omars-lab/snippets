SHELL := /bin/bash
MAKEFILE_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

# https://ant.apache.org/manual/tutorial-HelloWorldWithAnt.html

build-plain-java:
	mkdir -p build/classes
	javac -sourcepath src -d build/classes src/com/oeid/HelloWorld.java
	java -cp build/classes com.oeid.HelloWorld

build-plain-jar: build-plain-java
	mkdir -p build/jar
	jar cfm build/jar/HelloWorld.jar Manifest -C build/classes .
	java -jar build/jar/HelloWorld.jar

build-ant-basic:
	ant -f build-simple.xml compile jar run

build-ant-medium:
	ant -f build-medium.xml compile jar run

build-ant-complex: download-jars
	ant -f build-complex.xml compile jar run

build-ant-complex-with-tests: download-jars
	ant -f build-complex-with-tests.xml compile jar run junit junitreport

build-ant-complex-fat-jar-with-tests: download-jars
	ant -f build-complex-fat-jar-with-tests.xml compile jar run junit junitreport
	java -jar ${MAKEFILE_DIR}/build/jar/HelloWorld.jar

download-jars:
	mkdir -p ${MAKEFILE_DIR}/lib/
	mvn org.apache.maven.plugins:maven-dependency-plugin:2.4:get \
		-DremoteRepositories=http://download.java.net/maven/2 \
		-Dartifact=log4j:log4j:1.2.17 \
		-Ddest=${MAKEFILE_DIR}/lib/log4j-1.2.17.jar

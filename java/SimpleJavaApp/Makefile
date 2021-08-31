JAR_NAME=target/$(shell cat pom.xml | xq -r '.project | "\(.artifactId)-\(.version).\(.packaging)" ' )

compile:
	mvn compile

build:
	mvn package

${JAR_NAME}: build

run: ${JAR_NAME}
	java -jar ${JAR_NAME}

test:
	mvn test


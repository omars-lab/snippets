name := "scala-snippets"

version := "0.1"

scalaVersion := "2.11.12"

lazy val akkaVersion = "2.5.21"
lazy val scalazVersion = "7.2.27"
lazy val sparkVersion = "2.4.0"

// FP
libraryDependencies += "org.scalaz" %% "scalaz-core" % scalazVersion
libraryDependencies += "org.scalaz" %% "scalaz-concurrent" % scalazVersion

// Distributed Computing
libraryDependencies += "org.apache.spark" %% "spark-sql" % sparkVersion

// Akka
libraryDependencies += "com.typesafe.akka" %% "akka-actor" % akkaVersion
libraryDependencies += "com.typesafe.akka" %% "akka-testkit" % akkaVersion

libraryDependencies += "io.gatling" % "jsonpath_2.11" % "0.6.9"
libraryDependencies += "com.github.melrief" %% "purecsv" % "0.0.9"
libraryDependencies += "org.scalactic" %% "scalactic" % "3.0.1"

// Json Encoding / Decoding
libraryDependencies += "io.argonaut" %% "argonaut" % "6.2-RC2"

// Command Line Parsing
libraryDependencies += "com.github.scopt" %% "scopt" % "3.5.0"

// Time Utils
libraryDependencies += "com.github.nscala-time" %% "nscala-time" % "2.20.0"

// Testing
libraryDependencies += "org.scalatest" %% "scalatest" % "3.0.5" % "test"

//libraryDependencies += "io.argonaut" %% "argonaut-monocle" % "6.2-RC2"
//libraryDependencies += "com.github.julien-truffaut" %%  "monocle-core"  % "1.4.0"
//libraryDependencies += "com.github.julien-truffaut" %%  "monocle-macro" % "1.4.0"
//libraryDependencies += "com.github.julien-truffaut" %%  "monocle-law"   % "1.4.0" % "test"

//// Core library, included automatically if any other module is imported.
//libraryDependencies += "com.nrinaudo" %% "kantan.csv" % "0.5.0"

//// Provides scalaz type class instances for kantan.csv, and vice versa.
//libraryDependencies += "com.nrinaudo" %% "kantan.csv-scalaz" % "0.5.0"

//// Provides instances for joda time types.
//libraryDependencies += "com.nrinaudo" %% "kantan.csv-joda-time" % "0.5.0"

//// Automatic type class instances derivation.
//libraryDependencies += "com.nrinaudo" %% "kantan.csv-generic" % "0.5.0"

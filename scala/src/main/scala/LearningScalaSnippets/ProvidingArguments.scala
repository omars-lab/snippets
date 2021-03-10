package LearningScalaSnippets

import scopt.OptionParser

// https://www.spantree.net/blog/2017/06/26/scala-native-for-cli-tools.html

case class Config(count: Int = 1, objects: List[String] = List())

object Main extends App {
  val parser = new OptionParser[Config]("command-line-args-example") {
    override def showUsageOnError = true

    head("command-line-args-example", "0.1")

    opt[Int]('c', "count").action(
      (x, c) => c.copy(count = x)
    ).text("How many items to pick?")

    arg[String]("<options>...").unbounded().optional().action(
      // case class copy method ... https://alvinalexander.com/scala/scala-case-class-copy-method-example/
      (x, c) => c.copy(objects = c.objects :+ x)
    ).text("Options to choose from")

    help("help").text("prints this usage text")
  }

  // in an app ... args ... maps to sys args ...
  parser.parse(args :+ "1" :+ "2" :+ "3", Config()) match {
    case Some(config) =>
      LeveragingRandomness.pick(config.objects, config.count).foreach(println)
    case None =>
    // arguments are bad, error message will have been displayed
  }
  println("--------")
  // We can pass explicit sys args by hand ...
  parser.parse(List("-c", sys.env.getOrElse("COUNT", "2"), "apple", "banana", "cucumber"), Config()) match {
    case Some(config) =>
      LeveragingRandomness.pick(config.objects, config.count).foreach(println)
    case None =>
    // arguments are bad, error message will have been displayed
  }

}


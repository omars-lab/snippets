package LearningScalaSnippets

// https://blog.knoldus.com/customizing-string-interpolation-an-example/

object UnderstandingStringContexts {
   implicit class JsonHelper(val sc: StringContext) extends AnyVal {
     def commaSep(args: Any*): String = {
       val strings = sc.parts.iterator
//       val expressions = args.iterator
       strings.mkString(",")
     }
   }
 }

object Runner extends App {
  import UnderstandingStringContexts._
  val x = 1
  println(commaSep"a $x b $x c $x d")
}
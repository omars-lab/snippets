package LearningScalaSnippets

import LearningScalaSnippets.Implicits.{ImplicitToolbox, shared}

import scala.language.implicitConversions

object Implicits {

  object ImplicitToolbox {

    implicit def thisIsMyFirstImplicitButItsNameDoesntReallyMatter(z: Int): String = {
      s"Hello, ${z.toString}"
    }

    implicit def thisIsMySecondImplicitAndItsNameDoesntMatterAsWell(z: Int): String = {
      s"Bye, ${z.toString}"
    }
  }

  object shared {
    def f(x: String): Option[String] = {
      Some(x)
    }
  }

}

object Test1 extends App {
  import ImplicitToolbox.thisIsMyFirstImplicitButItsNameDoesntReallyMatter
  val blah: Int = 100
  val blah2: Int = 200
  println(shared.f(blah))
  println(shared.f(blah2))
}

object Test2 extends App {
  import ImplicitToolbox.thisIsMySecondImplicitAndItsNameDoesntMatterAsWell
  val blah: Int = 100
  val blah2: Int = 200
  println(shared.f(blah))
  println(shared.f(blah2))
}


/**
  * This wont compile!
  *     The compiler doesnt know whether to use `thisIsMyFirstImplicitButItsNameDoesntReallyMatter` or
  *     `thisIsMySecondImplicitAndItsNameDoesntMatterAsWell` to turn the Int into a String!
  */
//object Test3 extends App {
//  import ImplicitToolbox._
//  val blah: Int = 100
//  val blah2: Int = 200
//  println(shared.f(blah))
//  println(shared.f(blah2))
//}

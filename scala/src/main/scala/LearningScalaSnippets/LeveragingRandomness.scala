package LearningScalaSnippets

import scala.util.Random

object LeveragingRandomness {
  def pick[A](objects: List[A], count: Int): List[A] = {
    Random.shuffle(objects).take(count)
  }
}

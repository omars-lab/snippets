package LearningScalaSnippets

object UnderstandingFolds extends App{

  val s = Stream(1,2,3,4,5)
  val foldDefault = (List(): List[Int], Stream(): Stream[Int])
  val (newList, newStream) = s.foldLeft(foldDefault){
    case ((array, stream), streamElement) => (streamElement::array, stream.append(Stream(streamElement)))
  }
  println("Printing List")
  newList.foreach(x => println(x))
  println("Printing Stream")
  newStream.foreach(x => println(x))

}
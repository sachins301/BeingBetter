object StringMatchingInAnArray_1408 {
  def stringMatching1(words: Array[String]): List[String] = {
    var res = List[String]()
    for(i <- words.indices){
      var found = false
      for (j <- words.indices if !found){
        if(i != j && words(j).contains(words(i))){
          res = res :+ words(i)
          found = true
        }
      }
    }
    res
  }

  // FP
  def stringMatching(words: Array[String]): List[String] = {
    words.indices.flatMap(i =>
      words.indices.collect{
        case j if i != j && words(j).contains(words(i)) => words(i)
      }
    ).distinct.toList
  }
}
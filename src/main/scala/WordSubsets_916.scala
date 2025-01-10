object Solution {

  def frequency(word: String): Array[Int] ={
    word.foldLeft(Array.fill(26)(0)){
      (freq, c) => freq.updated(c - 'a', freq(c - 'a') + 1)
    }
  }

  def wordSubsets(words1: Array[String], words2: Array[String]): List[String] = {
    val words2Freq = words2.map(frequency).reduce {
      (freq1, freq2) => freq1.indices.map(i => math.max(freq1(i), freq2(i))).toArray
    }

    words1.filter { word =>
      val freq = frequency(word)
      words2Freq.indices.forall(i => freq(i) >= words2Freq(i))
    }.toList
  }
}
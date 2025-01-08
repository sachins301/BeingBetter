object Solution {
  def countPrefixSuffixPairs(words: Array[String]): Int = {
    words.indices.flatMap { i =>
      (i + 1 until words.length).collect {
        case j if words(j).startsWith(words(i)) && words(j).endsWith(words(i)) => 1
      }
    }.sum
  }
}
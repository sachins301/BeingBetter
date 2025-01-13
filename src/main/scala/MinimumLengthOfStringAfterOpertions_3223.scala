object Solution {
  def minimumLength(s: String): Int = {
    val counter = s.map(c => (c, 1)).groupBy(_._1).map(x => (x._1, x._2.length))

    def reduceLength(v: Int, r: Int): Int = {
      if (v > 2) reduceLength(v - 2, r - 2) else r
    }

    counter.foldLeft(s.length) {
      case (acc, (_, v)) => reduceLength(v, acc)
    }
  }
}
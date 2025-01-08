object Solution {
  def containsDuplicate(nums: Array[Int]): Boolean = {
    import scala.collection.mutable.Set
    var visit = Set[Int]()
    var res = false
    for(n <- nums if !res){
      res = visit.contains(n)
      visit.add(n)
    }
    res
  }
}
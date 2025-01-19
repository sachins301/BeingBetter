object BruteForceSolution {
    def prefixCount(words: Array[String], pref: String): Int = {
        words.foldLeft(0){ (acc, word) =>
            if (word.startsWith(pref)) acc + 1 else acc
        }
    }
}

// Trie Solution
case class TrieNode(children: Map[Char, TrieNode] = Map.empty, count: Int = 0) {
    override def equals(that: Any): Boolean = ???
}

class Trie(val root: TrieNode = TrieNode()){
    def add(word: String, node: TrieNode = root): TrieNode ={
        if (word.isEmpty) {
            node.copy(count = node.count + 1)
        } else {
            val char = word.head
            val updatedChild = add(word.tail, node.children.getOrElse(char, TrieNode()))
            node.copy(children = node.children.updated(char, updatedChild), count = node.count + 1)
        }
    }
    def count(word: String, node: TrieNode = root): Int ={
        if (word.isEmpty){
            node.count
        } else {
            node.children.get(word.head) match {
                case Some(child) => count(word.tail, child)
                case None => 0
            }
        }
    }
}

object CountingWordsWithAGivenPrefix_2185 {
    def prefixCount(words: Array[String], pref: String): Int = {
        words.foldLeft(new Trie())((t: Trie, word) => new Trie(t.add(word))).count(pref)
    }
}


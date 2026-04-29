class PrefixTree {

    static class TireNode{
        int pass ;
        int end ;
        TireNode[] nexts = new TireNode[26] ;
        public TireNode(){ 
            pass = 0 ;
            end = 0 ;  
        }
    }

    TireNode root ;

    public PrefixTree() {
        root = new TireNode();
    }

    public void insert(String word) {
        if(word != null && !word.isEmpty()){
            char[] chars = word.toCharArray();
            TireNode node = root ;
            node.pass++ ;
            for(char c : chars){
                var t = node.nexts[c-'a'] ;
                if(t == null){
                    t = new TireNode();
                    t.pass++;
                }
                node.nexts[c-'a'] = t ;
                node.pass++;
                node = t ;
            }
            node.end++;
        }
    }

    public boolean search(String word) {
        TireNode node = root ; 
        if (node.pass == 0) {
            return false ;
        }
        for (char c : word.toCharArray()){
             if(node.nexts[c-'a'] == null)
                return false ;
            node = node.nexts[c-'a'] ;
        }
        if (node.end > 0)
            return true ; 
        else 
            return false ;
    }

    public boolean startsWith(String prefix) {
        TireNode node = root ; 
        if (node.pass == 0) {
            return false ;
        }
        for (char c : prefix.toCharArray()){
             if(node.nexts[c-'a'] == null)
                return false ;
            node = node.nexts[c-'a'] ;
        }
        return true ;
    }
}

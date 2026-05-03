class WordDictionary {

    static class TireNode{
        int pass ;
        int end ;
        TireNode[] nexts = new TireNode[26] ;
        public TireNode(){
            pass =0 ;
            end =0 ;
        }
        
    }
    TireNode root;

    public WordDictionary() {
        root = new TireNode() ;
    }

    public void addWord(String word) {
        if(word == null || word.isEmpty()){
            return ;
        }
        char[] chars = word.toCharArray(); 
        TireNode node = root ;
        for(char c : chars){
            node.pass++ ;
            if (node.nexts[c - 'a'] == null)
                 node.nexts[c - 'a'] = new TireNode();
            node = node.nexts[c-'a'] ;
        }
        node.end ++ ;
        System.out.println("Adding " + word + " node.end:" + node.end);
    }

    public boolean search(String word) {
        if( word == null || word.isEmpty()){
            return true ;
        }

        return process(word, 0, root) ;
      
    }

    boolean process(String word, int index, TireNode node){
       
        if(index == word.length()){
            return node.end > 0 ;
        }

        char c = word.charAt(index);
        if(c == '.'){
            for(TireNode tn : node.nexts){
                if(tn != null){
                        if(process(word, index+1, tn)){
                        return true ;
                        }
                }
            }
            return false ;
        }else{
            System.out.println("checking " + word + " - " + c);
            TireNode n = node.nexts[c - 'a']; 
            if(n == null){
                return false ;
            }
            return process(word, index +1, n) ;
        }
         
    }
}

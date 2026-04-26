class Solution {
    
    List<String> res = new ArrayList<>();
    public List<String> letterCombinations(String digits) {

        if(digits == null || digits.length() == 0){
            return res;
        }

        Map<Character, String> map = new HashMap<>() ; 
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        char[] chars = digits.toCharArray(); 

        List<String> toProcess = new ArrayList<>();

        for(int i =0 ; i < chars.length; i++){ 
            if(map.containsKey(chars[i]))
                toProcess.add(map.get(chars[i])); 
        }
        process(toProcess, 0, "") ;
        System.out.println(map);
        System.out.println(toProcess) ;
        return res ;

    }

    void process(List<String> toProcess, int index, String path){
        if(index ==  toProcess.size()){
            res.add(path) ;
            return ;
        }

        String letters = toProcess.get(index) ;
        for(int i = 0 ; i < letters.length() ; i++){
            process(toProcess, index+1, path + letters.charAt(i));
        }
    }
}

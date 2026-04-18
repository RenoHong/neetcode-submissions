class Twitter {

    HashMap<Integer, Set<Integer>> followMap ;
    HashMap<Integer, List<Tweet>> tweetMap ;
    int timestamp ; 

    public Twitter() {
        followMap = new HashMap<>();
        tweetMap = new HashMap<>() ;
        timestamp = 0 ; 
    }
    
    public void postTweet(int userId, int tweetId) {
        tweetMap.putIfAbsent(userId, new ArrayList<Tweet>());
        tweetMap.get(userId).add(new Tweet(tweetId, ++timestamp));
    }
    
    public List<Integer> getNewsFeed(int userId) {
        List<Tweet> ret = new ArrayList<>(); 
        var users = new HashSet<Integer>();
        users.add(userId);
        var set = followMap.getOrDefault(userId, new HashSet<Integer>()) ;
        users.addAll(set);
        for(int i : users){
            List list = tweetMap.getOrDefault(i, new ArrayList<Tweet>()); 
            ret.addAll(list);
        }
        ret.sort((t1, t2)-> t2.getTimestamp() - t1.getTimestamp());
       return ret.stream().map(t->t.getId()).limit(10).collect(Collectors.toList());

    }
    
    public void follow(int followerId, int followeeId) {
        followMap.putIfAbsent(followerId, new HashSet<Integer>()) ;
        followMap.get(followerId).add(followeeId) ;
    }
    
    public void unfollow(int followerId, int followeeId) {
        followMap.getOrDefault(followerId, new HashSet<Integer>()).remove(followeeId);
    }

    class Tweet{
        int timestamp ; 
        int id ;
        public Tweet(int id, int timestamp){
            this.id = id ;
            this.timestamp = timestamp ;
        }
        public int getId(){return this.id ;} 
        public int getTimestamp(){return this.timestamp ; } 
    }
}


class MedianFinder {

    PriorityQueue<Integer> minQueue = new PriorityQueue<>((o1, o2) -> Integer.compare(o1, o2));
    PriorityQueue<Integer> maxQueue = new PriorityQueue<>((o1, o2) -> Integer.compare(o2 ,o1));

    public MedianFinder() {
    }
    
    public void addNum(int num) {

        if (maxQueue.size()> 0 && num > maxQueue.peek()){
            minQueue.offer(num);
        }else if(minQueue.size() > 0 && num < minQueue.peek()){
            maxQueue.offer(num);
        }else{
            minQueue.offer(num);
        }

        // Rebalance the pq
        while(maxQueue.size() - minQueue.size() > 1){
            minQueue.offer(maxQueue.poll());
        }   

        while(minQueue.size() - maxQueue.size() > 1){
            maxQueue.offer(minQueue.poll());
        } 

    }
    
    public double findMedian() {
        if(minQueue.isEmpty() && maxQueue.isEmpty()){
            return 0;
        }
        if(minQueue.isEmpty()){
            return maxQueue.peek() ;
        }
        if(maxQueue.isEmpty()){
            return minQueue.peek() ;
        }

        if(maxQueue.size() > minQueue.size()){
            return maxQueue.peek() ;
        }else if(minQueue.size() > maxQueue.size()){
            return minQueue.peek() ;
        }else{
            return (minQueue.peek() + maxQueue.peek()) / 2.0 ;
        }
    }
}

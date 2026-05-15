class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.follows = {} #hashmap follower: followees
        self.tweets = {} #hashmap author: queue of last 10 tweets
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId not in self.tweets:
            self.tweets[userId] = deque()

        if len(self.tweets[userId]) == 10:
            self.tweets[userId].popleft()
        
        self.tweets[userId].append(((self.timestamp, tweetId)))

        

    def getNewsFeed(self, userId: int) -> List[int]: #!O(F*10*log10) but T is at most 10 --> O(F)
    #!we could also have done the K-WAY MERGE extracting everytime the most recent tweet for each followee --> O(Flog10 + 10log10) if we prune only 10 starting tweets and the apply K-WAY-MERGE
        min_heap = []

        if userId not in self.follows:
            self.follows[userId] = set()
            self.follows[userId].add(userId)
        

        for followee in self.follows[userId]:
            if followee not in self.tweets:
                continue
            for tweet in self.tweets[followee]:
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, tweet) #O(1) in practice (cap at 10)
                elif tweet[0] > min_heap[0][0]:
                    heapq.heapreplace(min_heap, tweet) #O(1) in practice (cap at 10)
        
        min_heap.sort(key=lambda x: x[0], reverse=True) #O(1) in practice (cap at 10)
        res = [tweet[1] for tweet in min_heap]
        
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
            self.follows[followerId].add(followerId)

        if followeeId not in self.follows[followerId]:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId] and followeeId != followerId:
            self.follows[followerId].remove(followeeId)
        

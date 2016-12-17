class User(object):
    def __init__(self,userid):
        self.userid=userid
        self.tweet=[]
        self.follow=[]
    def PostTweet(self,t):
        self.tweet.append(t)
    def Follow(self,userid):
        self.follow.append(userid)
        
class Tweet(object):
    def __init__(self,tweetid,seq):
        self.tweetid=tweetid
        self.seq=seq
        
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users=[]
        self.index={}#userid对应的对象索引
        self.existed=[]
        self.seq=0
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        t=Tweet(tweetId,self.seq)
        if(userId in self.existed):
            #用户已经存在
            index=self.index[userId]
            self.users[index].PostTweet(t)
        else:
            #用户不存在
            self.existed.append(userId)
            u=User(userId)
            u.PostTweet(t)
            self.users.append(u)
            self.index[userId]=len(users)-1
        self.seq=self.seq+1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users
        who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        feed=[]
        index=self.index[userId]
        follow=self.users[index].follow
        feed.append(self.users[index].tweet)
        
        for i in follow:
            index=self.index[i]
            feed.append(self.users[index].tweet)
        feed.sort(key=lambda x:x.seq)
        return feed[0:10]
        
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        index=self.index[followerId]
        follow=self.users[index].follow
        if(followeeId  in follow):
            pass
        else:
            self.users[index].Follow(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
 obj.unfollow(followerId,followeeId)       :type followeeId: int
        :rtype: void
        """
        index=self.index[followerId]
        follow=self.users[index].follow
        if(followeeId not in follow):
            pass
        else:
            follow.pop(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
def test():
    Twitter twitter = new Twitter();

# User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 5);

# User 1's news feed should return a list with 1 tweet id -> [5].
    twitter.getNewsFeed(1);

# User 1 follows user 2.
    twitter.follow(1, 2);

# User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 6);

# User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.getNewsFeed(1);

# User 1 unfollows user 2.
    twitter.unfollow(1, 2);

# User 1's news feed should return a list with 1 tweet id -> [5],
# since user 1 is no longer following user 2.
    twitter.getNewsFeed(1);


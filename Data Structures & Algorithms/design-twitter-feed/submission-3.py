from collections import defaultdict
from heapq import heappush, heappop

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)

        # add latest tweets from all users followed by userId to heap
        # heap should be sorted by max timestamp first (maxHeap)
        maxHeap = []
        for followeeId in self.following[userId]:
            tweetsLen = len(self.tweets[followeeId])
            lastTweetIdx = tweetsLen - 1
            if lastTweetIdx >= 0:
                timestamp, tweetId = self.tweets[followeeId][lastTweetIdx]
                # add lastTweetIdx to heap to know to do -1 for next most recent
                # tweet by user "followeeId"
                heappush(maxHeap, (-timestamp, tweetId, followeeId, lastTweetIdx))

        newsFeed = []
        # now add 10 most recent tweets to newsFeed
        # if we use first tweet from userA, add second tweet from userA
        # to the maxHeap
        while len(newsFeed) < 10 and maxHeap:
            negTimestamp, topTweetId, followeeId, lastTweetIdx = heappop(maxHeap)
            newsFeed.append(topTweetId)

            # check if more tweets by user "followeeId" exist and then add to heap
            if lastTweetIdx > 0:
                lastTweetIdx -= 1
                timestamp, tweetId = self.tweets[followeeId][lastTweetIdx]
                heappush(maxHeap, (-timestamp, tweetId, followeeId, lastTweetIdx))
        
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

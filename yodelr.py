from abc import ABC, abstractmethod
from typing import List
from collections import defaultdict
import re

class Yodelr(ABC):
    """
    The Yodelr service interface.

    This allows adding and deleting users, adding and retrieving posts
    and getting trending topics.
    """

    @abstractmethod
    def add_user(self, user_name: str) -> None:
        pass

    @abstractmethod
    def add_post(self, user_name: str, post_text: str, timestamp: int) -> None:
        pass

    @abstractmethod
    def delete_user(self, user_name: str) -> None:
        pass

    @abstractmethod
    def get_posts_for_user(self, user_name: str) -> List[str]:
        pass

    @abstractmethod
    def get_posts_for_topic(self, topic: str) -> List[str]:
        pass

    @abstractmethod
    def get_trending_topics(self, from_timestamp: int, to_timestamp: int) -> List[str]:
        pass

class Solution(Yodelr):
    """Implementation of the Yoderl interface"""

    def __init__(self):
        self.users = defaultdict(lambda: {"post_text": [], "timestamp": []})
        self.topics = defaultdict(int)

    def add_user(self, user_name: str) -> None:
         """Adding a user to the system."""

         if user_name not in self.users:
            self.users[user_name] 

    def add_post(self, user_name: str, post_text: str, timestamp: int) -> None:
        """Given the user, add a post text with the corresponding timestamp to the system."""

        if user_name in self.users:
            if len(post_text)<=140:
                self.users[user_name]["post_text"].append(post_text)
                self.users[user_name]["timestamp"].append(timestamp)
                self.update_topics(post_text)

    
    def delete_user(self, user_name: str) -> None:
        """Delete a user in addition with the content from the system."""

        if user_name in self.users:
            del self.users[user_name]

    def get_posts_for_user(self, user_name: str) -> List[str]:
        """Fetch the post texts given the user's name sorted per timestamp in descending order."""

        if user_name in self.users:
            sorted_data = sorted(zip(self.users[user_name]["post_text"], self.users[user_name]["timestamp"]), key=lambda x: x[1], reverse=True)
            return [post for post, _ in sorted_data]

        return []
    
    def get_posts_for_topic(self, topic: str) -> List[str]:
        """Fetch the post texts given a topic sorted per timestamp in descending order."""
        
        post_texts = []
        for user_name, user_data in self.users.items():
            user_posts = [(post_text, timestamp) for post_text, timestamp in zip(user_data["post_text"], user_data["timestamp"]) if topic in post_text]
            sorted_user_posts = sorted(user_posts, key=lambda x: x[1], reverse=True)
            sorted_post_texts = [post_text for post_text, _ in sorted_user_posts]
            post_texts.extend(sorted_post_texts)

        return post_texts
    
    def get_trending_topics(self, from_timestamp: int, to_timestamp: int) -> List[str]: 
        """Fetch the topics given a timeframe according to timestamps, sorted on descending mention
        count primarily, alphabetically on topic secondarily."""

        topics = defaultdict(int)
        for user_data in self.users.values():
            for post_text, timestamp in zip(user_data["post_text"], user_data["timestamp"]):
                if from_timestamp <= timestamp <= to_timestamp:
                    topics_in_post = set([topic[1:] for topic in re.findall("#\w+", post_text)])
                    for topic in topics_in_post:
                        if topic not in topics_in_post:
                            topics[topic] = 1
                        else:
                            topics[topic] += 1

        trending_topics = sorted(topics.keys(), key=lambda x: (topics[x], x), reverse=True)
        return trending_topics[:5]

    def update_topics(self, post_text: str) -> None:
        """Count the frequency of each topic according to the given pattern."""
        
        topics = set([topic[1:] for topic in re.findall("#\w+", post_text)])
        for topic in topics:
            if topic not in self.topics:
                self.topics[topic]=1
            else:
                self.topics[topic]+=1

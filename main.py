from flask import Flask, request, jsonify
from yodelr import Solution

class YodelrApp:
    def __init__(self):
        """Initialise the Flask API."""

        self.app = Flask(__name__)
        self.solution = Solution()
        self.setup_routes()

    def setup_routes(self):
        """Setup the HTTP requests."""

        self.app.route('/addUser', methods=['POST'])(self.add_user)
        self.app.route('/addPost', methods=['POST'])(self.add_post)
        self.app.route('/deleteUser', methods=['DELETE'])(self.delete_user)
        self.app.route('/getPostsForUser', methods=['GET'])(self.get_posts_for_user)
        self.app.route('/getPostsForTopic', methods=['GET'])(self.get_posts_for_topic)
        self.app.route('/getTrendingTopics', methods=['GET'])(self.get_trending_topics)

    def run(self):
        """Execute the interface."""

        self.app.run(debug=True)

    def add_user(self):
        """Adding a user to the system."""

        data = request.get_json()
        userName = data['user_name']
        self.solution.add_user(userName)
        return jsonify({'message': 'User added successfully'}), 200

    def add_post(self):
        """Given the user, add a post text with the corresponding timestamp to the system."""

        data = request.get_json()
        userName = data.get('user_name')
        postText = data.get('post_text')
        timestamp = data.get('timestamp')
        self.solution.add_post(userName, postText, timestamp)
        return jsonify({'message': 'Post added successfully'}), 200

    def delete_user(self):
        """Delete a user in addition with the content from the system."""

        userName = request.args.get('user_name')
        self.solution.delete_user(userName)
        return jsonify({'message': 'User deleted successfully'}), 200

    def get_posts_for_user(self):
        """Fetch the post texts given the user's name sorted per timestamp in descending order."""

        user_name = request.args.get('user_name')
        if user_name:
            posts = self.solution.get_posts_for_user(user_name)
            return jsonify({'posts': posts}), 200
        else:
            return jsonify({'error': 'Missing user_name parameter'}), 400

    def get_posts_for_topic(self):
        """Fetch the post texts given a topic sorted per timestamp in descending order."""

        topic = request.args.get('topic')
        posts = self.solution.get_posts_for_topic(topic)
        return jsonify({'posts': posts}), 200

    def get_trending_topics(self):
        """Fetch the topics given a timeframe according to timestamps, sorted on descending mention
        count primarily, alphabetically on topic secondarily."""
        
        fromTimestamp = int(request.args.get('from_timestamp'))
        toTimestamp = int(request.args.get('to_timestamp'))
        topics = self.solution.get_trending_topics(fromTimestamp, toTimestamp)
        return jsonify({'topics': topics}), 200

if __name__ == '__main__':
    yodelr_app = YodelrApp()
    yodelr_app.run()
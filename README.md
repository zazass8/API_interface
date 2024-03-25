This work demonstrates an implementation of an API interface where users are added to a system with their corresponding post texts and subtopics within the texts. The Flask API is used to enable HTTP requests and two methods where used to test the API's correctness, using the Python requests library and the PostMan GUI.

# Instructions for testing the API interface:

Run the below command to your terminal

```pip install -r requirements.txt```

## Using the ```requests``` library:

- Open the ```test_API.ipynb```, where code of each functionality is stored in a separate cell.

- Before checking for any responses, execute the ```main.py``` file provided on your terminal.

## Using the PostMan GUI:

- Download the PostMan found in [this link](https://www.postman.com/downloads/). It is recommended as it allows you to execute requests locally.

- Before checking for any responses, execute the ```main.py``` file provided on your terminal.

- Import the ```Test_API_postman.json``` file to the GUI. The collection with the corresponding requests will appear on the left.


- For POST requests:

	- The HTTP URL given is fixed, hence only the raw JSON structure needs to be edited shown in the cells.

	- For PostMan, enter the POST tabs shown on the left right below the collection name. The HTTP URL given is fixed, hence only the body raw JSON structure needs to be edited shown in the cells. Once edited, click send and the response will be viewed on the panel below.

	- addUser

	```json
	{
	"user_name": "user1"
	}
	```

	- addPost

	```json 
	{
	"user_name": "user1",
	"post_text": "just #chilling today",
	"timestamp": 1
	}
	```


- For GET requests:

	- The fields need to be specified on the URL itself. For this, a function is created, where the user only needs to plug the required fields.

	- In PostMan, the URL is shown right above the body raw JSON structure and to the right of the request type. Once edited, click send and the response will be viewed on the panel below.

	- getPostUser (edit ```{username=user1}``` when the parameter needs to be specified)

	URL: (http://127.0.0.1:5000/getPostsForUser?user_name=user1)


	- getPostTopic (edit ```{topic=steak}``` when the parameter needs to be specified)

	URL: (http://127.0.0.1:5000/getPostsForTopic?topic=steak)


	- getTrendingTopics (edit ```{from_timestamp=1}``` and ```{to_timestamp=3}```)

	URL: (http://127.0.0.1:5000/getTrendingTopics?from_timestamp=1&to_timestamp=3)


- For any DELETE requests:

	- The fields need to be specified on the URL itself. For this, a function is created, where the user only needs to plug the required fields.

	- In PostMan, the URL is shown right above the body raw JSON structure and to the right of the request type. Once edited, click send and the response will be viewed on the panel below.

	- deleteUser (edit ```{username=user1}```)

	URL: (http://127.0.0.1:5000/deleteUser?user_name=user1)
# MongoDB Connection for Streamlit (experimental_connection)
This piece of code provides a Streamlit-based MongoDB connection class that allows you to interact with a MongoDB database seamlessly. It's designed to simplify the process of connecting to a MongoDB server and performing common operations like adding, listing, finding, and inserting documents into collections

## Usage 
**Installation**: Make sure you have the required libraries installed by running the following command:
```console
pip install -r requirements.txt
```
**Setting up the MongoDB URL**: Before using the connection class, you need to set up the MongoDB URL. You can either pass the URL as an argument while creating an instance of the class or use Streamlit secrets to store it securely. Here's how you can set it up in Streamlit secrets, Save the follwing in  *./streamlit/secrets.toml file*
```toml
url = "mongodb+srv://<username>:<password>@<cluster_name>.8mfbkxr.mongodb.net/?retryWrites=true&w=majority"
```
Now set the url to st.secrets by
```python
st.secrets["url"] = "your_mongodb_url"
```
**Establishing Connection**: We establish the connection using the experimental_connection from streamlit
```python
conn = st.experimental_connection("mongo",type = connection_type, database = "db_name")
```
## Methods
### add_collection(collection_name)
**Description**: Adds a new collection to the connected database.
**Parameters**:
*collection_name (str)*: The name of the new collection to be added.
Returns: The MongoDB collection object representing the newly added collection.
### list_collection()
__Description__: Lists all the collections available in the connected database.
__Returns__: A list of collection names.
### current_collection(collection_name)

Description: Sets the current collection for subsequent operations.
__Parameters__:
__collection_name (str)__: The name of the collection to set as the current collection.
__Returns__: The MongoDB collection object representing the current collection.
### find()
__Description__: Fetches all documents from the current collection.
__Returns__: A cursor object representing the query results.
### insert(record)
__Description__: Inserts a single document into the current collection.
__Parameters__: *record (dict)*: The document to be inserted into the collection.


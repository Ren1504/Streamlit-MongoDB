import streamlit as st
from database import mongo_connection
import base64


st.set_page_config(layout = "wide",page_icon = "🖼️", page_title = "Image Wall")

tab1,tab2 = st.tabs(['App','How it works'])

with tab1:

    st.title("IMAGE WALL")

    conn = st.experimental_connection("mongo",type = mongo_connection, database = "IMAGES")


    conn.current_collection("image_boi")

    
    x = conn.find()


    col1, col2 = st.columns(2)

    with col1:
        st.subheader("What's this about")
        st.write("""Share your stunning photographs, mesmerizing artworks, and awe-inspiring snapshots for the entire community to see. The image wall format ensures that your posts stand out and receive the attention they deserve.""")
        st.image("https://cdn.editage.com/insights/editagecom/production/styles/detail_page_image/public/A%20forum%20for%20researchers%20by%20researchers_resized.jpg?itok=e7U2KA-W")


    with col2:
        name = st.text_input(
            "Enter Name"
        )

        caption = st.text_input(
            "Enter Caption"
        )

        image = st.file_uploader("upload an image",type=['png','jpg','jpeg'])

        if image:
            st.write("Preview")
            st.image(image,width = 250,caption = caption)
            my_string = base64.b64encode(image.read())

        if st.button("Post"):

            if image is  None or name == "":
                st.error("Missing name or image")

            else:
                record = {"Name":name,"Caption":caption,"Image":my_string}
                conn.insert(record)
                st.experimental_rerun()



    data = list(x)

    n_pics = len(data)


    st.title("What have others posted")

    try:
        if data:      
            col1, col2, col3 = st.columns(3)
            columns = [col1,col2,col3]

            for i in range(n_pics):

                with columns[i%3]:
                    im = data[i]['Image']
                    decode = base64.b64decode(im)
                    st.subheader(data[i]["Name"])
                    st.image(decode,caption = data[i]["Caption"], width=400)

    except:
        st.error("No data in database")

with tab2:
    st.title("Documentation")
    st.subheader("How the App works")
    st.write(""" The user is allowed to post a image in the app and the app is connected to the
             MongoDB server. It then retrieves the images from the database and allows the others users to
             see what they have posted along with their name and""")    
    
    st.markdown("""# MongoDB Connection for Streamlit (experimental_connection)
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

__Description__: Sets the current collection for subsequent operations.
__Parameters__:
__collection_name (str)__: The name of the collection to set as the current collection.
__Returns__: The MongoDB collection object representing the current collection.
### find()
__Description__: Fetches all documents from the current collection.
__Returns__: A cursor object representing the query results.
### insert(record)
__Description__: Inserts a single document into the current collection.
__Parameters__: *record (dict)*: The document to be inserted into the collection.

""")

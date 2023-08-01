import pymongo
from pymongo.mongo_client import MongoClient
import streamlit as st
from streamlit.connections import ExperimentalBaseConnection


class mongo_connection(ExperimentalBaseConnection[pymongo.MongoClient]):
    def __init__(self,database:str,**kwargs):
        super().__init__(**kwargs)
        self.database = database
        self.collection = None
    
    def _connect(self, **kwargs) -> MongoClient:
        if 'url' in kwargs:
            url = kwargs.pop('url')
        else:
            url = st.secrets.get("url")
            client = MongoClient(url)

        return client

    def list_collection(self):
        db = self._instance[self.database]
        return db.list_collection_names()

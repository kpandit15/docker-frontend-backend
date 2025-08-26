import os

import streamlit as st
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd

load_dotenv()

# MongoDB connection
username = os.getenv("MONGO_INITDB_ROOT_USERNAME")
password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
mongodb_host = os.getenv("ME_CONFIG_MONGODB_SERVER", "mongo-db")
print("Environment variables loaded:")
print("------------------------------------------------------------------------------------")
print(f"Connecting to MongoDB at {mongodb_host}, with user {username}, password {password}")
client = MongoClient(f"mongodb://{username}:{password}@{mongodb_host}:27017/")
db = client["users-db"]
collection = db["user"]


def insert_user(name, location, email, phone):
    user = {"name": name, "location": location, "email": email, "phone": phone}
    collection.insert_one(user)


def get_all_users():
    return list(collection.find({}, {"_id": 0}))


def main():
    st.title("User Information Form")

    # User input fields
    name = st.text_input("Name")
    location = st.text_input("Location")
    email = st.text_input("Email ID")
    phone = st.text_input("Phone Number")
    
    if st.button("Insert User"):
        if name and location and email and phone:
            insert_user(name, location, email, phone)
            st.success("User inserted successfully!")
        else:
            st.error("Please fill all fields.")

    if st.button("Show All Users"):
        users = get_all_users()
        df = pd.DataFrame(users)
        st.subheader("All Users in Database")
        st.dataframe(df)


if __name__ == "__main__":
    main()

##############################################
# This file is used to INTERACT with setup databases
# Run setup.py file if databases are empty
# 
# Three databases are created in NoSQL DBMS (MongoDB): 
# UsersDatabase, VideosDatabase, CommentsDatabase
# 
# 
# 
##############################################

from pymongo import MongoClient

def connect_to_mongodb():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    return client

# Example: Functions to interact with databases
def get_all_users():
    users_db = client["UsersDatabase"]
    return list(users_db["Users"].find({}))

def get_videos_by_category(category):
    videos_db = client["VideosDatabase"]
    return list(videos_db["Videos"].find({"category": category}))

def add_comment(video_id, user_id, comment_text):
    comments_db = client["CommentsDatabase"]
    comment_id = comments_db["Comments"].estimated_document_count() + 1001
    comments_db["Comments"].insert_one({
        "comment_id": comment_id,
        "video_id": video_id,
        "user_id": user_id,
        "comment": comment_text
    })
    return f"Comment added with ID {comment_id}"

# Main Interaction
if __name__ == "__main__":
    # Connect to NoSQL MongoDB
    client = connect_to_mongodb()

    # Example: Retrieve all users
    users = get_all_users()
    print("All Users:")
    for user in users:
        print(user)

    # Example: Retrieve videos by category
    category = "Category A"
    videos = get_videos_by_category(category)
    print(f"\nVideos in category '{category}':")
    for video in videos:
        print(video)

    # Example: Add a new comment
    new_comment = add_comment(video_id=101, user_id=1, comment_text="Great video!")
    print(f"\n{new_comment}")

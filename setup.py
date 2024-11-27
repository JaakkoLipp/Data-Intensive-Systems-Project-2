##############################################
# This file is used to populate the databases with sample data
# Run this file if databases are empty
# it should populate A NoSQL DBMS (MongoDB) with sample data and another SQL DBMS
# 
# 
# 
# 
# 
##############################################

from pymongo import MongoClient

def populate_databases():
    # call nosql populate function (and sql populate function)
    populate_databases_mongodb()

def populate_databases_mongodb():
    
    """
    Populates MongoDB databases with sample data for users, videos, and comments.
    This function connects to a MongoDB server running on localhost at port 27017
    and populates three databases with sample data:
    1. UsersDatabase:
        - Collection: Users
        - Sample Data: 20 users with fields 'user_id', 'name', and 'email'.
    2. VideosDatabase:
        - Collection: Videos
        - Sample Data: 20 videos with fields 'video_id', 'title', 'category', and 'views'.
    3. CommentsDatabase:
        - Collection: Comments
        - Sample Data: 20 comments with fields 'comment_id', 'video_id', 'user_id', and 'comment'.
    4. ChannelDatabase:
        - Collection: Channels
        - Sample Data: 20 channels with fields 'channel_id', 'channel_name', 'description', 'user_id', 'subscriber_count'.
    5. NotificationsDatabase:
        - Collection: Notifications
        - Sample Data: 20 notifications with fields 'user_id', 'notification_id', 'text', 'date'.
    6. PlaylistDatabase:
        - Collection: Playlists
        - Sample Data: 20 playlists with fields 'playlist_id', 'name', 'user_id', 'video_id', 'date_created'.
    Prints messages indicating the start and completion of the database population process.
    """

    print("Populating databases with sample data...")
    # Connect to MongoDB server
    client = MongoClient("mongodb://localhost:27017/")

    # Database 1: Users
    users_db = client["UsersDatabase"]
    users_data = [
        {"user_id": i, "name": f"User{i}", "email": f"user{i}@example.com"}
        for i in range(1, 21)
    ]
    users_db["Users"].insert_many(users_data)

    # Database 2: Videos
    videos_db = client["VideosDatabase"]
    videos_data = [
        {"video_id": i, "title": f"Video{i}", "category": "Category A", "views": i * 100}
        for i in range(101, 121)
    ]
    videos_db["Videos"].insert_many(videos_data)

    # Database 3: Comments
    comments_db = client["CommentsDatabase"]
    comments_data = [
        {"comment_id": i, "video_id": 101, "user_id": 1, "comment": f"Comment {i}"}
        for i in range(1001, 1021)
    ]
    comments_db["Comments"].insert_many(comments_data)

    # Database 4: Channels
    channel_db = client["ChannelDatabase"]
    channel_data = [
        {"channel_id": i, "channel_name": f"Channel {i}", "description": f"describtion {i}", "user_id": 3, "subscriber_count": 4000 * i }
        for i in range(1, 21)
    ]
    channel_db["Channels"].insert_many(channel_data)

    # Database 5: Notifications
    notification_db = client["NotificationDatabase"]
    notification_data = [
        {"user_id": 9, "notification_id": i, "text": f"Text {i}", "date": f"{3+1}.04.2024"}
        for i in range(1, 21)
    ]
    notification_db["Notifications"].insert_many(notification_data)

    # Database 6: Playlists
    playlist_db = client["PlaylistDatabase"]
    playlist_data = [
        {"playlist_id": i, "Name": f"Name {i}", "user_id": 6, "video_id": f"{100+i}", "date_created": f"{5+1}.06.2021"}
        for i in range(1, 21)
    ]
    playlist_db["Playlists"].insert_many(playlist_data)


    print("Databases populated with sample data.")

if __name__ == "__main__":
    populate_databases()

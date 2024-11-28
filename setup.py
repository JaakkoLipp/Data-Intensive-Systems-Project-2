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

    print("Populating databases with sample data...")
    # Connect to MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    # Define the regional databases
    REGIONS = ["EU", "NA", "SA", "AS", "OCE"]

    for region in REGIONS:
        db = client[region]  # Create/Access the regional database

        # Users collection
        users_data = [
            {"user_id": i, "name": f"User{i}_{region}", "email": f"user{i}@{region.lower()}.example.com"}
            for i in range(1, 21)
        ]
        db["Users"].insert_many(users_data)

        # Channels collection
        channels_data = [
            {"channel_id": i, "channel_name": f"Channel{i}_{region}", "description": f"Description {i}_{region}", 
             "user_id": i, "subscriber_count": 100 * i}
            for i in range(1, 21)
        ]
        db["Channels"].insert_many(channels_data)

        # Comments collection
        comments_data = [
            {"comment_id": i, "video_id": i, "user_id": i, "comment": f"Comment {i} from {region}"}
            for i in range(1, 21)
        ]
        db["Comments"].insert_many(comments_data)

        # Videos collection
        videos_data = [
            {"video_id": i, "title": f"Video{i}_{region}", "category": f"Category_{i % 5}", "views": i * 100}
            for i in range(1, 21)
        ]
        db["Videos"].insert_many(videos_data)

        # Notifications collection
        notifications_data = [
            {"notification_id": i, "user_id": i, "text": f"Notification {i} for {region}", "date": f"2024-11-{i:02}"}
            for i in range(1, 21)
        ]
        db["Notifications"].insert_many(notifications_data)

        playlist_data = [
            {"playlist_id": i, "user_id": i, "playlist_name": f"Playlist{i}_{region}"}
            for i in range(1, 21)
        ]
        db["Playlists"].insert_many(playlist_data)

        print(f"Populated {region} database with sample data.")

    print("All regional databases have been populated.")







if __name__ == "__main__":
    populate_databases()

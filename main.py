##############################################
# This file is used to INTERACT with setup databases
# Run setup.py file if databases are empty
# 
# Six databases are created in NoSQL DBMS (MongoDB): 
# UsersDatabase, VideosDatabase, CommentsDatabase, ChannelDatabase, NotificationDatabase, PlaylistDatabase
# 
# 
# 
##############################################

import frontend

# this could be implemented:
#from setup import populate_databases

from pymongo import MongoClient

# Function to connect to MongoDB
def get_database(region):
    """
    Connect to the specified regional database.
    :param region: The name of the region (e.g., 'EU').
    :return: The MongoDB database object.
    """
    client = MongoClient("mongodb://localhost:27017/")
    return client[region]

# Query 1: Find all users in a specific region
def find_all_users(region):
    db = get_database(region)
    users = list(db["Users"].find())
    return users

# Query 2: Find all videos in a specific region
def find_all_videos(region):
    db = get_database(region)
    videos = list(db["Videos"].find())
    return videos

# Query 3: Add a video into a specific region
def add_video(region, video_data):
    db = get_database(region)
    db["Videos"].insert_one(video_data)
    print("Video added successfully.")

# Query 4: Delete a video from a specific region
def delete_video(region, video_id):
    db = get_database(region)
    result = db["Videos"].delete_one({"video_id": video_id})
    if result.deleted_count > 0:
        print("Video deleted successfully.")
    else:
        print("Video not found.")

# Main Program
def testui():
    while True:
        print("\n\n----- T E S T I N  U I -----\n\n")
        print("Select a query to execute:")
        print("1. Find all users in a specific region")
        print("2. Find all videos in a specific region")
        print("3. Add a video into a specific region")
        print("4. Delete a video from a specific region")
        print("5. Exit\n")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            region = input("Enter the region name (e.g., EU, NA, AS, SA, OCE): ")
            users = find_all_users(region)
            print("\nUsers in", region, ":")
            for user in users:
                print(user)

        elif choice == "2":
            region = input("Enter the region name (e.g., EU, NA, AS, SA, OCE): ")
            videos = find_all_videos(region)
            print("\nVideos in", region, ":")
            for video in videos:
                print(video)

        elif choice == "3":
            region = input("Enter the region name (e.g., EU, NA, AS, SA, OCE): ")
            video_id = int(input("Enter video ID: "))
            title = input("Enter video title: ")
            category = input("Enter video category: ")
            views = int(input("Enter number of views: "))
            video_data = {
                "video_id": video_id,
                "title": title,
                "category": category,
                "views": views,
            }
            add_video(region, video_data)

        elif choice == "4":
            region = input("Enter the region name (e.g., EU, NA, AS, SA, OCE): ")
            video_id = int(input("Enter the video ID to delete: "))
            delete_video(region, video_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


# Main Interaction
if __name__ == "__main__":
    testui()
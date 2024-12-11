##############################################
# This file is used to INTERACT with setup databases
# Run setup.py file if databases are empty
# 
# Collections in NoSQL DBMS (MongoDB): 
# Users, Channels, Comments, Videos, Notifications, Playlists
##############################################

from pymongo import MongoClient

# MongoDB Setup
def get_mongo_database(region):
    """
    Connect to the specified regional MongoDB database.
    :param region: The name of the region (e.g., 'EU').
    :return: The MongoDB database object.
    """
    client = MongoClient("mongodb://localhost:27017/")
    return client[region]

# ---------------------------------
# SIMPLE QUERIES (Single Database)
# ---------------------------------

# Find all users in a specific region
def find_all_users(region):
    db = get_mongo_database(region)
    users = list(db["Users"].find())
    return users

# Add a video to a specific region
def add_video(region, video_data):
    db = get_mongo_database(region)
    db["Videos"].insert_one(video_data)
    print("Video added successfully.")

# Find top videos in a specific region
def find_top_videos(region, limit=5):
    db = get_mongo_database(region)
    top_videos = list(db["Videos"].find().sort("views", -1).limit(limit))
    return top_videos

# Find all comments on a video in a specific region
def find_comments_on_video(region, video_id):
    db = get_mongo_database(region)
    comments = list(db["Comments"].find({"video_id": video_id}))
    return comments

# Add a comment to a video in a specific region
def add_comment(region, video_id, user_id, comment_text):
    db = get_mongo_database(region)

    # Generate a unique comment_id based on the existing data
    last_comment = db["Comments"].find_one(sort=[("comment_id", -1)])  # Get the last comment
    comment_id = (last_comment["comment_id"] + 1) if last_comment else 1

    # Create the comment document
    comment_data = {
        "comment_id": comment_id,
        "video_id": video_id,
        "user_id": user_id,
        "comment": comment_text,
    }

    # Insert the comment into the Comments collection
    db["Comments"].insert_one(comment_data)
    print(f"Comment added successfully with comment_id {comment_id}.")

# -----------------------------------------
# COMPLEX QUERIES (Multiple Databases)
# -----------------------------------------

# Find all users across all regions
def find_all_users_across_regions():
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    all_users = []
    for region in regions:
        db = get_mongo_database(region)
        users = list(db["Users"].find())
        for user in users:
            user["region"] = region  # Add region information
        all_users.extend(users)
    return all_users

# Find top videos across all regions
def find_top_videos_across_regions(limit=5):
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    all_top_videos = []
    for region in regions:
        db = get_mongo_database(region)
        top_videos = list(db["Videos"].find().sort("views", -1).limit(limit))
        for video in top_videos:
            video["region"] = region  # Add region information
        all_top_videos.extend(top_videos)
    return all_top_videos

# Find channels with the most videos across regions
def find_channels_with_most_videos_across_regions():
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    channel_video_counts = {}
    for region in regions:
        db = get_mongo_database(region)
        videos = db["Videos"].aggregate([
            {"$group": {"_id": "$channel_id", "video_count": {"$sum": 1}}}
        ])
        for result in videos:
            channel_id = result["_id"]
            if channel_id not in channel_video_counts:
                channel_video_counts[channel_id] = {"video_count": 0, "regions": []}
            channel_video_counts[channel_id]["video_count"] += result["video_count"]
            channel_video_counts[channel_id]["regions"].append(region)
    return channel_video_counts

# Find users who commented on videos in multiple regions
def find_users_commented_across_regions():
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    user_activity = {}
    for region in regions:
        db = get_mongo_database(region)
        comments = db["Comments"].find()
        for comment in comments:
            user_id = comment["user_id"]
            if user_id not in user_activity:
                user_activity[user_id] = {"regions": set(), "comment_count": 0}
            user_activity[user_id]["regions"].add(region)
            user_activity[user_id]["comment_count"] += 1
    # Filter users who commented in more than one region
    multi_region_users = {
        user_id: data for user_id, data in user_activity.items() if len(data["regions"]) > 1
    }
    return multi_region_users

# Count total videos across all regions
def count_total_videos_across_regions():
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    total_videos = 0
    for region in regions:
        db = get_mongo_database(region)
        total_videos += db["Videos"].count_documents({})
    return total_videos

# Consolidate video metadata across regions
def consolidate_video_metadata_across_regions():
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    consolidated_metadata = []
    for region in regions:
        db = get_mongo_database(region)
        videos = list(db["Videos"].find({}, {"video_id": 1, "title": 1, "views": 1}))
        for video in videos:
            video["region"] = region  # Add region information
        consolidated_metadata.extend(videos)
    return consolidated_metadata

# ---------------------------------
# CLI DEMO USER INTERFACE
# ---------------------------------

def testui():
    while True:
        print("\n\n----- CLI DEMO UI -----\n\n")
        print("Select a query to execute:")
        print("1. Find all users in a specific region")
        print("2. Add a video to a specific region")
        print("3. Find top videos in a specific region")
        print("4. Find all comments on a video in a specific region")
        print("5. Add a comment to a video in a specific region")
        print("6. Find all users across all regions")
        print("7. Find top videos across all regions")
        print("8. Find channels with the most videos across regions")
        print("9. Find users who commented in multiple regions")
        print("10. Count total videos across all regions")
        print("11. Consolidate video metadata across regions")
        print("12. Exit\n")
        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            region = input("Enter the region name (e.g., EU, NA, AS, SA, OCE): ")
            users = find_all_users(region)
            print("\nUsers in", region, ":")
            for user in users:
                print(user)

        elif choice == "2":
            region = input("Enter the region name (e.g., EU, NA, AS, SA, OCE): ")
            video_id = input("Enter video ID: ")
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

        elif choice == "3":
            region = input("Enter the region name (e.g., EU, NA, AS, SA, OCE): ")
            limit = int(input("Enter the number of top videos to display: "))
            top_videos = find_top_videos(region, limit)
            print("\nTop Videos in", region, ":")
            for video in top_videos:
                print(video)

        elif choice == "4":
            region = input("Enter the region name (e.g., EU, NA, AS, SA, OCE): ")
            video_id = input("Enter video ID: ")
            comments = find_comments_on_video(region, video_id)
            print("\nComments for Video", video_id, ":")
            for comment in comments:
                print(comment)

        elif choice == "5":
            region = input("Enter the region name (e.g., EU, NA, AS, SA, OCE): ")
            video_id = int(input("Enter video ID: "))
            user_id = int(input("Enter user ID: "))
            comment_text = input("Enter comment text: ")
            add_comment(region, video_id, user_id, comment_text)

        elif choice == "6":
            users = find_all_users_across_regions()
            print("\nAll Users Across Regions:")
            for user in users:
                print(user)

        elif choice == "7":
            limit = int(input("Enter the number of top videos to display: "))
            top_videos = find_top_videos_across_regions(limit)
            print("\nTop Videos Across Regions:")
            for video in top_videos:
                print(video)

        elif choice == "8":
            channels = find_channels_with_most_videos_across_regions()
            print("\nChannels with the Most Videos Across Regions:")
            for channel_id, data in channels.items():
                print(f"Channel ID: {channel_id}, Video Count: {data['video_count']}, Regions: {', '.join(data['regions'])}")

        elif choice == "9":
            multi_region_users = find_users_commented_across_regions()
            print("\nUsers Who Commented in Multiple Regions:")
            for user_id, data in multi_region_users.items():
                print(f"User ID: {user_id}, Comment Count: {data['comment_count']}, Regions: {', '.join(data['regions'])}")

        elif choice == "10":
            total_videos = count_total_videos_across_regions()
            print(f"\nTotal Videos Across All Regions: {total_videos}")

        elif choice == "11":
            video_metadata = consolidate_video_metadata_across_regions()
            print("\nConsolidated Video Metadata Across Regions:")
            for metadata in video_metadata:
                print(metadata)

        elif choice == "12":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Main Interaction
if __name__ == "__main__":
    testui()

import tkinter as tk
from tkinter import messagebox, ttk
from pymongo import MongoClient

# MongoDB Setup function from your provided code
def get_mongo_database(region):
    client = MongoClient("mongodb://localhost:27017/")
    return client[region]

# Example queries (add more queries or adapt as needed)
def find_all_users(region):
    db = get_mongo_database(region)
    users = list(db["Users"].find())
    return users

def add_video(region, video_data):
    db = get_mongo_database(region)
    db["Videos"].insert_one(video_data)
    return "Video added successfully."

def find_top_videos(region, limit=5):
    db = get_mongo_database(region)
    top_videos = list(db["Videos"].find().sort("views", -1).limit(limit))
    return top_videos

def find_comments_on_video(region, video_id):
    db = get_mongo_database(region)
    comments = list(db["Comments"].find({"video_id": video_id}))
    return comments

def add_comment(region, video_id, user_id, comment_text):
    db = get_mongo_database(region)
    last_comment = db["Comments"].find_one(sort=[("comment_id", -1)])
    comment_id = (last_comment["comment_id"] + 1) if last_comment else 1
    comment_data = {
        "comment_id": comment_id,
        "video_id": video_id,
        "user_id": user_id,
        "comment": comment_text,
    }
    db["Comments"].insert_one(comment_data)
    return f"Comment added successfully with comment_id {comment_id}."

def find_all_users_across_regions():
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    all_users = []
    for region in regions:
        db = get_mongo_database(region)
        users = list(db["Users"].find())
        for user in users:
            user["region"] = region
        all_users.extend(users)
    return all_users

def find_top_videos_across_regions(limit=5):
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    all_top_videos = []
    for region in regions:
        db = get_mongo_database(region)
        top_videos = list(db["Videos"].find().sort("views", -1).limit(limit))
        for video in top_videos:
            video["region"] = region
        all_top_videos.extend(top_videos)
    return all_top_videos

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
    multi_region_users = {
        user_id: data for user_id, data in user_activity.items() if len(data["regions"]) > 1
    }
    return multi_region_users

def count_total_videos_across_regions():
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    total_videos = 0
    for region in regions:
        db = get_mongo_database(region)
        total_videos += db["Videos"].count_documents({})
    return total_videos

def consolidate_video_metadata_across_regions():
    regions = ["EU", "NA", "SA", "AS", "OCE"]
    consolidated_metadata = []
    for region in regions:
        db = get_mongo_database(region)
        videos = list(db["Videos"].find({}, {"video_id": 1, "title": 1, "views": 1}))
        for video in videos:
            video["region"] = region
        consolidated_metadata.extend(videos)
    return consolidated_metadata


# Tkinter Interface for interacting with the functions
class DatabaseApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MongoDB Interface")
        self.geometry("600x500")

        # Label for region selection
        self.region_label = tk.Label(self, text="Select Region:")
        self.region_label.grid(row=0, column=0, padx=10, pady=10)

        # Dropdown menu for regions
        self.region_var = tk.StringVar()
        self.region_dropdown = ttk.Combobox(self, textvariable=self.region_var, values=["EU", "NA", "SA", "AS", "OCE"])
        self.region_dropdown.grid(row=0, column=1, padx=10, pady=10)
        self.region_dropdown.set("EU")  # Default to EU

        # Label for query selection
        self.query_label = tk.Label(self, text="Select Query:")
        self.query_label.grid(row=1, column=0, padx=10, pady=10)

        # Dropdown menu for queries
        self.query_var = tk.StringVar()
        self.query_dropdown = ttk.Combobox(self, textvariable=self.query_var, values=[
            "Find all users in a region", 
            "Add a video to a region", 
            "Find top videos in a region", 
            "Find comments on a video", 
            "Add a comment", 
            "Find all users across all regions", 
            "Find top videos across all regions", 
            "Find channels with most videos", 
            "Find users who commented in multiple regions", 
            "Count total videos across all regions", 
            "Consolidate video metadata across regions"
        ])
        self.query_dropdown.grid(row=1, column=1, padx=10, pady=10)
        self.query_dropdown.set("Find all users in a region")  # Default query

        # Button to submit query
        self.submit_button = tk.Button(self, text="Submit", command=self.execute_query)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=20)

        # Text area for displaying results
        self.result_text = tk.Text(self, wrap=tk.WORD, height=10, width=50)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def execute_query(self):
        region = self.region_var.get()
        query = self.query_var.get()
        self.result_text.delete(1.0, tk.END)  # Clear previous results

        try:
            if query == "Find all users in a region":
                users = find_all_users(region)
                if users:
                    for user in users:
                        self.result_text.insert(tk.END, f"{user}\n")
                else:
                    self.result_text.insert(tk.END, "No users found.\n")

            elif query == "Add a video to a region":
                video_id = input("Enter video ID: ")
                title = input("Enter video title: ")
                category = input("Enter video category: ")
                views = int(input("Enter number of views: "))
                video_data = {"video_id": video_id, "title": title, "category": category, "views": views}
                result = add_video(region, video_data)
                self.result_text.insert(tk.END, result)

            elif query == "Find top videos in a region":
                limit = 5
                top_videos = find_top_videos(region, limit)
                if top_videos:
                    for video in top_videos:
                        self.result_text.insert(tk.END, f"{video}\n")
                else:
                    self.result_text.insert(tk.END, "No videos found.\n")

            elif query == "Find comments on a video":
                video_id = input("Enter video ID: ")
                comments = find_comments_on_video(region, video_id)
                if comments:
                    for comment in comments:
                        self.result_text.insert(tk.END, f"{comment}\n")
                else:
                    self.result_text.insert(tk.END, "No comments found.\n")

            elif query == "Add a comment":
                video_id = int(input("Enter video ID: "))
                user_id = int(input("Enter user ID: "))
                comment_text = input("Enter comment text: ")
                result = add_comment(region, video_id, user_id, comment_text)
                self.result_text.insert(tk.END, result)

            elif query == "Find all users across all regions":
                users = find_all_users_across_regions()
                if users:
                    for user in users:
                        self.result_text.insert(tk.END, f"{user}\n")
                else:
                    self.result_text.insert(tk.END, "No users found.\n")

            elif query == "Find top videos across all regions":
                limit = 5
                top_videos = find_top_videos_across_regions(limit)
                if top_videos:
                    for video in top_videos:
                        self.result_text.insert(tk.END, f"{video}\n")
                else:
                    self.result_text.insert(tk.END, "No videos found.\n")

            elif query == "Find channels with most videos":
                channels = find_channels_with_most_videos_across_regions()
                if channels:
                    for channel_id, data in channels.items():
                        self.result_text.insert(tk.END, f"Channel {channel_id} has {data['video_count']} videos across regions {data['regions']}\n")
                else:
                    self.result_text.insert(tk.END, "No channels found.\n")

            elif query == "Find users who commented in multiple regions":
                users = find_users_commented_across_regions()
                if users:
                    for user_id, data in users.items():
                        self.result_text.insert(tk.END, f"User {user_id} commented in regions {data['regions']} with {data['comment_count']} comments\n")
                else:
                    self.result_text.insert(tk.END, "No such users found.\n")

            elif query == "Count total videos across all regions":
                total_videos = count_total_videos_across_regions()
                self.result_text.insert(tk.END, f"Total videos across all regions: {total_videos}\n")

            elif query == "Consolidate video metadata across regions":
                videos = consolidate_video_metadata_across_regions()
                if videos:
                    for video in videos:
                        self.result_text.insert(tk.END, f"{video}\n")
                else:
                    self.result_text.insert(tk.END, "No videos found.\n")

        except Exception as e:
            self.result_text.insert(tk.END, f"Error: {e}\n")


# Run the app
if __name__ == "__main__":
    app = DatabaseApp()
    app.mainloop()

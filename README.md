# Data-Intensive Systems Prototype
Gropup 2

This project demonstrates a distributed database prototype inspired by YouTube's architecture using **MongoDB**, (**SQL database?**) and **Python**. The system includes three separate databases with sample data and provides tools for interaction and querying. These could be sharded and replicated if needed.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [Database Details](#database-details)
6. [Usage Instructions](#usage-instructions)
7. [Example Queries](#example-queries)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview

This prototype simulates the architecture of a distributed database system for a video-sharing platform. It includes:
- A **setup script** to populate databases with sample data.
- A **main script** for interacting with the databases to query data, add comments, and retrieve user or video information.

---

## Features

### For Developers
- Prepopulated databases with sample data (20 rows per table across 3 databases).
- Modular Python scripts for easy extension.
- Clear and logical data organization using MongoDB collections.

### For Users
- Query user data from the `UsersDatabase`.
- Fetch videos by categories from the `VideosDatabase`.
- Add comments to videos in the `CommentsDatabase`.

---

## Technologies Used
- **MongoDB**: Database system for storing and managing data.
- **Python**: For backend scripting and database interaction.
  - Libraries: `pymongo`

---

## Setup Instructions

### Prerequisites
1. **MongoDB**: Install and ensure the server is running locally or remotely.
   - [MongoDB Installation Guide](https://www.mongodb.com/docs/manual/installation/)
2. **Python 3.8+**: Ensure Python is installed.
   - [Python Installation Guide](https://www.python.org/downloads/)
3. Install required Python libraries:
   ```bash
   pip install pymongo
   ```

---

### Steps to Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/JaakkoLipp/Data-Intensive-Systems-Project-2
   cd Data-Intensive-Systems-Project-2
   ```
2. Run the setup script to populate the databases:
   ```bash
   python setup.py
   ```
3. Run the main script to interact with the databases:
   ```bash
   python main.py
   ```

---

## Database Details

The project contains **three separate MongoDB databases**:

### 1. UsersDatabase
- **Collection:** `Users`
- **Fields:** `user_id`, `name`, `email`
- **Sample Data:**
  ```json
  {"user_id": 1, "name": "Alice", "email": "alice@example.com"}
  ```

### 2. VideosDatabase
- **Collection:** `Videos`
- **Fields:** `video_id`, `title`, `category`, `views`
- **Sample Data:**
  ```json
  {"video_id": 101, "title": "Funny Cats", "category": "Animals", "views": 1000}
  ```

### 3. CommentsDatabase
- **Collection:** `Comments`
- **Fields:** `comment_id`, `video_id`, `user_id`, `comment`
- **Sample Data:**
  ```json
  {"comment_id": 1001, "video_id": 101, "user_id": 1, "comment": "This is hilarious!"}
  ```

---

## Usage Instructions

### Running the Scripts
1. **Populating Databases:**
   Run the `setup.py` script to initialize and populate the databases:
   ```bash
   python setup.py
   ```

2. **Interacting with Databases:**
   Use the `main.py` script for interaction:
   ```bash
   python main.py
   ```

---

## Example Queries

### Fetch All Users
Function:
```python
get_all_users()
```
Output:
```json
[
  {"user_id": 1, "name": "Alice", "email": "alice@example.com"},
  {"user_id": 2, "name": "Bob", "email": "bob@example.com"}
]
```

### Fetch Videos by Category
Function:
```python
get_videos_by_category("Animals")
```
Output:
```json
[
  {"video_id": 101, "title": "Funny Cats", "category": "Animals", "views": 1000}
]
```

### Add a Comment
Function:
```python
add_comment(video_id=101, user_id=1, comment_text="Great video!")
```
Output:
```plaintext
Comment added with ID 1021
```

#### Simple Queries (Single Database)
The following queries operate on a specific regional database (e.g., EU, NA, SA, AS, OCE):

- **Find all users in a specific region**: Retrieve all users stored in the Users collection of a regional database.
- **Add a video to a specific region**: Insert a new video into the Videos collection of a regional database.
- **Find the top N videos in a specific region**: Fetch the top N videos by views from the Videos collection of a regional database.
- **Find all comments on a specific video in a specific region**: Retrieve all comments associated with a specific video from the Comments collection of a regional database.
- **Add a comment to a specific video in a specific region**: Insert a new comment into the Comments collection of a regional database.

#### Complex Queries (Across Multiple Databases)
The following queries involve data aggregation or interaction across multiple regional databases:

- **Find all users across all regions**: Retrieve all users from the Users collections of all regional databases and consolidate them into a single list.
- **Find the top N videos across all regions**: Fetch the top N videos by views from the Videos collections of all regional databases.
- **Find channels with the most videos across regions**: Aggregate the number of videos per channel across the Videos collections of all regional databases and identify channels with the most videos.
- **Find users who commented on videos in multiple regions**: Identify users who have commented on videos in more than one regional database.
- **Count the total number of videos across all regions**: Calculate the total number of videos in the Videos collections of all regional databases.
- **Consolidate video metadata across all regions**: Retrieve video metadata (e.g., video ID, title, views) from the Videos collections of all regional databases and combine them into a unified list.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

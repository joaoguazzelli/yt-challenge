from decouple import config
from googleapiclient.discovery import build
import re

api_key = config('GOOGLE_API_KEY')
youtube = build("youtube", "v3", developerKey=api_key)


base_video_url = "https://www.youtube.com/watch?v=jWPOPjXjiYU&list=PLpbom12S-UaJEDmUaFfWLws317OUKNceE"


def get_playlist_id(playlist_url=base_video_url):
    pattern = r"list=([a-zA-Z0-9_-]+)"

    matches = re.findall(pattern, playlist_url)

    if matches:
        playlist_id = matches[0]
        return playlist_id
    else:
        raise


def get_video_ids(playlist_id):
    video_id_list = []
    page_token = None  # Initialize the page token

    while True:
        # Request a page of video items using the current page token
        playlist_response = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,  # Adjust the maxResults as needed
            pageToken=page_token  # Use the current page token
        ).execute()

        for playlist_item in playlist_response["items"]:
            video_id = playlist_item["snippet"]["resourceId"]["videoId"]
            video_id_list.append(video_id)

        # Check if there are more pages of results
        page_token = playlist_response.get("nextPageToken")

        # Exit the loop if there are no more pages
        if not page_token:
            break

    return video_id_list


def get_video_data(video_id):
    video_response = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    ).execute()
    if not video_response["items"]:
        return {}
    video_info = video_response["items"][0]
    title = video_info["snippet"]["title"]
    published_at = video_info["snippet"]["publishedAt"]
    views = video_info["statistics"]["viewCount"]
    likes = video_info["statistics"]["likeCount"]
    comments = video_info["statistics"]["commentCount"]
    return {
        "Video ID": video_id,
        "Title": title,
        "Views": views,
        "Likes": likes,
        "Comments": comments,
        "Published At": published_at
    }



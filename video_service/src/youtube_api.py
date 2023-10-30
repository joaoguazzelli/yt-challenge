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
    playlist_response = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50  # You may need to paginate through results if the playlist is large
    ).execute()

    video_id_list = []
    for playlist_item in playlist_response["items"]:
        video_id = playlist_item["snippet"]["resourceId"]["videoId"]
        video_id_list.append(video_id)

    return video_id_list


def get_video_data(video_id):
    video_response = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    ).execute()

    video_info = video_response["items"][0]
    title = video_info["snippet"]["title"]
    views = video_info["statistics"]["viewCount"]
    likes = video_info["statistics"]["likeCount"]
    comments = video_info["statistics"]["commentCount"]
    return {
        "Video ID": video_id,
        "Title": title,
        "Views": views,
        "Likes": likes,
        "Comments": comments
    }



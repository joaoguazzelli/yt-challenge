from video_service.src.youtube_api import *
while True:
    print("press 1 to start the program or 0 to exit")
    controller = int(input())
    if controller == 1:
        playlist_id = get_playlist_id()
        video_ids = get_video_ids(playlist_id)
        video_data = []
        for video_id in video_ids:
            video_data.append(get_video_data(video_id))

        print(video_data)
    elif controller == 0:
        break

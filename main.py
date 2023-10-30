from video_service.src.youtube_api import *
from data_processing_service.src.data_analysis import *
while True:
    print("press 1 to start the program or 0 to exit")
    controller = int(input())

    if controller == 1:
        playlist_id = get_playlist_id()
        video_ids = get_video_ids(playlist_id)
        video_data = []
        for video_id in video_ids:
            video_data.append(get_video_data(video_id))

        result = get_fund_name(video_data)
        result = order_by_publish_date(result)
        print(result)
    elif controller == 0:
        break

from googleapiclient.discovery import build

api_key = 'AIzaSyAZQVjnqFomqKOpjPA7VhRmyJzftGrRbS8'


def video_comments(video_id):
    # empty list for storing reply
    replies = []

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)

    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id
    ).execute()

    # iterate video response

    # extracting required info
    # from each result object
    for item in video_response['items']:

        # Extracting comments
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

        # counting number of reply of comment
        replycount = item['snippet']['totalReplyCount']

        # if reply is there
        if replycount > 0:

            # iterate through all reply
            for reply in item['replies']['comments']:
                # Extract reply
                reply = reply['snippet']['textDisplay']

                # Store reply is list
                replies.append(reply)

        # print comment with list of reply
        print(comment, replies, end='\n\n')

        # empty reply list
        replies = []


# Enter video id
video_url = input('Enter Youtube URL\n').split('v=')
video_id = video_url[1]
# Call function
print(video_id)
video_comments(video_id)

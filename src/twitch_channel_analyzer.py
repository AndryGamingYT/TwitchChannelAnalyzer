import os
from TwitchRequest import TwitchRequest
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def main():
    twitch_request = TwitchRequest(CLIENT_ID, CLIENT_SECRET)

    # Search channel
    channel_name = input("Insert channel name: ")
    channels = twitch_request.search_channels(channel_name, 5)
    for i, channel in enumerate(channels):
        print("{}) {}".format(i + 1, channel.display_name))

    # Select channel
    channel_index = -1
    while channel_index < 0 or channel_index > len(channels):
        channel_index = input("Select channel: ")
        channel_index = int(channel_index) - 1 if channel_index.isdigit() else -1

    channel = channels[channel_index]
    # Show channel info
    print("\nSTATISTICS OF {}:".format(channel.display_name))
    print("Follows: {}".format(twitch_request.get_follows(channel.id)))
    print("Live: {}".format("Yes" if channel.is_live else "No"))
    if (channel.is_live):
        stream = twitch_request.get_streams(channel.broadcaster_login)[0]
        print("Title: {}".format(channel.title))
        print("Game: {}".format(channel.game_name))
        print("Viewers: {}".format(stream.viewer_count))
        print("Started at: {}".format(channel.started_at.strftime("%d/%m/%Y %H:%M:%S")))
        print("Language: {}".format(stream.language))


if __name__ == "__main__":
    main()

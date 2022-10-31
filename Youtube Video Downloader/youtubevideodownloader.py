'''
    A python script to download youtube videos
'''

from pytube import YouTube

def main():
    ''' Main function '''
    # Ask for the link
    link = input("Enter the link: ")

    # Ask for the path
    path = input("Enter the path: ")

    # Check if the path exists
    if not os.path.exists(path):
        os.makedirs(path)

    # Download the video
    YouTube(link).streams.first().download(path)

    # Print a message
    print("Video downloaded successfully")

if __name__ == "__main__":
    main()
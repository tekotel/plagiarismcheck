import feedparser

from urllib.parse import urlparse


def main():
    try:
        # Get input from the user and parse it
        user_input = input("Enter the RSS Feed URL: ")
        url_data = urlparse(user_input)

        """
        `scheme` contains the protocol used for accessing the resource (e.g., 'http' or 'https').
        `netloc` contains the network location of the resource. This includes a domain name and option to choose which have greater impact on next.
        """
        if not (url_data.scheme and url_data.netloc):  
            raise ValueError()   # Raise error if invalid URL

        feed = feedparser.parse(user_input) 
        for entry in feed.entries:
            print('Title:\n', entry.title)  
            print('Link:\n', entry.link)
            print('Description:\n', entry.description)

    except Exception as e:
        print("An error occurred Invalid URL", str(e))


if __name__ == '__main__':
    main()

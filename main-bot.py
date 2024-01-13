import time
import requests
from mastodon import Mastodon
from bs4 import BeautifulSoup 

access_token = "Your Access Token Here."
api_url = "Your API_URL Here."
username = 'Your Username Here.'

discord_webhook_url = 'Your Webhook URL Here.'
sent_posts = set()

def get_five_newest_posts(api_url, access_token, username):
    mastodon = Mastodon(api_base_url=api_url, access_token=access_token)

    # Get user ID by username
    user_id = mastodon.account_search(username)[0]['id']

    # Get user's timeline
    timeline = mastodon.account_statuses(user_id, limit=1)

    # Extract the content and media links of each valid status
    newest_posts = []
    for status in timeline:
        post_content = status['content']

        # Remove <p> tags from the post content
        soup = BeautifulSoup(post_content, 'html.parser')
        clean_content = soup.get_text()
        
        if clean_content.strip() and status['id'] not in sent_posts:
            
            media_attachments = status.get('media_attachments', [])
            media_links = [attachment['url'] for attachment in media_attachments]

            # Combine content and media links
            post_with_media = {'content': clean_content, 'media_links': media_links, 'post_id': status['id']}
            newest_posts.append(post_with_media)

    return newest_posts

def send_to_discord_webhook(webhook_url, post_content, media_links):
    embed_data = {
        'title': 'New Post',
        'description': post_content,
        'color': 0x42f5c5,  # Optional: Set the color of the embed
    }

    # Add media links as images to the embed
    if media_links:
        embed_data['image'] = {'url': media_links[0]}  

    data = {
        'content': ' ',
        'embeds': [embed_data],
    }

    requests.post(webhook_url, json=data)

while True:
    posts = get_five_newest_posts(api_url, access_token, username)

    for post in posts:
        
        send_to_discord_webhook(discord_webhook_url, post['content'], post['media_links'])

        # Add the post ID to the set to mark it as sent
        sent_posts.add(post['post_id'])

    
    time.sleep(10)




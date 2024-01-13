# mastodon-post-reader
A Bot / API That Sends the Most Recent Posts From one Account to a Discord Webhook
## Example
<img src="https://media.discordapp.net/attachments/1180803359129747507/1195849693473816586/image.png?ex=65b57cd0&is=65a307d0&hm=bd3ec84ff18560c433008b9205ad0cd9f97a3a7ed828f8c7e5b3087d1b556df3&=&format=webp&quality=lossless">

### How to setup to your Unique Mastodon Account.

**Step 1**
<img src="https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/0fa87975-ca25-4365-aa78-81d28f9d7442">
<br>
Create a Mastodon Account, And Open Settings To the "Development" Tab.

**Step 2**
<img src="https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/650e2b56-5bf9-4161-a17f-67a59c333b70">
<br>
Create a New Application.

**Step 3**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/c75f1121-1a4d-4f0b-b350-d7db280c6f00)
<br>
Set the Application Name, And Hit Submit.

**Step 4**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/0e06bc5f-71ec-4987-a397-367d6e740456)
<br>
Click the Hyperlinked Text.

**Step 5**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/2206df39-3225-4249-8edf-3aba2c27d94b)
<br>
Copy The Access Key / Token.

**Step 6**
Download And Open "bot-main.py"

**Step 7**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/8eb88911-a453-43e3-8aab-413a4bdaa760)
<br>
Paste the Access Key / Token we copied Before, to here.

**Step 8**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/b1eba64b-b87e-4b9b-a256-b4b5b2d33ae6)
<br>
Open Discord, Goto Your Server, Right Click on a Channel, Click Settings, and Goto Integrations And Create a Webhook.

**Step 9**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/a4219c15-e245-464f-adcb-95e278f3a0c1)
<br>
Copy That Webhook URL, And Paste it in discord_webhook_url in bot-main.py

**Step 10**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/6f739f63-f73b-4938-8ba7-324ab107ea02)
<br>
Find your API Url In your Profile. (it Should be after the username@ Part.)\

**Step 11**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/9ac716a3-bcb6-4821-91b4-d2a228c649aa)
<br>
Paste it in Like So. (replace troetbu.de with your own.)

**Step 12**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/d21ef9e1-fb86-4e9f-bb2a-534cad5d532d)
<br>
Find The Account's Username For the account you wanna use for this. (That_one_guy is just a example, he is a great guy tho)

**Step 13**
![image](https://github.com/dot-wuid/mastodon-post-reader/assets/125801210/a31c4109-51de-4617-9bb5-e7eff6275d5f)
<br>
After you paste in the Username, it should look a little something like this, but not the exact same.

**Step 14**
Hit Run! (Or type "python3 bot-main.py" in terminal) I Recommend you run this on a server 24/7 so you dont have to bring it online for every post you send.

**Note:** 
Make sure to NOT Leak stuff like discord webhook url, or access tokens, Since those shouldnt be shared publicly.
anyway enjoy using this, ill update it more soon with post links, better image support and more!

### Required Libraries
**bs4 / BeautifulSoup** "pip install bs4"
**mastodon.py** "pip install mastodon.py"
**requests** "pip install requests"







# instagram_downloader

You can use this app for downnload Instagram posts.

## Installation

```bash
git clone https://github.com/azizbekQozoqov/instagram_downloader.git
```
## Installing packages
```bash
pip install -r instagram_downloader/requirements.txt
```

## Usage

```python
from instagram_downloader.app import InstaDownload

instagram_post_url = 'https://www.instagram.com/p/CRD7T9NFzQ8/'

post = InstaDownload(url=instagram_post_url, target='down').download_and_get_path()

print(post)
```

## Output
```bash
{'type': 'in.success', 'data': {'path': 'C:\\Users\\user\\Desktop\\project\\instagram_downloader_telegram_bot\\instagram_downloader\\down'}}
```
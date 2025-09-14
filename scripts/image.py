import os
from rich import print
from rich.console import Console
from rich.table import Table
import requests
from urllib.parse import urlparse
from datetime import datetime

console = Console()

script_path = os.path.abspath(__file__)
cwd = os.path.dirname(script_path)
log_directory = os.path.abspath(os.path.join(cwd, "logs"))


def download_from_clipboard(path="./user_media/", name=None):
    from PIL import ImageGrab

    im = ImageGrab.grabclipboard()
    if im is None:
        raise ValueError("No image found in clipboard!")

    os.makedirs(path, exist_ok=True)
    name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png") if name is None else name
    save_path = os.path.join(path, name)
    im.save(save_path)
    return save_path


def is_imgur_url(url):
    parts = urlparse(url)
    return parts.netloc in ("i.imgur.com", "imgur.com")


def download_imgur_image(url, output_dir="./user_media/"):
    try:
        if not is_imgur_url(url):
            raise ValueError(
                "Invalid Imgur URL. Must start with https://i.imgur.com/ or https://imgur.com/"
            )

        image_name = url.split("/")[-1]
        final_url = f"https://i.imgur.com/{image_name}.png"

        response = requests.get(
            final_url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
            },
            stream=True,
        )
        response.raise_for_status()

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save the image
        output_path = os.path.join(output_dir, image_name)
        with open(output_path, "wb") as image_file:
            for chunk in response.iter_content(chunk_size=8192):
                image_file.write(chunk)

        print(f"Image downloaded successfully: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

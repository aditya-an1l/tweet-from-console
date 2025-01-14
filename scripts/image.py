from rich import print
from rich.console import Console
from rich.table import Table
import argparse


import requests
import os

console = Console()

script_path = os.path.abspath(__file__)
cwd = os.path.dirname(script_path)
log_directory = os.path.abspath(os.path.join(cwd, "logs"))


def download_imgur_image(url, output_dir):
    try:
        if not url.startswith("https://i.imgur.com/"):
            raise ValueError("Invalid Imgur URL. Must start with https://i.imgur.com/")

        image_name = url.split("/")[-1]

        response = requests.get(
            url,
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

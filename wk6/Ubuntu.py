
import requests
import os
from urllib.parse import urlparse

def main():
    print("=== Ubuntu Image Fetcher ===")
    print("Download and organize images mindfully\n")

    # Prompt user for image URL
    url = input("Enter the image URL: ").strip()

    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        # Build full save path
        filepath = os.path.join("Fetched_Images", filename)

        # Save image in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"\n✓ Successfully downloaded: {filename}")
        print(f"✓ Image saved to: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"\n✗ Connection error: {e}")
    except Exception as e:
        print(f"\n✗ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

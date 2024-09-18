import argparse
import requests
import os

def download_file(url, save_path):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Write the content to a file
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded successfully to: {save_path}")
    else:
        print(f"Failed to download file from {url}. Status code: {response.status_code}")

def main():
    parser = argparse.ArgumentParser(description='Download a file from a URL.')
    parser.add_argument('url', type=str, help='URL of the file to download')
    parser.add_argument('save_path', type=str, help='Path where the file should be saved')

    args = parser.parse_args()

    download_file(args.url, args.save_path)

if __name__ == "__main__":
    main()

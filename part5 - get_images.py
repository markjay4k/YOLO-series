"""
Download 300 images or whatever limit you set staright from google
"""

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords": "fidget spinners", "limit": 300,
             "print_urls": True}
absolute_image_paths = response.download(arguments)

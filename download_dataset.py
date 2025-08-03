import gdown

file_id = "1nfUiaZ_e_HReJEdrD6Ivl5_80k2eLInH"

url = f"https://drive.google.com/uc?id={file_id}"
output = "data/dataset.zip"

gdown.download(url, output, quiet=False)

# Now Unzip the downloaded dataset and use it in your project

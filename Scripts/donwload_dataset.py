import kagglehub

def download_dataset():
    print("Downloading Garbage Classification V2...")

    path = kagglehub.dataset_download(
        "sumn2u/garbage-classification-v2"
    )

    print(f"Dataset downloaded successfully!")
    print(f"Path to dataset files: {path}")

    return path


if __name__ == "__main__":
    download_dataset()

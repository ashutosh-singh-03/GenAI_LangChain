import config  # Load HF_HOME from your .env file first

from huggingface_hub import scan_cache_dir


def list_downloaded_models():
    cache_info = scan_cache_dir()

    models = sorted(cache_info.repos, key=lambda model: model.repo_id.lower())

    output_file = "downloaded_models.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("MY DOWNLOADED HUGGING FACE MODELS\n")
        file.write("=" * 50 + "\n\n")

        if not models:
            file.write("No downloaded models found.\n")

        for index, model in enumerate(models, start=1):
            file.write(f"{index}. Model ID: {model.repo_id}\n")
            file.write(f"   Type: {model.repo_type}\n")
            file.write(f"   Size: {model.size_on_disk / (1024 ** 3):.2f} GB\n")
            file.write(f"   Location: {model.repo_path}\n\n")

    print(f"Found {len(models)} downloaded models.")
    print(f"Model list saved to: {output_file}")


if __name__ == "__main__":
    list_downloaded_models()

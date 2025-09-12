#import library operating system
import os

def download_kaggle_dataset(url, dest_folder):
    try:
        # check URL from user is valid or not
        if "datasets/" in url:
            dataset_slug = url.split("datasets/")[1]
        else:
            raise ValueError("❌ URL Kaggle tidak valid, pastikan formatnya benar.\n"
                             "Contoh: https://www.kaggle.com/datasets/<owner>/<dataset-name>")

        # make a new directory if the directory not created
        os.makedirs(dest_folder, exist_ok=True)

        # downloading dataset using format .zip
        print(f"⬇️  Downloading dataset: {dataset_slug}")
        exit_code = os.system(f'kaggle datasets download -d {dataset_slug} -p "{dest_folder}" --unzip')

        #checking if dataset successfully download or not
        if exit_code == 0:
            print(f"✅ Dataset berhasil didownload & diekstrak ke {dest_folder}")
        else:
            print("⚠️ Terjadi error saat mendownload dataset. Pastikan Kaggle API sudah terkonfigurasi.")

    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    # 🔗 URL dataset smartphone sales 
    url = "https://www.kaggle.com/datasets/vinothkannaece/mobiles-and-laptop-sales-data"

    # 📂 Path dest folder/ directory
    dest_folder = r"D:\Portofolio\Portofolio Mobile Phone Sales\data"

    #using download_kaggle_dataset function
    download_kaggle_dataset(url, dest_folder)

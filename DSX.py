import argparse
import logging
import requests
from io import BytesIO
from ds_store import DSStore
from urllib.parse import urlparse

def parse_dstore_data(file_obj):
    entries = {"Directories": set(), "Files": set()}
    with DSStore.open(file_obj, "r+") as d:
        for f in d:
            if f.code in [b"BKGD", b"ICVO", b"fwi0", b"fwsw", b"fwvh", b"icsp", b"icvo", b"icvt", 
                          b"logS", b"lg1S", b"lssp", b"lsvo", b"lsvt", b"modD", b"moDD", b"phyS", 
                          b"ph1S", b"pict", b"vstl", b"LSVO", b"ICVO", b"dscl", b"icgo", b"vSrn"]:
                entries["Directories"].add(f.filename)
            else:
                entries["Files"].add(f.filename)
    return entries

def is_url(path):
    result = urlparse(path)
    return all([result.scheme, result.netloc])

def download_file_to_memory(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception(f"Failed to download file from {url}")

def print_banner():
    print("""
   ___  _____  __
  / _ \/ __/ |/_/
 / // /\ \_>  <   v0.1.0
/____/___/_/|_|  
@h4x0rl33tx
    """)

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Parse .DS_Store file and extract directories and files.")
    parser.add_argument("input", help="Path to .DS_Store file or URL", nargs="?", default=None)
    args = parser.parse_args()

    if not args.input:
        parser.print_help()
        return

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    
    try:
        input_path = args.input
        
        if is_url(input_path):
            file_obj = download_file_to_memory(input_path)
        else:
            file_obj = open(input_path, "rb")
        
        entries = parse_dstore_data(file_obj)
        
        for type_ in entries:
            print(f"{type_}:")
            print("\n".join(entries[type_]))

    except Exception as e:
        logging.error(f"{e}")

    finally:
        if 'file_obj' in locals():
            if isinstance(file_obj, BytesIO):
                file_obj.close()
            else:
                file_obj.close()

if __name__ == "__main__":
    main()

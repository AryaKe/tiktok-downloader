import requests
import re
import os
from urllib.parse import urlparse
import time

def get_video_id(url):
    try:
        # Handle short URLs (vt.tiktok.com, vm.tiktok.com)
        if 'vt.tiktok.com' in url or 'vm.tiktok.com' in url:
            session = requests.Session()
            response = session.head(url, allow_redirects=True, timeout=10)
            final_url = response.url
            match = re.search(r'/video/(\d+)', final_url)
            if match:
                return match.group(1)
            raise Exception("Cannot extract video ID from short URL")
        
        # Standard URLs (www.tiktok.com/@user/video/12345)
        match = re.search(r'/video/(\d+)', url)
        if match:
            return match.group(1)
        
        raise Exception("Format URL tidak didukung")
    except Exception as e:
        raise Exception(f"Gagal mendapatkan Video ID: {str(e)}")

def get_hd_video_url(video_id):
    apis = [
        {
            "name": "TikTok Official API",
            "url": f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={video_id}",
            "path": ["aweme_list", 0, "video", "play_addr", "url_list"],
            "hd_param": "ratio=1080p"
        },
        {
            "name": "TikWM HD API",
            "url": "https://www.tikwm.com/api/",
            "params": {"url": f"https://www.tiktok.com/@tiktok/video/{video_id}", "hd": 1},
            "path": ["data", "play"]
        },
        {
            "name": "Tiklydown API",
            "url": f"https://api.tiklydown.eu.org/api/download?url=https://www.tiktok.com/@tiktok/video/{video_id}",
            "path": ["video", "url"]
        }
    ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "Accept": "application/json"
    }
    
    for api in apis:
        try:
            print(f"\nMencoba {api['name']}...")
            params = api.get("params", {})
            response = requests.get(api["url"], params=params, headers=headers, timeout=15)
            response.raise_for_status()
            data = response.json()
            
            # Navigasi ke URL video
            video_data = data
            for key in api["path"]:
                video_data = video_data[key]
            
            if isinstance(video_data, list):
                # Cari URL dengan kualitas HD
                hd_urls = [url for url in video_data if api.get("hd_param", "") in url] if api.get("hd_param") else video_data
                if not hd_urls:
                    hd_urls = video_data
                return hd_urls[0]  # Ambil URL pertama
            
            return video_data  # Jika langsung dapat URL
            
        except Exception as e:
            print(f"Gagal: {str(e)}")
            time.sleep(1)
    
    raise Exception("Semua API gagal. Coba lagi nanti atau gunakan VPN.")

def download_video(url, filename):
    try:
        # Download dengan chunk untuk file besar
        with requests.get(url, stream=True, timeout=30) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            
            with open(filename, 'wb') as f:
                downloaded = 0
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    downloaded += len(chunk)
                    # Tampilkan progress
                    print(f"Downloading... {downloaded/1024/1024:.2f}MB / {total_size/1024/1024:.2f}MB", end='\r')
        
        return True
    except Exception as e:
        print(f"\nError saat download: {str(e)}")
        if os.path.exists(filename):
            os.remove(filename)
        return False

def main():
    print("TikTok HD Video Downloader")
    print("-------------------------")
    print("Fitur:")
    print("- Resolusi HD (1080p)")
    print("- Support semua perangkat")
    print("- Multi-API backup")
    print("- Progress indicator\n")
    
    tiktok_url = input("Masukkan URL TikTok: ").strip()
    
    try:
        # Dapatkan Video ID
        video_id = get_video_id(tiktok_url)
        print(f"\nVideo ID: {video_id}")
        
        # Dapatkan URL video HD
        video_url = get_hd_video_url(video_id)
        print(f"\nURL Video HD: [tersedia]")
        
        # Download video
        filename = f"tiktok_hd_{video_id}.mp4"
        print(f"\nMemulai download: {filename}")
        
        if download_video(video_url, filename):
            print(f"\n\n✅ Berhasil didownload! File: {filename}")
            print(f"Ukuran: {os.path.getsize(filename)/1024/1024:.2f} MB")
        else:
            print("\nGagal mendownload video")
            
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nSolusi:")
        print("1. Coba lagi dalam beberapa menit")
        print("2. Gunakan VPN (jika di block)")
        print("3. Coba URL yang berbeda")
        print("4. Pastikan video tidak private")

if __name__ == "__main__":
    main()
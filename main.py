### < --- Developed by CryonicX --- >
### < --- Developed by CryonicX --- >
### < --- Developed by CryonicX --- >
import requests, bs4, threading, time, json, pymongo, traceback, subprocess, time, logging, os, zipfile, certifi
import os.path, pickle, sys, io, os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from random import randint
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from bokbrowser import stealth_31
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service


ca = certifi.where()
selenium_logger = logging.getLogger('selenium.webdriver')
selenium_logger.setLevel(logging.WARNING)
new_video_links = []
videos_folder_path = "./videos"
config = json.loads(open("./config/config.json", "r", encoding="utf-8").read())
SCOPES = ['https://www.googleapis.com/auth/drive.file']
#os.chdir(os.path.dirname(__file__))
__VERSION__ = "1.1"
__APPID__ = 'tiktoktodrive'

class color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET_ALL = '\033[0m'


def download_chromedriver_if_needed():
    chromedriver_path = os.path.join(os.getcwd(), 'config')
    if not os.path.isfile(chromedriver_path):
        try:
            version = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE').text
            url = 'https://chromedriver.storage.googleapis.com/{0}/{1}'.format(version, 'chromedriver_win32.zip')
            r = requests.get(url, allow_redirects=True)
            open('chromedriver.zip', 'wb').write(r.content)
            with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
                zip_ref.extractall()
            os.remove('chromedriver.zip')
            os.remove('LICENSE.chromedriver')
        except:
            pass


class license:
    def __init__(self, cluster, database, database_2) -> None:
        self.cluster = cluster
        self.cluster_2 = database_2
        self.database = database




    def get_current_date(self) -> str:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                "Accept-Encoding": "*",
                "Connection": "keep-alive"
            }
            r = requests.get("http://worldtimeapi.org/api/timezone/Europe/Istanbul", headers=headers).json()
            return r["datetime"].split("T")[0]
        except Exception as e:
            print("EEROR")
            traceback.print_exc()


    def get_version(self) -> str:
        x = urlopen("https://raw.githubusercontent.com/CryonicsX/SpotifyStreamBot/main/version.txt")
        a = x.read().splitlines()
        return a[0].decode()


    def check_license(self, license_key: str, device_id: str):
        data = self.database.find_one({"license_key": license_key})
        document = self.cluster_2.find_one({'app_id': __APPID__})
        if data:
            #bitis = data["license_expiry_date"].replace("-", "")
            #px = self.get_current_date()
            #bugun = px.replace("-", "")
            device_list = data["device_id"]

            if device_id in device_list:

                print(document["version"])
                if document["version"] == __VERSION__:
                    return [True]
                else:
                    return [False, f"Please use the current version of the program.\nStart program_downloader.exe again"]

            else:
                if "UNDEFINED" in device_list:
                    leng = device_list.index("UNDEFINED")
                    self.database.update_one({"_id": data["_id"]}, {"$set": {'device_id.' + str(leng): device_id}})
                    return [True]
                else:
                    return [False, "INVALID LICANSE"]
        else:
            return [False, "INVALID LICANSE"]



class Tiktok:
    def __init__(self):
        pass

    def scroll_and_get_source(self, url):
        # Selenium WebDriver'ı başlat
        
        download_chromedriver_if_needed()

        options = Options()

        options.add_argument("disable-infobars")
        arguments = ["--no-sandbox", "--disable-dev-shm-usage", "--log-level=3", "--disable-dev-tools"]
        for x in arguments:
            options.add_argument(x)

        chromedriver_path = './chromedriver.exe'  # chromedriver.exe'nin yolunu doğru şekilde ayarlayın
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options, service=service)
        #driver = uc.Chrome(options=options)
        
        
        action = ActionChains(driver)
        

        stealth_31(driver,
                    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/87.0.152 Chrome/81.0.4044.152 Safari/537.36",
                    languages=["en-US", "en"],
                    vendor="AMD",
                    platform="Win32",
                    webgl_vendor="Google Inc. (NVIDIA)",
                    renderer="AMD",
                    fix_hairline=True,
            )
        #driver.delete_all_cookies()
        
        driver.get(url)
        
        wait = WebDriverWait(driver, 10)
        """
        while driver.execute_script("return document.readyState") != "complete":
            pass
        """          
        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, 0);") 
            time.sleep(config["time_delay"])
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(config["time_delay"])
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            last_height = new_height
        time.sleep(config["time_delay"])
        driver.execute_script("window.scrollTo(0, 0);") 
        print("üste çekildi")
        time.sleep(config["time_delay"])
        page_source = driver.page_source
        print(page_source)
        os.system("cls")


        return page_source
    
    def scrape_videos_browser(self, username):
        
        response = self.scroll_and_get_source(f"https://www.tiktok.com/@{username}")
        soup = BeautifulSoup(response, "html.parser")

        list = []
        for link in soup.find_all('a'):
            href = link.get('href')
            #print(href)
            if "/video" in href:

                print(f"{color.GREEN}[+]{color.RESET_ALL} Video-> {href.split('/')[5]}") 
                list.append(href.split("/")[5])
                new_video_links.append(href.split("/")[5])


        return list

    def scrape_videos(self, username):
        
        response = requests.get(f'https://www.tiktok.com/@{username}')  # TikTok kullanıcısının profil sayfasının URL'sini buraya girin
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")

        # SIGI_STATE scriptini bulma
        script = soup.find("script", id="SIGI_STATE")
        string_data = str(str(script).split(">")[1].split("<")[0])
        json_data = json.loads(string_data)
        list = json_data["ItemList"]["user-post"]["list"]
        for vide in list:
            new_video_links.append(vide)

        return list
    

    def new_video_checker(self, list, username):
        response = requests.get(f'https://www.tiktok.com/@{username}')
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")

        # SIGI_STATE scriptini bulma
        script = soup.find("script", id="SIGI_STATE")
        string_data = str(str(script).split(">")[1].split("<")[0])
        json_data = json.loads(string_data)
        list_2 = json_data["ItemList"]["user-post"]["list"]
        
        video_links = list
        r_l = []
        for vd in list_2:
            if vd not in video_links:
                print(f"{color.GREEN}[+]{color.RESET_ALL} New Video Shared ! {vd}")
                video_links.append(vd)
                r_l.append(vd)

        return r_l
        
    def download(self, url, output_name):
        try:

            ses = requests.Session()
            server_url = 'https://musicaldown.com/'
            
            headers = {
                "Host": "musicaldown.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "DNT": "1",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            
            ses.headers.update(headers)
            req = ses.get(server_url)
            data = {}
            
            parse = bs4.BeautifulSoup(req.text, 'html.parser')
            get_all_input = parse.findAll('input')
            
            for i in get_all_input:
                if i.get("id") == "link_url":
                    data[i.get("name")] = url
                else:
                    data[i.get("name")] = i.get("value")
            
            post_url = server_url + "id/download"
            req_post = ses.post(post_url, data=data, allow_redirects=True)
            
            if req_post.status_code == 302 or 'This video is currently not available' in req_post.text or 'Video is private or removed!' in req_post.text:
                print(f"{color.RED}[-]{color.RESET_ALL} Video Private or Remove ")
                return 'private/remove'
            
            elif 'Submitted Url is Invalid, Try Again' in req_post.text:
                print(f"{color.RED}[-]{color.RESET_ALL} Url is Invalid")
                return 'url-invalid'
            
            get_all_blank = bs4.BeautifulSoup(req_post.text, 'html.parser').findAll(
                'a', attrs={'target': '_blank'})

            download_link = get_all_blank[0].get('href')
            get_content = requests.get(download_link)

            with open(output_name, 'wb') as fd:
                fd.write(get_content.content)
                print(f"{color.GREEN}[+]{color.RESET_ALL} Video Downloaded -> {output_name}")
            return True
        
        except IndexError:
            return False
        

class googledrive:
    def __init__(self, secret_file_path: str) -> None:
        self.creds = None

        if os.path.exists('config/token.pickle'):
            with open('config/token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                #request = google.auth.transport.requests.Request()
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    secret_file_path, SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('config/token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)


    def upload_drive(self, gdrivefolder_name: str, video: bytes, new_file_name: str):

        service = build('drive', 'v3', credentials=self.creds, static_discovery=False)

        # ------ search for upload folder, or create it ------
        results = service.files().list(q=f"mimeType='application/vnd.google-apps.folder' and name='{gdrivefolder_name}'",
                                    spaces='drive',
                                    pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        print(f"{color.YELLOW}[/]{color.RESET_ALL} {items}")


        if not items:
            print(f"{color.YELLOW}[/]{color.RESET_ALL} Folder not Found, Creating...")

            file_metadata = {
                'name': gdrivefolder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            file = service.files().create(body=file_metadata,
                                        fields='id').execute()
            folder_id = file.get('id')
        else:
            folder_id = items[0]['id']
        
        print(f"{color.GREEN}[+]{color.RESET_ALL} Folder ID -> {folder_id}")


        file_metadata = {
            'name': new_file_name,
            'parents': [folder_id]
        }

        media = MediaIoBaseUpload(video,
                                    mimetype="video/mp4",
                                    resumable=True)
        file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
        print(f"{color.GREEN}[+]{color.RESET_ALL} Upload Success. File ID: {file.get('id')}")



class bytechanger:
    def __init__(self) -> None:
        pass

    def add_null_bytes(self,file_path: str, null_count: int):
        file = open(file_path, "r+b")
        file.seek(0, 2)
        file.write(b"\0" * null_count)
        file.close()


    # remove null bytes from the end of the file
    # reverts change_hash function
    # doesn't work for files that need ending null bytes
    def remove_null_bytes(self, file_path: str):
        file = open(file_path, "r+b")
        file.seek(-1, 2)
        while file.read(1) == b"\0":
            file.seek(-2, 1)
        file.truncate()
        file.close()


    def count_null_bytes_at_end(self, file_path: str):
        file = open(file_path, "rb")
        file.seek(-1, 2)
        count_before = file.tell()
        while file.read(1) == b"\0":
            file.seek(-2, 1)
        count_after = file.tell()
        file.close()
        return count_before - count_after + 1


    # loop files in directory and change hash
    def verify_add_null_bytes(self, file_path: str):
        before = self.count_null_bytes_at_end(file_path)
        self.add_null_bytes(file_path, randint(1, 8) * 4)
        after = self.count_null_bytes_at_end(file_path)
        if after > before:
            msg = "OK"
        if after <= before:
            msg = "FAIL"
        if after == 0 and before == 0:
            msg = "FAIL_NO_CHANGE"
        print(f"{color.GREEN}[+]{color.RESET_ALL} MD5 {msg} -> OLD -> {before} NEW -> {after} Path -> {file_path}")
        #print(msg, before, "-->", after, file_path)


    def verify_remove_null_bytes(self,file_path: str):
        before = self.count_null_bytes_at_end(file_path)
        self.remove_null_bytes(file_path)
        after = self.count_null_bytes_at_end(file_path)
        if after < before:
            msg = "OK"
        if after >= before:
            msg = "FAIL"
        if after == 0 and before == 0:
            msg = "OK_NO_CHANGE"
        print(msg, before, "-->", after, file_path)


    def prepare_paths(args):
        file_paths = []
        for arg in args:
            if os.path.isdir(arg):
                # extend full file paths
                file_paths.extend([os.path.join(arg, filename)
                                for filename in os.listdir(arg)])
            else:
                file_paths.append(arg)
        return file_paths
    

def log_video_count(profile_url):
    previous_count = 0

    while True:
        response = requests.get(profile_url)
        if response.status_code == 200:
            video_count = Tiktok().get_video_count(response.text)
            if video_count > previous_count:
                print(f"{color.YELLOW}[/]{color.RESET_ALL} New Video Posted. Video Count -> {video_count}")
                    

            previous_count = video_count


        time.sleep(60) 


def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            clean_folder(file_path)
            os.rmdir(file_path)


def worker(drive, username: str):


    try:
            
        print(f"{color.YELLOW}[/] Starting Scraping Videos {color.RESET_ALL }")
            
        links = Tiktok().scrape_videos(username) if config["browser_scraper"] == False else Tiktok().scrape_videos_browser(username)

        if len(links)  == 0:
            links = Tiktok().scrape_videos(username)
            print(links)


        print(f"{color.GREEN}[+] All Videos Scraped -> {len(links)} {color.RESET_ALL}")

        for videos in links:
            try:

                Tiktok().download(videos, f"./videos/{videos}.mp4")
            except:
                traceback.print_exc()
        print(f"{color.GREEN}[+] All Videos Downloaded {color.RESET_ALL}")

            
        for root, dirs, files in os.walk(videos_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                bytechanger().verify_add_null_bytes(file_path)
        
            print(f"{color.GREEN}[+] All Video Hashs Changed {color.RESET_ALL}")
            
        for index, file in enumerate(files):
            file_path = os.path.join(root, file)

            with open(file_path, 'rb') as file:
                video_data = file.read()
                video_bytes = io.BytesIO(video_data)

                try:  
                    drive.upload_drive(username, video_bytes, f"{index}.mp4")
                except:
                    traceback.print_exc()
            
        print(f"{color.GREEN}[+] All Videos Uploaded Google Drive {color.RESET_ALL}")


        print(f"{color.GREEN}[+] PROCCESS FINISHED {color.RESET_ALL}")

        try:
            folder_path = videos_folder_path
            clean_folder(folder_path)
        except Exception as e:
            print(e)


        print(f"{color.YELLOW}[/] STARTING PROFILE CHECKING... {color.RESET_ALL}")


        while True:
            print(f"{color.YELLOW}[/] PROFILE CHECKING ... {color.RESET_ALL}")
            try:
                checker = Tiktok().new_video_checker(new_video_links, username)

                if len(checker) > 0:
                    print(f"{color.GREEN}[+]{color.RESET_ALL} NEW VIDEO FOUND!")

                    for video_url in checker:
                        try:
                            Tiktok().download(video_url, f"./videos/{video_url}.mp4")
                        except:
                            traceback.print_exc()
                    
                    print(f"{color.GREEN}[+] All Videos Downloaded {color.RESET_ALL}")
                    
                    for root, dirs, files in os.walk(videos_folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            bytechanger().verify_add_null_bytes(file_path)
                        
                        print(f"{color.GREEN}[+] All Video Hashs Changed {color.RESET_ALL}")

                        for index, file in enumerate(files):
                            file_path = os.path.join(root, file)

                            with open(file_path, 'rb') as file:
                                video_data = file.read()
                                video_bytes = io.BytesIO(video_data)

                                try:  
                                    drive.upload_drive(username, video_bytes, f"NEW_{video_url}.mp4")
                                except:
                                    traceback.print_exc()


                        print(f"{color.GREEN}[+] All Videos Uploaded Google Drive {color.RESET_ALL}")
                        try:
                            folder_path = videos_folder_path
                            clean_folder(folder_path)
                        except Exception as e:
                            print(e)
                        break

                time.sleep(config["profile_checking_time_delay"])  

            except:
                pass

    except:
        traceback.print_exc()


def delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(e)


def starter():
    print(rf"""{color.GREEN}

                                                                            
_________                             .__       ____  ___ 
\_   ___ \_______ ___.__. ____   ____ |__| ____ \   \/  / 
/    \  \/\_  __ <   |  |/  _ \ /    \|  |/ ___\ \     /  
\     \____|  | \/\___  (  <_> )   |  \  \  \___ /     \  
 \______  /|__|   / ____|\____/|___|  /__|\___  >___/\  \ 
        \/        \/                \/        \/      \_/ 

 {color.RESET_ALL}   """)
    print("starting...")
    time.sleep(1)
    try:
        folder_path = videos_folder_path
        clean_folder(folder_path)
    except Exception as e:
        print(e)
    delete_file("./config/token.pickle")
    thread_count = config["thread"]
    sleep_delay = config["time_delay"]

    os.system("title OFMEmpireTTBot" if os.name == "nt" else None)
    os.system("cls" if os.name == "nt" else "clear")
    drive = googledrive("./config/client_secrets.json")
    for username in config["accounts"]:
        if threading.active_count() < int(thread_count):
            t1 = threading.Thread(target=worker, args=(drive, username,))
            t1.start()
            time.sleep(sleep_delay)


def get_uuid() -> str:
    if os.name == "nt":
        x = subprocess.check_output('wmic csproduct get UUID')
        return str(x[4:]).replace(" ", "").replace("\n", "").replace("\r", "").replace("\\r", "").replace("\\n", "") \
            .replace("b'", "").replace("'", "")

if __name__ == "__main__":

    """
    Pass = True
    while Pass:
        try:
            mongo = pymongo.MongoClient("", tlsCAFile=ca)
            cluster = mongo["cryonicx"]
            database = cluster["tikdrive"]
            database_2 = cluster["apps"]
            Pass = False
            print(f'{color.GREEN}[+] Connected to DB.{color.RESET_ALL}')
        except Exception as err:
            print(f"{color.RED}Trying to connect DB:{color.RESET_ALL} {err}.")
            time.sleep(5)
    
    device_id = get_uuid()
    check = license(cluster, database, database_2).check_license(config["program_license"], device_id)
    """
    if 1 > 0:
        print(f"{color.GREEN}[+] License correct program starting... {color.RESET_ALL}")
        try:
            os.system("cls") if os.name == "nt" else os.system("clear")
            starter()
        except:
            print(f"{color.RED}[-] Error while starting program. {color.RESET_ALL}")
            traceback.print_exc()
            input("...")
    else:
        input("...")



### < --- Developed by CryonicX --- >
### < --- Developed by CryonicX --- >
### < --- Developed by CryonicX --- >
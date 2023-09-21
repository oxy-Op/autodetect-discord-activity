import time
import pygetwindow as gw
from pypresence import Presence
import win32con
import win32process
import win32ui
import win32gui
import win32api
import psutil
import requests
from json import load


try:
    config = load(open("config.json"))
except FileNotFoundError:
    print("config.json not found")
except Exception as e:
    print(f"An error occurred: {e}")
    exit()


RPC = Presence(client_id=config["client_id"])
RPC.connect()


def get_active_window_title():
    try:
        active_app = gw.getActiveWindow().title
        return active_app
    except ImportError:
        return None


def read_image_file(image_path):
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
        return image_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


try:
    print("Initiated.")
    while True:
        active_program = get_active_window_title()
        title = str(active_program).rfind("-")
        sliced_title = active_program[title + 1 :].strip()
        try:
            time.sleep(0.5)
            pid1 = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
            process1 = psutil.Process(pid1[-1]).exe()
            ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
            ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

            large, small = win32gui.ExtractIconEx(process1, 0)
            win32gui.DestroyIcon(large[0])
            hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
            hbmp = win32ui.CreateBitmap()
            hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_y)
            hdc = hdc.CreateCompatibleDC()

            hdc.SelectObject(hbmp)
            hdc.DrawIcon((0, 0), small[0])
            hbmp.SaveBitmapFile(hdc, "save.png")
        except ValueError or psutil.NoSuchProcess or ProcessLookupError as error:
            print(error)

        r = requests.post(
            f"https://api.imgbb.com/1/upload?expiration=600&key={config['imgbb_api_key']}",
            files={"image": open("save.png", "rb")},
        )
        url = r.json()["data"]["url"]
        time.sleep(2)

        if active_program:
            activity = {
                "state": f"Using {sliced_title}",
                "details": config["activity"]["details"],
                "large_image": url,
                "large_text": "Watching!",
                "small_image": config["activity"]["small_image_url"],
                "small_text": config["activity"]["small_image_text"],
            }
            RPC.update(
                **activity,
                buttons=config["activity"]["buttons"],
            )
        else:
            RPC.clear()

        time.sleep(15)  # Check every 15 seconds
except KeyboardInterrupt:
    pass
finally:
    RPC.clear()

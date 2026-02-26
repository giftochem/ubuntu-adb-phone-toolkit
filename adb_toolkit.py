
```python
import subprocess
import sys
from datetime import datetime

def run_adb(command):
    try:
        result = subprocess.check_output(['adb'] + command.split(), stderr=subprocess.STDOUT)
        return result.decode('utf-8').strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 adb_toolkit.py [command]")
        print("Commands: devices, screenshot, battery, logs")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "devices":
        print("📱 Connected devices:\n", run_adb("devices"))
    elif cmd == "screenshot":
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M')}.png"
        print(run_adb(f"shell screencap -p /sdcard/{filename}"))
        print(run_adb(f"pull /sdcard/{filename} ."))
        print(f"✅ Screenshot saved: {filename}")
    elif cmd == "battery":
        print("🔋 Battery info:\n", run_adb("shell dumpsys battery"))
    elif cmd == "logs":
        print("📜 Pulling logs (last 50 lines)...")
        print(run_adb("logcat -d | tail -50"))
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()

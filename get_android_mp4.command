echo "Finding largest recent .mp4 file..."

file=$(adb shell find /sdcard/DCIM/Camera/ -type f -size +6G -name "*.mp4" 
| xargs -0 ls -tl | tail -n1)

echo "Downloading selected file..."

adb pull "$file" /Users/matthewbeck/Downloads/

echo "File successfully downloaded to Downloads folder."

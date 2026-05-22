from pathlib import Path
import subprocess

video_exts = [".mp4", ".mov", ".mkv", ".avi", ".webm"]
play_icon = "play.png"

for video in Path(".").iterdir():
    if video.suffix.lower() in video_exts:
        output = video.with_suffix(".jpg")

        cmd = [
            "ffmpeg",
            "-i", str(video),
            "-i", play_icon,
            "-ss", "00:00:01",
            "-vframes", "1",
            "-filter_complex",
            "scale=640:-1[vid];[1:v]scale=100:-1[icon];[vid][icon]overlay=(W-w)/2:(H-h)/2",
            "-q:v",
            "2",
            str(output),
        ]

        subprocess.run(cmd, check=True)
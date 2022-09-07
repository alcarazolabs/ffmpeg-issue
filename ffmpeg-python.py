
import subprocess
import shlex

"""
cmd = 'ffmpeg -f concat -i videos.txt -c copy output.mp4' 
p = subprocess.Popen(shlex.split(cmd), stdin=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
"""

subprocess.run(shlex.split('ffmpeg -f concat -safe 0  -i videos.txt -c:v libx264 -c copy output.mp4'))
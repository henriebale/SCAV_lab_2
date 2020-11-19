import os
ex="1"
while ex != "0":
    print("Exercice Nº (insert 0 to end)")
    ex=input()
    print(f"Exercise {ex} selected")
    if ex=="1":
        os.system("ffmpeg -i BBB_video.mp4 -ss 00:00:00 -t 00:00:10 BBB_video_cut.mp4")
    elif ex=="2":
        os.system("ffmpeg -i BBB_video.mp4 -ss 00:00:00 -t 00:00:10 BBB_video_cut.mp4")
        os.system("ffplay BBB_video_cut.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p,scale=100:240[hh],[a][hh]overlay")
    elif ex=="3":
        os.system("ffmpeg -i BBB_video.mp4 -vf scale=1280:720 BBB_video_720.mp4")
        os.system("ffmpeg -i BBB_video.mp4 -vf scale=640:480 BBB_video_480.mp4")
        os.system("ffmpeg -i BBB_video.mp4 -vf scale=360:240 BBB_video_240.mp4")
        os.system("ffmpeg -i BBB_video.mp4 -vf scale=160:120 BBB_video_120.mp4")
    elif ex=="4":
        os.system("ffmpeg -i BBB_video.mp4 -ac 1 -acodec mp3 BBB_video_mono.mp4")
    else:
        print(f"Exercise {ex} doesn't exiat")


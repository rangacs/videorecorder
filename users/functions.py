from moviepy.editor import *
import os

cwd = "/home/rahul/Documents/web/authsysproject/users/static/upload/"
def handle_uploaded_file(f):  
    
    #save uploaded video to local system
    with open('users/static/upload/'+f.name+'-name.webm', 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

    #convert uploaded video to mp4 format
    conver_video(cwd+''+f.name+'-name.webm',cwd+''+f.name+'-name.mp4')

    #merge uploaded video with message video
    final_path = merge_videos(cwd+''+f.name+'-name.mp4')
    return final_path

def merge_videos(file_path):
    # loading user video
    uploaded_clip = VideoFileClip(file_path)

    # loading message video
    constant_msg = VideoFileClip(cwd+'constant_message.mp4')

    # concatenating both the clips
    final_clip = concatenate_videoclips([uploaded_clip, constant_msg])
    #writing the video into a file / saving the combined video
    final_clip.write_videofile(cwd+"final_msg.mp4")
    return True

def conver_video(ori_file,target_file):
    cmd = 'ffmpeg -i '+ori_file+' '+target_file
    os.system(cmd)
    return target_file

    

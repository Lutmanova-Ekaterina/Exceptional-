import time

def read_file_timed(file):
    start_time = time.time()
    try:
        file_opened = open(f'{file}', mode = 'rb')
        f = file_opened.read()
    except FileNotFoundError as k:
        print(k)
        print(f'Time required for {file} = 0.0')
    else:
        print(f' Time required for {file} = {time.time() - start_time}')
    finally:
        file_opened.close()

video_data = read_file_timed('video.mp4') 
video_data = read_file_timed('file_not_exist.mp4')

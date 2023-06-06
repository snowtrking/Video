import os
import random

width = 1920  # 视频宽度
height = 1080  # 视频高度
frame_rate = 30  # 视频帧率

input_file = 'raw.yuv'

for i in range(50):
    output_file = f'output_{i}.yuv'
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        frame_number = 0
        while True:
            frame_data = f_in.read(width * height * 3 // 2)  # 读取一帧数据
            if not frame_data:
                break
            if frame_number % frame_rate != 0:  # 判断是否为I帧，非I帧则写入输出文件
                f_out.write(frame_data)
            frame_number += 1

    # 将处理后的YUV文件重新编码为视频文件
    output_video = f'output_{i}.mp4'
    os.system(f'ffmpeg -f rawvideo -pix_fmt yuv420p -s {width}x{height} -r {frame_rate} -i {output_file} -c:v libx264 -crf 23 {output_video}')

    # 删除临时的YUV文件
    os.remove(output_file)

# 删除原始的YUV文件
os.remove(input_file)

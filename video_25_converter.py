import subprocess
import ffmpeg

parser = argparse.ArgumentParser(description='DeepSpeech argument parser')
parser.add_argument('--input_video_path', '-i', type=str, required=True, help='input_video_path')
parser.add_argument('--output_video_path', '-i', type=str, required=True, help='output_video_path')


opt = parser.parse_args()

input_file = opt.input_video_path
output_file = opt.output_video_path
target_fps = 25
#####Input########
input = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate', '-of', 'csv=p=0', input_file])
fps = eval(input.decode().strip())
print(f"Original FPS: {fps}")
#####Output#######
output = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate', '-of', 'csv=p=0', output_file])
fps = eval(output.decode().strip())
print(f"Converted FPS: {fps}")

import os
import subprocess
from tqdm import tqdm

def convert_mkv_to_mp4(moviesDir, mp4Dir):
    if not os.path.exists(mp4Dir):
        os.makedirs(mp4Dir)
    
    mkv_files = [f for f in os.listdir(moviesDir) if f.lower().endswith('.mkv')]
    
    if not mkv_files:
        print("No MKV files found in the specified directory.")
        return
    
    print(f"Found {len(mkv_files)} MKV files to convert")
    with tqdm(total=len(mkv_files), desc="Converting MKV to MP4", unit="file") as pbar:
        for mkv_file in mkv_files:
            input_path = os.path.join(moviesDir, mkv_file)
            output_file = os.path.splitext(mkv_file)[0] + '.mp4'
            output_path = os.path.join(mp4Dir, output_file)
            
            try:
                cmd = [
                    'ffmpeg',
                    '-i', input_path,
                    '-c:v', 'copy',
                    '-c:a', 'copy',
                    '-y',  # Overwrite output files without asking
                    output_path
                ]
                
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                pbar.update(1)
                
            except Exception as e:
                print(f"Error converting {mkv_file}: {str(e)}")
                pbar.update(1)
                continue
    
    print("Conversion complete!")

if __name__ == "__main__":
    moviesDir = "movies" 
    mp4Dir = "mp4"    
    convert_mkv_to_mp4(moviesDir, mp4Dir)
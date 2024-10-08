import librosa
import numpy as np
import json
import os
import base64
from io import BytesIO

def preprocess_audio(audio_data, file_name):
    # Load the audio file from the binary data
    audio_buffer = BytesIO(audio_data)
    y, sr = librosa.load(audio_buffer)
    
    # Get the file name without extension
    file_name = os.path.splitext(file_name)[0]
    
    # Detect beat frames
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    
    # Convert beat frames to time
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    
    # Detect onset frames
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
    
    # Convert onset frames to time
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    
    # Extract frequency information
    # We'll use the spectral centroid as a simple representation of frequency content
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    times = librosa.times_like(spec_cent)
    
    # Downsample frequency data to reduce file size
    downsampled_times = times[::10]
    downsampled_freq = spec_cent[0][::10]
    
    # Prepare the rhythm data
    rhythm_data = {
        'beats': beat_times.tolist(),
        'onsets': onset_times.tolist(),
        'frequencies': list(zip(downsampled_times.tolist(), downsampled_freq.tolist()))
    }
    
    # Convert rhythm data to JSON
    json_data = json.dumps(rhythm_data)
    
    print(f"Rhythm data processed for {file_name}")
    print(f"Beats: {len(rhythm_data['beats'])}")
    print(f"Onsets: {len(rhythm_data['onsets'])}")
    print(f"Frequency data points: {len(rhythm_data['frequencies'])}")
    
    return json_data

# This function will be called from the main script
def process_audio_file(file_content, file_name):
    try:
        # Decode base64 content
        audio_data = base64.b64decode(file_content)
        
        # Process the audio data
        json_data = preprocess_audio(audio_data, file_name)
        
        return json_data
    except Exception as e:
        return str(e)

# Example usage (this part will be in a separate script)
if __name__ == "__main__":
    # This is just a placeholder. In the actual use, you'll call process_audio_file()
    # from another script that handles file uploads.
    print("This script is designed to be imported and used by another script.")
    print("Please run the main script that handles file uploads and processing.")

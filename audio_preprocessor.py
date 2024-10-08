import librosa
import numpy as np
import json
import os

def preprocess_audio(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)
    
    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(audio_file))[0]
    
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
    
    # Save the rhythm data to a JSON file
    output_file = f"{file_name}_rhythm_data.json"
    with open(output_file, 'w') as f:
        json.dump(rhythm_data, f)
    
    print(f"Rhythm data saved to {output_file}")
    print(f"Beats: {len(rhythm_data['beats'])}")
    print(f"Onsets: {len(rhythm_data['onsets'])}")
    print(f"Frequency data points: {len(rhythm_data['frequencies'])}")

# Example usage
if __name__ == "__main__":
    audio_file = "path_to_your_audio_file.mp3"
    preprocess_audio(audio_file)
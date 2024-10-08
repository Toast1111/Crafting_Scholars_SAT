import base64
import json
from audio_preprocessor import process_audio_file

def main():
    print("Audio File Preprocessor for Rhythm Game")
    print("=======================================")
    print("Please upload your audio file when prompted.")
    print("The file should be in MP3 format.")
    
    # In a real web-based environment, you'd have a file upload mechanism here.
    # For this example, we'll simulate it by asking the user to input a file path.
    file_path = input("Enter the path to your audio file: ")
    
    try:
        with open(file_path, "rb") as audio_file:
            file_content = base64.b64encode(audio_file.read()).decode('utf-8')
        
        file_name = file_path.split("/")[-1]
        
        print(f"Processing {file_name}...")
        json_data = process_audio_file(file_content, file_name)
        
        # Save the JSON data to a file
        output_file_name = f"{file_name.rsplit('.', 1)[0]}_rhythm_data.json"
        with open(output_file_name, "w") as output_file:
            output_file.write(json_data)
        
        print(f"Rhythm data saved to {output_file_name}")
        print("You can now download this file and use it in your Pythonista project.")
    
    except FileNotFoundError:
        print("Error: File not found. Please make sure you entered the correct file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

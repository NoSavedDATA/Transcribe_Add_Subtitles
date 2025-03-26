import whisper_timestamped as whisper


import ffmpeg
import numpy as np
import librosa
import argparse
import json



def json_to_srt(json_file, srt_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    segments = data.get("segments", [])

    def format_time(seconds):
        millisec = int((seconds % 1) * 1000)
        h, m, s = int(seconds // 3600), int((seconds % 3600) // 60), int(seconds % 60)
        return f"{h:02}:{m:02}:{s:02},{millisec:03}"

    with open(srt_file, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments, 1):
            start = format_time(segment["start"])
            end = format_time(segment["end"])
            text = segment["text"].strip()
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")



def main(args):

    audio = whisper.load_audio(args.input)

    model = whisper.load_model("turbo", device="cpu")

    result = whisper.transcribe(model, audio, language="pt")


    with open("transcription.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    json_to_srt("transcription.json", "subtitles.srt")    

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default='input.mp4')
    parser.add_argument("--out", type=str, default='transcription.json')
    args = parser.parse_args()

    main(args)

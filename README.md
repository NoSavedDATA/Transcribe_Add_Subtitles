<h2>Transcription script using Ubuntu terminal, Python and Whisper.</h2>

Clone repo:
```bash
git clone https://github.com/NoSavedDATA/Transcribe_Add_Subtitles.git
cd Transcribe_Add_Subtitles
```

Create a Docker container with PyTorch 2.6
```bash
sudo docker run --name whisper --net="host" --cpus=12 --shm-size=16g -e PYTHONIOENCODING=utf-8 -e LANG=C.UTF-8 -e LC_ALL=C.UTF-8 --gpus all -v /home/nosaveddata/:/root -w /root -it 79226f81ed99 bash
```

Note: 79226f81ed99 image is an official PyTorch 2.6 docker image and you will need to find a way to install it yourself.


Attach to Docker container if necessary:
```bash
sudo docker start whisper
sudo docker attach whisper
```

Install dependencies:
```bash
git clone https://github.com/linto-ai/whisper-timestamped.git
cd whisper-timestamped
pip install .
cd ..
pip install ffmpeg-python
```

Run:
```bash
python transcribe.py
ffmpeg -i input.mp4 -vf "subtitles=subtitles.srt" -c:a copy output.mp4
```

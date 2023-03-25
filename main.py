import glob
import os
import json
import re
import datetime
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

previous_base_name = None
previous_segment = None

for mp3_file in glob.glob(os.path.join(INPUT_DIR, '*.mp3')):
    audio_file_name = os.path.splitext(os.path.basename(mp3_file))[0]

    print(f'Processing {audio_file_name}...')
    
    audio_file = open(mp3_file, "rb")
    base_name = re.sub(r'_\d+$', '', os.path.splitext(mp3_file)[0])

    if base_name != previous_base_name:
        previous_segment = None

    prompt = ''
    txt_file = base_name + '.txt'

    if not os.path.exists(txt_file):
        print(f'No txt file for {base_name}')
        continue

    with open(txt_file, 'r') as f:
        prompt = f.read()

    if previous_segment != None:
        prompt += f'\n\nPrevious segment:\n\n{previous_segment}'

    response = openai.Audio.transcribe("whisper-1", audio_file, prompt=prompt)

    previous_segment = response["text"][-300:]

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    with open(os.path.join(OUTPUT_DIR, f'{timestamp}_{audio_file_name}_response.json'), "w") as file:
        file.write(json.dumps({"prompt": prompt, "response": response}))

    with open(os.path.join(OUTPUT_DIR, f'{timestamp}_{audio_file_name}.txt'), "w") as file:
        file.write(response["text"])

    previous_base_name = base_name

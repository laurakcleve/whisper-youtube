import os
import json
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

# prompt = "This is part three of a coding video for web developers.\n\nVideo description:\n\nIf you've ever been stuck on what tests to write for your code, Jest's coverage reports can be a great tool for showing what sections of your codebase are not tested yet. It becomes even more powerful when used in combination with Continuous Integration (CI), as it can be automated and even block pull requests from merging, which we'll show in this video.\n\nPrevious segment:\n\nThen down here, you know, that was that one conditional that we couldn't cover. And now it's so much lower, because this file overall has dropped it. I really like this because it's a good way to kind of it's like a measure of confidence of, you know, of all my files, how well tested are they? Well, if some things are like completely not tested, they're really going to bring down your overall confidence rating in the code base."

# prompt = "If you've ever been stuck on what tests to write for your code, Jest's coverage reports can be a great tool for showing what sections of your codebase are not tested yet. It becomes even more powerful when used in combination with Continuous Integration (CI), as it can be automated and even block pull requests from merging, which we'll show in this video. 00:00 - What we'll cover 01:09 - Project overview 03:10 - When is coverage useful?  08:04 - Exploring the report in the browser 15:25 - Increasing coverage with a test 20:20 - Covering conditionals (branches) 24:49 - Gotchas with random outcomes in tests 28:32 - Adding a config for coverage customization 33:58 - Expanding coverage on a previously untested file 36:44 - Failing a test run on poor coverage 43:05 - Pull request workflow example (CI) 52:50 - Wrap-up"

prompt = "This is some example text that demonstrates what kind of output we want. This one is somewhat formal and stiff and does not include any filler words. But we'll make sure to add a little extra, some commas at least, because a couple sentences isn't enough to keep punctuation the whole way through."

audio_file = open("jest-coverage-part1.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file, prompt=prompt)

with open(f"./response.json", "w") as file:
    json_string = json.dumps(transcript)
    file.write(json_string)

with open(f"./text.txt", "w") as file:
    file.write(transcript["text"])
title: How to Transcribe Speech Recordings into Text with Python
slug: transcribe-recordings-speech-text-assemblyai
meta: Learn to transcribe speech in recordings like MP3s into text with Python and AssemblyAI's API.
category: post
date: 2020-08-09
modified: 2020-08-30
newsletter: False
headerimage: /img/headers/python-assemblyai.jpg
headeralt: Logos for the implementations used in this blog post. Copyright their respective owners.


When you have a recording where one or more people are talking, it's useful
to have a highly accurate and automated way to extract the spoken words into
text. Once you have the text, you can use it for further analysis or
as an accessibility feature.

In this tutorial, we'll use a high accuracy speech-to-text web application
programming interface called [AssemblyAI](https://www.assemblyai.com/) to
extract text from an MP3 recording (many other formats are supported as well).

With the code from this tutorial, you will be able to take an audio file
that contains speech
[such as this example one I recorded](https://www.fullstackpython.com/audio/fsp-object-relational-mappers.mp3)
and output a highly accurate text transcription like this:

```
An object relational mapper is a code library that automates the transfer of 
data stored in relational, databases into objects that are more commonly used
in application code or EMS are useful because they provide a high level 
abstraction upon a relational database that allows developers to write Python 
code instead of sequel to create read update and delete, data and schemas in 
their database. Developers can use the programming language. They are 
comfortable with to work with a database instead of writing SQL...

(the text goes on from here but I abbreviated it at this point)
```

## Tutorial requirements
Throughout this tutorial we are going to use the following dependencies,
which we will install in just a moment. Make sure you also have Python 3,
[preferably 3.6 or newer installed](https://www.python.org/downloads/),
in your environment:

We will use the following dependencies to complete this
tutorial:

* [requests](https://requests.readthedocs.io/)
  [version 2.24.0](https://pypi.org/project/requests/) to make HTTP requests to
  the [AssemblyAI](https://www.assemblyai.com/) speech-to-text
  [API](/application-programming-interfaces.html)
* An [AssemblyAI](https://www.assemblyai.com/) account, 
  which you can sign up for a 
  [free API access key here](https://app.assemblyai.com/login/)

All code in this blog post is available open source under the MIT license
on GitHub under the
[transcribe-speech-text-script directory of the blog-code-examples repository](https://github.com/fullstackpython/blog-code-examples).
Use the source code as you desire for your own projects.


## Setting up the development environment
Change into the directory where you keep your Python
[virtual environments](/virtual-environments-virtualenvs-venvs.html).
I keep mine in a subdirectory named `venvs` within my user's home 
directory. Create a new virtualenv for this project using the following
command.

```bash
python3 -m venv ~/venvs/pytranscribe
```

Activate the virtualenv with the `activate` shell script:

```bash
source ~/venvs/pytranscribe/bin/activate
```

After the above command is executed, the command prompt will
change so that the name of the virtualenv is prepended to the
original command prompt format, so if your prompt is simply
`$`, it will now look like the following:

```bash
(pytranscribe) $
```

Remember, you have to activate your virtualenv in every new terminal
window where you want to use dependencies in the virtualenv.

We can now install the `requests` package into the activated 
but otherwise empty virtualenv.

```
pip install requests==2.24.0
```

Look for output similar to the following to confirm the appropriate
packages were installed correctly from PyPI.

```
(pytranscribe) $ pip install requests==2.24.0
Collecting requests==2.24.0
  Using cached https://files.pythonhosted.org/packages/45/1e/0c169c6a5381e241ba7404532c16a21d86ab872c9bed8bdcd4c423954103/requests-2.24.0-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests==2.24.0)
  Using cached https://files.pythonhosted.org/packages/5e/c4/6c4fe722df5343c33226f0b4e0bb042e4dc13483228b4718baf286f86d87/certifi-2020.6.20-py2.py3-none-any.whl
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests==2.24.0)
  Using cached https://files.pythonhosted.org/packages/9f/f0/a391d1463ebb1b233795cabfc0ef38d3db4442339de68f847026199e69d7/urllib3-1.25.10-py2.py3-none-any.whl
Collecting chardet<4,>=3.0.2 (from requests==2.24.0)
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting idna<3,>=2.5 (from requests==2.24.0)
  Using cached https://files.pythonhosted.org/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl
Installing collected packages: certifi, urllib3, chardet, idna, requests
Successfully installed certifi-2020.6.20 chardet-3.0.4 idna-2.10 requests-2.24.0 urllib3-1.25.10
```

We have all of our required dependencies installed so we can get started 
coding the application.


## Uploading, initiating and transcribing audio
We have everything we need to start building our application that
will transcribe audio into text. We're going to build this
application in three files:

1. [upload_audio_file.py](https://github.com/fullstackpython/blog-code-examples/blob/master/transcribe-speech-text-script/upload_audio_file.py): 
  uploads your audio file to a secure place on AssemblyAI's service so
  it can be access for processing. If your audio file is already accessible
  with a public URL, you don't need to do this step, you can just follow 
  [this quickstart](https://docs.assemblyai.com/overview/getting-started)
1. [initiate_transcription.py](https://github.com/fullstackpython/blog-code-examples/blob/master/transcribe-speech-text-script/initiate_transcription.py):
  tells the API which file to transcribe and to start immediately
1. [get_transcription.py](https://github.com/fullstackpython/blog-code-examples/blob/master/transcribe-speech-text-script/get_transcription.py):
  prints the status of the transcription if it is still processing, or
  displays the results of the transcription when the process is complete

Create a new directory named `pytranscribe` to store these files as 
we write them. Then change into the new project directory.

```
mkdir pytranscibe
cd pytranscribe
```

We also need to export our AssemblyAI API key as an environment variable.
[Sign up for an AssemblyAI account](https://app.assemblyai.com/login/) 
and log in to the 
[AssemblyAI dashboard](https://app.assemblyai.com/dashboard/), then
copy "Your API token" as shown in this screenshot:

<img src="/img/200809-transcription-assemblyai/assemblyai-dashboard.png" width="100%" alt="AssemblyAI dashboard." class="shot rnd outl">


```bash
export ASSEMBLYAI_KEY=your-api-key-here
```

Note that you must use the `export` command in every command line window
that you want this key to be accessible. The scripts we are writing will
not be able to access the API if you do not have the token exported as
`ASSEMBLYAI_KEY` in the environment you are running the script.

Now that we have our project directory created and the API key set as an
environment variable, let's move on to writing the code for the first file 
that will upload audio files to the AssemblyAI service.


## Uploading the audio file for transcription
Create a new file named `upload_audio_file.py` and place the following
code in it:

```python
import argparse
import os
import requests


API_URL = "https://api.assemblyai.com/v2/"


def upload_file_to_api(filename):
    """Checks for a valid file and then uploads it to AssemblyAI
    so it can be saved to a secure URL that only that service can access.
    When the upload is complete we can then initiate the transcription
    API call.
    Returns the API JSON if successful, or None if file does not exist.
    """
    if not os.path.exists(filename):
        return None

    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {'authorization': os.getenv("ASSEMBLYAI_KEY")}
    response = requests.post("".join([API_URL, "upload"]), headers=headers,
                             data=read_file(filename))
    return response.json()

```

The above code imports the `argparse`, `os` and `requests` packages
so that we can use them in this script. The `API_URL` is a constant
that has the base URL of the AssemblyAI service. We define the
`upload_file_to_api` function with a single argument, `filename`
that should be a string with the absolute path to a file and its
filename.

Within the function, we check that the file exists, then use Request's 
[chunked transfer encoding](https://requests.readthedocs.io/en/master/user/advanced/#chunk-encoded-requests)
to stream large files to the AssemblyAI API.

The `os` module's `getenv` function reads the API that was set on the 
command line using the `export` command with the `getenv`. Make sure
that you use that `export` command in the terminal where you are
running this script otherwise that `ASSEMBLYAI_KEY` value will be
blank. When in doubt, use `echo $ASSEMBLY_AI` to see if the value
matches your API key.

To use the `upload_file_to_api` function, append the following lines of
code in the `upload_audio_file.py` file so that we can properly
execute this code as a script called with the `python` command:

```python

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    upload_filename = args.filename
    response_json = upload_file_to_api(upload_filename)
    if not response_json:
        print("file does not exist")
    else:
        print("File uploaded to URL: {}".format(response_json['upload_url']))
```

The code above creates an `ArgumentParser` object that allows the
application to obtain a single argument from the command line
to specify the file we want to access, read and upload to the
AssmeblyAI service. 

If the file does not exist, the script will print a message that 
the file couldn't be found. In the happy path where we do find the
correct file at that path, then the file is uploaded using
the code in `upload_file_to_api` function.

Execute the completed `upload_audio_file.py` script by running it on
the command line with the `python` command. Replace `FULL_PATH_TO_FILE`
with an absolute path to the file you want to upload, such as 
`/Users/matt/devel/audio.mp3`.

```bash
python upload_audio_file.py FULL_PATH_TO_FILE
```

Assuming the file is found at the location that you specified, when the 
script finishes uploading the file, it will print a message like this one
with a unique URL:

```
File uploaded to URL: https://cdn.assemblyai.com/upload/463ce27f-0922-4ea9-9ce4-3353d84b5638
```

This URL is not public, it can only be used by the AssemblyAI service, so no
one else will be able to access your file and its contents except for you
and their transcription API.

The part that is important is the last section of the URL, in this example
it is `463ce27f-0922-4ea9-9ce4-3353d84b5638`. Save that unique identifier 
because we need to pass it into the next script that initiates the 
transcription service.


## Initiate transcription
Next, we'll write some code to kick off the transcription. Create a
new file named `initiate_transcription.py`. Add the following
code to the new file.

```python
import argparse
import os
import requests


API_URL = "https://api.assemblyai.com/v2/"
CDN_URL = "https://cdn.assemblyai.com/"


def initiate_transcription(file_id):
    """Sends a request to the API to transcribe a specific
    file that was previously uploaded to the API. This will
    not immediately return the transcription because it takes
    a moment for the service to analyze and perform the
    transcription, so there is a different function to retrieve
    the results.
    """
    endpoint = "".join([API_URL, "transcript"])
    json = {"audio_url": "".join([CDN_URL, "upload/{}".format(file_id)])}
    headers = {
        "authorization": os.getenv("ASSEMBLYAI_KEY"),
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    return response.json()
```

We have the same imports as the previous script and we've added a 
new constant, `CDN_URL` that matches the separate URL where AssemblyAI
stores the uploaded audio files.

The `initiate_transcription` function essentially just sets up
a single HTTP request to the AssemblyAI API to start the transcription
process on the audio file at the specific URL passed in. This is why
passing in the `file_id` is important: that completes the URL of the
audio file that we are telling AssemblyAI to retrieve.

Finish the file by appending this code so that it can be easily
invoked from the command line with arguments.

```python

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_id")
    args = parser.parse_args()
    file_id = args.file_id
    response_json = initiate_transcription(file_id)
    print(response_json)
```

Start the script by running the `python` command on the 
`initiate_transcription` file and pass in the unique file identifier
you saved from the previous step.

```bash
# the FILE_IDENTIFIER is returned in the previous step and will
# look something like this: 463ce27f-0922-4ea9-9ce4-3353d84b5638
python initiate_transcription.py FILE_IDENTIFIER
```

The API will send back a JSON response that this script prints to
the command line.

```bash
{'audio_end_at': None, 'acoustic_model': 'assemblyai_default', 'text': None, 
 'audio_url': 'https://cdn.assemblyai.com/upload/463ce27f-0922-4ea9-9ce4-3353d84b5638', 
 'speed_boost': False, 'language_model': 'assemblyai_default', 'redact_pii': False, 
 'confidence': None, 'webhook_status_code': None, 
 'id': 'gkuu2krb1-8c7f-4fe3-bb69-6b14a2cac067', 'status': 'queued', 'boost_param': None, 
 'words': None, 'format_text': True, 'webhook_url': None, 'punctuate': True, 
 'utterances': None, 'audio_duration': None, 'auto_highlights': False, 
 'word_boost': [], 'dual_channel': None, 'audio_start_from': None}
```

Take note of the value of the `id` key in the JSON response. This is the
transcription identifier we need to use to retrieve the transcription result.
In this example, it is `gkuu2krb1-8c7f-4fe3-bb69-6b14a2cac067`. Copy the 
transcription identifier in your own response because we will need it to 
check when the transcription process has completed in the next step.


## Retrieving the transcription result
We have uploaded and begun the transcription process, so let's get the
result as soon as it is ready. 

How long it takes to get the results back can depend on the size of the file,
so this next script will send an HTTP request to the API and report back 
the status of the transcription, or print the output if it's complete.

Create a third Python file named `get_transcription.py` and put the following
code into it.

```python
import argparse
import os
import requests


API_URL = "https://api.assemblyai.com/v2/"


def get_transcription(transcription_id):
    """Requests the transcription from the API and returns the JSON
    response."""
    endpoint = "".join([API_URL, "transcript/{}".format(transcription_id)])
    headers = {"authorization": os.getenv('ASSEMBLYAI_KEY')}
    response = requests.get(endpoint, headers=headers)
    return response.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("transcription_id")
    args = parser.parse_args()
    transcription_id = args.transcription_id
    response_json = get_transcription(transcription_id)
    if response_json['status'] == "completed":
        for word in response_json['words']:
            print(word['text'], end=" ")
    else:
        print("current status of transcription request: {}".format(
              response_json['status']))
```

The code above has the same imports as the other scripts. In this
new `get_transcription` function, we simply call the AssemblyAI API
with our API key and the *transcription identifier* from the previous
step (not the file identifier). We retrieve the JSON response and
return it.

In the main function we handle the transcription identifier that
is passed in as a command line argument and pass it into the
`get_transcription` function. If the response JSON from the
`get_transcription` function contains a `completed` status then we
print the results of the transcription. Otherwise, print the
current status which is either `queued` or `processing` before
it is `completed`.

Call the script using the command line and the transcription identifier
from the previous section:

```bash
python get_transcription.py TRANSCRIPTION_ID
```

If the service has not yet started working on the transcript then it
will return `queued` like this:

```bash
current status of transcription request: queued
```

When the service is currently working on the audio file it will
return `processing`:

```bash
current status of transcription request: processing
```

When the process is completed, our script will return the text of
the transcription, like you see here:

```bash
An object relational mapper is a code library that automates the transfer of 
data stored in relational, databases into objects that are more commonly used
in application code or EMS are useful because they provide a high level 

...(output abbreviated)
```

That's it, we've got our transcription! 

You may be wondering what to do if the accuracy isn't where you need 
it to be for your situation. That is where
[boosting accuracy for keywords or phrases](https://docs.assemblyai.com/guides/boosting-accuracy-for-keywords-or-phrases)
and
[selecting a model that better matches your data](https://docs.assemblyai.com/guides/transcribing-with-a-different-acoustic-or-custom-language-model)
come in. You can use either of those two methods to boost the accuracy
of your recordings to an acceptable level for your situation.


## What's next?
We just finished writing some scripts that call the AssemblyAI API to
transcribe recordings with speech into text output.

Next, take a look at some of their more advanced documentation that goes
beyond the basics in this tutorial:

* [Supported file formats](https://docs.assemblyai.com/overview/supported-file-formats)
* [Transcribing dual channel/stereo recordings](https://docs.assemblyai.com/guides/transcribing-dual-channel-stereo-recordings)
* [Getting speaker labels (speaker diarization)](https://docs.assemblyai.com/guides/getting-speaker-labels-speaker-diarization)

Questions? Let me know via an issue ticket on
[the Full Stack Python repository](https://github.com/mattmakai/fullstackpython.com/issues),
on Twitter
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai).
See something wrong with this post? Fork
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/200809-transcribe-recordings-speech-text-assemblyai.markdown)
and submit a pull request.


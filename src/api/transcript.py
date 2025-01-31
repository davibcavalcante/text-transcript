from dotenv import load_dotenv
import os
import assemblyai as aai

load_dotenv()

def start_transcript(config, file_path):
  transcriber = aai.Transcriber(config=config)
  transcript = transcriber.transcribe(file_path)
  return transcript


def get_config():
  config = aai.TranscriptionConfig(language_code="pt")
  aai.settings.api_key = os.getenv('API_KEY')
  return config

def get_transcription(file_path):
  config = get_config()
  transcript = start_transcript(config, file_path)
  return transcript
import assemblyai as aai
from .config import get_api_key

def start_transcript(config, file_path):
  transcriber = aai.Transcriber(config=config)
  transcript = transcriber.transcribe(file_path)
  return transcript

def get_config():
  config = aai.TranscriptionConfig(language_code="pt")
  aai.settings.api_key = get_api_key()
  return config

def get_transcription(file_path):
  config = get_config()
  transcript = start_transcript(config, file_path)
  return transcript
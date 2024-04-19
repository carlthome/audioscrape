"""Machine listening help functionality to easily categorize downloaded audio."""

import logging
from mediapipe.tasks.python import BaseOptions, audio
from mediapipe.tasks.python.components.containers import AudioData
import importlib.resources
import soundfile as sf

MODULE_PATH = importlib.resources.files(__package__)
OPTIONS = audio.AudioClassifierOptions(base_options=BaseOptions(model_asset_path=MODULE_PATH / "yamnet.tflite"))
logger = logging.getLogger(__name__)


def classify(audio_path) -> audio.AudioClassifierResult:
    with audio.AudioClassifier.create_from_options(OPTIONS) as f:
        logger.info(f"Classifying {audio_path}")
        audio_data = AudioData.create_from_array(*sf.read(audio_path))
        predictions = f.classify(audio_data)
        logger.debug(predictions)
        # TODO Average predictions over time.
        # TODO Use more tags than just music.
        is_music = predictions[0].classifications[0].categories[0].category_name == "Music"
        logger.info(f"Classified {audio_path} as music: {is_music}")
    return predictions

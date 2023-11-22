# Dealing with puntuations
#
from dbpunctuator.inference import Inference, InferenceArguments
from dbpunctuator.utils import DEFAULT_ENGLISH_TAG_PUNCTUATOR_MAP

args = InferenceArguments(
        model_name_or_path="Qishuai/distilbert_punctuator_en",
        tokenizer_name="Qishuai/distilbert_punctuator_en",
        tag2punctuator=DEFAULT_ENGLISH_TAG_PUNCTUATOR_MAP
    )

punctuator_model = Inference(inference_args=args, 
                             verbose=False)
    
    
text = [
    """
however when I am elected I vow to protect our American workforce
unlike my opponent I have faith in our perseverance our sense of trust and our democratic principles will you support me
    """
]

print(punctuator_model.punctuation(text)[0])

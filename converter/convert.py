from transformers import pipeline

# Use a stable paraphrasing model
rephraser = pipeline(
    "text2text-generation",
    model="ramsrigouthamg/t5_paraphraser",
    tokenizer="ramsrigouthamg/t5_paraphraser"
)


def convert_to_human(text):
    output = rephraser(text, max_length=256, num_return_sequences=1, do_sample=True)
    return output[0]['generated_text']
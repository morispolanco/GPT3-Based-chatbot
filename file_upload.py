import openai
import os

#minhaz- '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'
openai.api_key = "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"

response = openai.File.create(
 file=open("domain.jsonl"),
 purpose='answers'
)
print(response)

import os
import openai

openai.api_key = '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'

response = openai.Completion.create(
  model="code-davinci-002",
  prompt="\"\"\"\nfetch csv file at url 'https://github.com/fivethirtyeight/data/blob/master/polls/pres_pollaverages_1968-2016.csv' and read into DataFrame\n\"\"\"",
  temperature=0,
  max_tokens=300,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)
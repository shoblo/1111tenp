import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="davinci",
  prompt="Back to Future: π¨π΄ππ\nBatman: π€΅π¦\nTransformers: ππ€\nWonder Woman: πΈπ»πΈπΌπΈπ½πΈπΎπΈπΏ\nWinnie the Pooh: π»πΌπ»\nThe Godfather: π¨π©π§π΅π»ββοΈπ²π₯\nGame of Thrones: πΉπ‘π‘πΉ\nSpider-Man:",
  temperature=0.8,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)
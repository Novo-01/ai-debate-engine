import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_debate(topic, history):
    messages = []

    # システムメッセージ：中立な要約AIの立場
    messages.append({
        "role": "system",
        "content": "あなたは優秀なディベート分析官です。以下の議論を中立的に要約し、最も合理的と思われる結論を1〜2文で提示してください。"
    })

    # ユーザーに渡す形で、議論のログとトピックを含める
    debate_text = f"議題: {topic}\n議論の流れ:\n"
    for h in history:
        debate_text += f"{h['speaker']}（{h['role']}）: {h['text']}\n"

    messages.append({
        "role": "user",
        "content": debate_text
    })

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5
    )

    return response.choices[0].message.content.strip()

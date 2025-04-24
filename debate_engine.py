import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.apikey = os.getenv("OPEN_API/KEY")

def call_openai_api(topic, role, history):
    prompt = f"あなたは「{role}」の立場で、次の課題について意見を述べてください : 「{topic}」\n"
    for h in history:
        prompt += f"{h['speaker']} ({h['role']}) : {h['text']}\n"
    prompt += f"{role}としてのあなたの発言 : "

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

def run_debate(topic, max_turns=6):
    history = []
    roles = {"AI_A": "賛成", "AI_B": "反対"}

    for turn in range(max_turns):
        speaker = "AI_A" if turn % 2 == 0 else "AI_B"
        role = roles[speaker]
        print(f"\n--- {speaker}（{role}）の発言 ---")

        response = call_openai_api(topic, role, history)
        print(response)

        history.append({
            "speaker": speaker,
            "role": role,
            "text": response
        })

    return history
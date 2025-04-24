from debate_engine import run_debate
from summarizer import summarize_debate

if __name__ == "__main__":
    topic = input("課題を入力してください：")
    
    # AI_AとAI_Bの議論
    history = run_debate(topic)

    # AI_Cが要約
    print("\n=== AI_C（中立な要約AI）による結論 ===\n")
    summary = summarize_debate(topic, history)
    print(summary)

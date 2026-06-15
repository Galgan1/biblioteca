import json

log_path = r"C:\Users\User\.gemini\antigravity\brain\4fe95e9d-2be3-4edd-9c23-7e8c24f39b06\.system_generated\logs\transcript.jsonl"
found_user_msgs = []

try:
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data.get("type") == "USER_INPUT":
                found_user_msgs.append(data.get("content", ""))
                
    with open("user_messages.json", "w", encoding="utf-8") as out:
        json.dump(found_user_msgs, out, indent=2, ensure_ascii=False)
except Exception as e:
    with open("user_messages.json", "w", encoding="utf-8") as out:
        out.write(str(e))

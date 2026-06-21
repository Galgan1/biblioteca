import json

log_path = r"C:\Users\User\.gemini\antigravity\brain\4fe95e9d-2be3-4edd-9c23-7e8c24f39b06\.system_generated\logs\transcript_full.jsonl"
found_user_msgs = []

try:
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data.get("type") == "USER_INPUT":
                found_user_msgs.append(data.get("content", ""))
                
    # only save the last message which has the bibliography
    if found_user_msgs:
        with open("full_bibliography_message.txt", "w", encoding="utf-8") as out:
            out.write(found_user_msgs[-1])
except Exception as e:
    with open("full_bibliography_message.txt", "w", encoding="utf-8") as out:
        out.write(str(e))

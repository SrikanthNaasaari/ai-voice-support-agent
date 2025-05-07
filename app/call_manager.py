transcript = []

def start_call():
    global transcript
    transcript = []

def update_transcript(user, agent):
    global transcript
    transcript.append(f"Customer: {user}\nAgent: {agent}\n")

def get_transcript():
    return "\n".join(transcript)
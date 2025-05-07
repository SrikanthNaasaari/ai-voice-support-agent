# AI Voice Support Agent

This project is an AI-powered customer support agent that handles voice-based interactions. It uses speech-to-text (STT), text-to-speech (TTS), and FAQ-based retrieval to assist users in real-time.

---

## Features

- Voice call interface using Streamlit
- Live Speech-to-Text transcription (OpenAI Whisper / other STT)
- AI agent replies using Text-to-Speech (OpenAI TTS or pyttsx3, etc.)
- FAQ document-based response system
- Graceful fallback for out-of-scope queries
- Full transcription shown after the call ends

---

## Setup Instructions

1.Clone the Repository

git clone https://github.com/SrikanthNaasaari/ai-voice-support-agent.git
cd ai-voice-support-agent

## 2. Create and Activate a Virtual Environment

    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate

## 3. Install Dependencies

   pip install -r requirements.txt

## 4. How to Run the Application
   
   streamlit run voice_agent.py


## STT & TTS Configuration

    Speech-to-Text (STT)

    Library Used: OpenAI Whisper via openai-whisper or whisperx (based on config).

    Alternative: Use speech_recognition with Google Web Speech API for live STT.

    Text-to-Speech (TTS)

    Library Used: pyttsx3 for offline TTS.

    Alternative Option: Use gTTS for higher-quality cloud-based audio.

## FAQ-Based Retrieval

    The FAQ document (faq.pdf) is parsed using PyMuPDF.

    Text is indexed using sentence embeddings via sentence-transformers.

    Retrieval uses cosine similarity to fetch the closest answer to the query.

## Out-of-Scope Handling

    If no answer is found within a similarity threshold, the agent replies:

    “I do not have an answer to that question, let me transfer your call to the live agent.”

    This simulates a handoff to a human support agent.

## Transcription

    A full call transcription buffer is maintained during the session.

    The transcript is displayed on the Streamlit interface once the call ends.


## Notes
    Ensure your faq.pdf file is placed in the data/ directory.

    Temporary audio files are generated in the audio/ directory.

    Full conversation transcription appears in the Streamlit UI after the simulated call ends.

## Design Decisions & Trade-offs

    Voice Simulation: Since real telephony integration (like Twilio) is complex and requires billing, we simulate calls in the UI using typed input and generated audio.

    STT/TTS Libraries: Chosen for balance between latency and ease of integration; Whisper is accurate but not real-time, so gTTS and pyttsx3 are used for faster feedback in mock flow.

    Document Search: We use a simple semantic search method for fast retrieval; this avoids the complexity of full-blown vector DBs like FAISS or Pinecone.

    UI Framework: Streamlit provides a fast prototyping interface but is limited in real telephony support — suitable for this simulation.
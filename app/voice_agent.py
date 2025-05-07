import streamlit as st
import os
# from app import stt_tts, qa_engine, call_manager

import stt_tts
import qa_engine
import call_manager

st.set_page_config(page_title="AI Voice Support Agent", layout="centered")

st.title("AI Voice Support Agent")

if "call_active" not in st.session_state:
    st.session_state.call_active = False

if st.button("Start Call"):
    st.session_state.call_active = True
    call_manager.start_call()

if st.button("End Call"):
    st.session_state.call_active = False
    st.audio("audio/temp_response.wav", format="audio/wav")
    st.write("###Conversation Transcript:")
    st.text(call_manager.get_transcript())

if st.session_state.call_active:
    st.write("Speak now...")
    input_audio_path = stt_tts.record_audio()
    user_text = stt_tts.speech_to_text(input_audio_path)
    st.write(f"You said: {user_text}")

    answer, out_of_scope = qa_engine.get_faq_answer(user_text)

    if out_of_scope:
        response = "I do not have an answer to that question, let me transfer your call to the live agent."
    else:
        response = answer

    st.write(f"Agent: {response}")
    call_manager.update_transcript(user_text, response)
    response_audio = stt_tts.text_to_speech(response)
    st.audio(response_audio, format="audio/wav")

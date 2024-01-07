import streamlit as st
import speech_recognition as sr
from LLM_model_run import get_gemini_response
from output_speech import text_to_speech

def convert_voice_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Recording... Speak now!")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds

        try:
            st.success("Recognizing... Please wait.")
            text = recognizer.recognize_google(audio)  # Use Google Speech Recognition
            st.subheader("You said:")
            st.write(text)

            # Pass the recognized text to the get_gemini_response function
            gemini_response = get_gemini_response(text)
            st.subheader("Here is the Response:")
            st.markdown(gemini_response)

            # Convert Gemini response to speech
            text_to_speech(gemini_response)

        except sr.UnknownValueError:
            st.error("Could not understand audio")
        except sr.RequestError as e:
            st.error(f"Error with the speech recognition service; {e}")

def main():
    st.title("Voice Interaction with Gemini")
    st.markdown(
        """
        ## Welcome to the Voice Interaction App

        Press provide the prompt using Record button and see the Gemini response!

        _Note: Make sure your microphone is connected and working._
        """
    )

    # Button to start recording
    if st.button("Record", key="record_button"):
        convert_voice_to_text()

if __name__ == "__main__":
    main()

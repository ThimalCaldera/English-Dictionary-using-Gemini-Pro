import streamlit as st 
import google.generativeai as genai
import google.ai.generativelanguage as glm
from gtts import gTTS
import tempfile
from dotenv import load_dotenv

from PIL import Image
import os
import io

load_dotenv()

API_KEY = os.environ.get("GOOGLE_API_KEY")
model = genai.GenerativeModel("gemini-pro")

class State:
    """ This is app state. """
    
    text = ""
    define = ""
    
    @staticmethod
    def get_meaning():
        """Get the meaning of the entered text using the Chat Completions API."""
        
        if not State.text:
            st.warning("Please enter a word !!")
            return
        try:
            response = model.generate_content(f"Provide the definition of '{State.text}' in a very short sentence and give an example sentence using that word. Also, provide synonyms. Present it as three bullet points(Definition, Example Sentence, Synonyms). Dont provide any answer if theat {State.text} is not existed on any english dictionary.")
            State.define = response.text
        except Exception as e:
            # Handle error in the Google API
            st.error(f"Error with LLM: {e}")
            
    @staticmethod
    def set_text(text):
        """Set the entered text in the app state."""
        State.text = text
        

def main():
     st.set_page_config(
        page_title="Streamlit: Multilingual Dictionary App",
        page_icon=":globe_with_meridians:",
        layout="wide",
    )
     # Add custom CSS for styling
     footer="""<style>
a:link , a:visited{
color: red;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p> 🚀 Built with Streamlit by <a href = "https://github.com/ThimalCaldera"  target="blank">Thimal Caldera </a> | 📚 Powered by Gemini-Pro</p>
</div>
"""
     st.markdown(footer,unsafe_allow_html=True)
        
     
     # Main title of the app
     
     st.image("dictionary.png", width=100)
     st.title(":red[Dictionary] Application")
     
 
    # Text area for user input
     State.text = st.text_area("Enter the word:")
 
     if st.button("Get Meaning", key="meaning_button"):
        State.get_meaning()
        
        
     # Horizontal line for visual separation
     st.markdown("---")
    
 
    # Display the retrieved definition
     if State.define:
        st.subheader("Definition: "+ State.text)
        tts  = gTTS(text =  State. text , lang = "en", slow = False) 
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp_word: #To diplay the audio of text-to-speech 
                tts.save(fp_word.name)
                st.audio(fp_word.name, format="audio/mp3")
        st.write(State.define)
        
        tts  = gTTS(text = State.define, lang = "en", slow = False)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                st.audio(fp.name, format="audio/mp3")
                
        st.markdown(footer, unsafe_allow_html=True)

        
        
if __name__ == "__main__":
    main()
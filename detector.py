import streamlit as st

# List of words to detect
DETECTION_WORDS = [
    "Moreover", "Furthermore", "Consequently", "Therefore", "Additionally",
    "Notably", "Significantly", "Importantly", "Thereafter", "Predominantly",
    "Immutable", "Elongated", "intricate tapestry", "delve", "dynamic",
    "interplay", "captivate", "leverage", "tapestry", "underscores",
    "leveraging", "uncharted waters", "embark", "perplexing", "testament",
    "delving", "resonate", "imperative", "realm", "fabric", "cacophony",
    "interplay", "nuanced", "complacency", "crossroads", "threads", "comprehensive", "paved",
    "reverberate", "shedding", "facets", "realm", "unraveling", "in-depth", "encompasses", "showcasing", "indicative",
    "cohesive","underscore"
]

# Convert all words to lowercase for case-insensitive matching
DETECTION_WORDS_LOWER = [word.lower() for word in DETECTION_WORDS]

def check_for_detection_words(text):
    # Split the text into words and convert to lowercase
    words = text.lower().split()
    # Check if any detection words are in the text
    for word in DETECTION_WORDS_LOWER:
        if word in words:
            return True
    return False

def check_detection(text):
    found_words = []
    for detection in DETECTION_WORDS:
        if detection.lower() in text.lower():
            found_words.append(detection)
    return found_words


# Streamlit app
def main():
    st.title("The ChatGPT detector App😎")

    # Text area for user input
    user_input = st.text_area("Enter your text here:")
     
    # Check words found from the detection list
    found_words = check_detection(user_input)
    
    # Display the input text
    st.markdown("---")
    st.subheader("Input Text:")
    st.text(user_input[:300] + "..." if len(user_input) > 300 else user_input)
    st.markdown("---")
    
    # Display detection result message with styling
    if len(found_words) > 3:
        st.error("THIS IS WRITTEN BY CHATGPT!!!!😡")
    elif len(found_words) == 3:
        st.error("Okay I think your text is written by an AI😐")
    elif len(found_words) == 2:
        st.error("Hmmm, this text is sus😶")

    elif len(found_words) == 1:
        st.error("Hmm, I smell something fishy on this essay, but carry on then🙂")
    else:
        st.success("huh, nothing fishy here...")

if __name__ == "__main__":
    main()

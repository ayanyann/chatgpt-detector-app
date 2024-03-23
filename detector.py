import streamlit as st

# List of words and sentences to detect
detection_list = [
    "Moreover",
    "Furthermore",
    "Consequently",
    "Therefore",
    "Additionally",
    "Notably",
    "Significantly",
    "Importantly",
    "Thereafter",
    "Predominantly",
    "Immutable",
    "Elongated",
    "intricate tapestry",
    "delve",
    "dynamic",
    "interplay",
    "captivate",
    "leverage",
    "tapestry",
    "underscores",
    "leveraging",
    "uncharted waters",
    "embark",
    "perplexing",
    "testament",
    "delving",
    "resonate",
    "imperative",
    "realm",
    "fabric",
    "cacophony",
    "interplay",
    "nuanced",
    "complacency",
    "crossroads",
    "threads",
    "comprehensive"
]

def check_detection(text):
    found_words = []
    for detection in detection_list:
        if detection.lower() in text.lower():
            found_words.append(detection)
    return found_words

def main():
    st.title("The real ChatGPT Detector App😎")
    
    # Text input widget
    input_text = st.text_area("Enter your text here:", max_chars=500)
    
    # Check words found from the detection list
    found_words = check_detection(input_text)
    
    # Display the input text
    st.markdown("---")
    st.subheader("Input Text:")
    st.text(input_text[:300] + "..." if len(input_text) > 300 else input_text)
    st.markdown("---")
    
    # Display detection result message with styling
    if len(found_words) > 3:
        st.error("THIS IS WRITTEN BY CHATGPT, OHH YOU'RE SOOOO DONE BRO!😡")
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

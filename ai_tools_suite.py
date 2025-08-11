import streamlit as st

st.set_page_config(page_title="AI Tools Suite", page_icon="🤖", layout="centered")

st.title("🤖 AI Tools Suite (Free Version)")

# Sidebar menu
menu = st.sidebar.radio("Choose a Tool", [
    "💬 FAQ Chatbot Prompt Builder",
    "🎥 YouTube Shorts Script Prompt Builder"
])

# -------------------------
# TOOL 1: FAQ Chatbot Prompt Builder
# -------------------------
if menu == "💬 FAQ Chatbot Prompt Builder":
    st.header("💬 FAQ Chatbot Prompt Builder")
    st.write("Upload or paste your FAQs, then enter a question to generate a prompt for ChatGPT.")

    business_name = st.text_input("Business Name", "My Company")
    faq_text = st.text_area("Paste your FAQs here", height=200, 
                            placeholder="Q: What are your business hours?\nA: We are open 9am-5pm, Monday to Friday.\n...")
    user_question = st.text_input("Customer Question", 
                                  placeholder="What time do you open on Saturdays?")

    if st.button("Generate Prompt for ChatGPT", key="faq_button"):
        if faq_text.strip() and user_question.strip():
            prompt = (
                f"You are a customer support assistant for {business_name}. "
                f"Here are the FAQs:\n\n{faq_text}\n\n"
                f"Please answer this customer question based only on the FAQs above:\n\n{user_question}"
            )
            st.success("✅ Prompt generated! Copy and paste into ChatGPT:")
            st.code(prompt, language="text")
        else:
            st.warning("Please fill out both the FAQs and the question.")

# -------------------------
# TOOL 2: YouTube Shorts Script Prompt Builder
# -------------------------
elif menu == "🎥 YouTube Shorts Script Prompt Builder":
    st.header("🎥 YouTube Shorts Script Prompt Builder")
    st.write("Fill in the details to generate a powerful prompt for ChatGPT to create your YouTube Shorts script.")

    topic = st.text_input("Topic", "How AI is changing education")
    tone = st.selectbox("Tone", ["Funny", "Inspirational", "Educational", "Dramatic"])
    duration = st.slider("Duration (seconds)", 30, 60, 45)

    if st.button("Generate Prompt for ChatGPT", key="shorts_button"):
        if topic.strip():
            prompt = (
                f"Write a {duration}-second YouTube Shorts script about '{topic}' "
                f"in a {tone.lower()} tone. The script should be punchy, engaging, "
                f"and end with a strong call-to-action."
            )
            st.success("✅ Prompt generated! Copy and paste into ChatGPT:")
            st.code(prompt, language="text")
        else:
            st.warning("Please enter a topic.")

# Footer
st.markdown("---")
st.caption("💡 Tip: Paste these prompts into free ChatGPT at chat.openai.com to get responses without an API key.")

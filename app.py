# Import required packages
import os
import streamlit as st
from langchain.llms import HuggingFaceHub, OpenAI
from llm_rap.classes.battle import *
from llm_rap.classes.agent import mc
from llm_rap.classes.round import round

def load_llm(llm_model):
	if llm_model == "T5":
		llm =HuggingFaceHub(repo_id="google/flan-t5-xl")
	elif llm_model == "GPT-3":
		llm = OpenAI()
	return llm

# Main function
def main():
	st.image("logo.jpg")
	st.header("About what do you wanna rap?")

	open_ai_api_key = st.text_input("Enter your OpenAI API key", type="password")
	os.environ["OPENAI_API_KEY"] = open_ai_api_key

	hf_api_key = st.text_input("Enter your hugging face API key", type="password")
	os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_api_key


	llm_model = st.selectbox("Select a language model", ["T5", "GPT-3"])

	name = st.text_input("What's the mc name?")
	context = st.text_input("Write a context for your mc.")
	about = st.text_input("What do you want to rap about?")

	if st.button("Rap") and name and context and about:
		with st.spinner("Loading language model..."):
			llm = load_llm(llm_model)
		with st.spinner("Rapping..."):
			mc1 : mc = mc(llm_model, name=name, context=context)
			mc2 : mc = mc(llm_model, name="2mc", context=context)
			rapBattle : Battle = Battle(mc1, mc2)
			
			rapBattle.startBattle(5)

# Run the main function
if __name__ == '__main__':
	main()

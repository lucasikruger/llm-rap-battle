# Import required packages
import os
import streamlit as st
from langchain.llms import HuggingFaceHub, OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
from llm_rap.classes.agent import mc
from llm_rap.classes.battle.battle import Battle
from llm_rap.classes.round import round

def load_llm(llm_model):
	if llm_model == "T5":
		llm =HuggingFaceHub(repo_id="gpt2")
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
			mc1 = mc.Mc(llm, name=name, context=context, initialTheme=about)
			mc2 = mc.Mc(llm, name="2mc", context=context, initialTheme=about)
			rapBattle = Battle(mc1, mc2)
			
			#output1, output2 = rapBattle.startBattle(5)
		beams = mc1.init_rap()
		for i, beam in enumerate(beams):
			st.write(f'i: {i} beam: {beam}')
		#st.text(output2)

# Run the main function
if __name__ == '__main__':
	main()

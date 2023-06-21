import os, shutil
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
from transformers import (GPT2LMHeadModel, GPT2Tokenizer, pipeline, AutoTokenizer, AutoModelForSeq2SeqLM)

class Mc():

    def __init__(self, model, name, context, initialTheme):
        self.initialTheme= initialTheme
        self.name = name
        self.context = context
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.llm = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=self.tokenizer.eos_token_id, temperature=1)

    def init_rap(self):

        tokenizer = AutoTokenizer.from_pretrained("bigscience/T0pp")
        model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/T0pp")

        inputs = tokenizer.encode("Is this review positive or negative? Review: this is the best cast iron skillet you will ever buy", return_tensors="pt")
        outputs = model.generate(inputs)
        return(tokenizer.decode(outputs[0]))


        #generator = pipeline('text2text-generation', model='bigscience/T0')
        #res = generator('Make the lyrics for a song that talks about gaming', max_length=100, do_sample=True, top_k=50,top_p=0.95, num_return_sequences=10)
        #nput_ids = self.tokenizer.encode('So he pointed his gun to me and said', return_tensors='pt')
        
        #output = self.llm.generate(input_ids, max_length=150, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=10, temperature=1)
        #res = []
        #for beam in output:
            #res.append(self.tokenizer.decode(beam, skip_special_tokens=True))

        return res



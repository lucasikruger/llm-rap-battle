import os, shutil

class Mc():

    def __init__(self, model, name, context):

        self.llm = model
        self.name = name
        self.context = context

    def rap(self, about): 

        request = f"""
        You are an mc, your name is {self.name}. 
        Your context is this: {self.context}.
        And you will rap about: {about}.
        Your only rap answer answer is:
        """
        return self.llm(request)


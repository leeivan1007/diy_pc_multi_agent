import openai
from langchain import LLMChain, OpenAI, PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class Agent():
    
    def __init__(self, agent_name, prompt, model):
        
        self.agent_name = agent_name
        self.memory = []
        
        template = ChatPromptTemplate.from_template(prompt)
        model = ChatOpenAI(model=model, temperature=0.7)
        parser = StrOutputParser()

        self.llm = template | model | parser
        
    def forward(self):
        pass
    
    def __call__(self, component_dict):
        
        component_dict = self.forward(component_dict)
        
        return component_dict
    
    def get_component_list(self, component_dict):

        component_list = ''

        for i, (key, value) in enumerate(component_dict.items()):
            
            num = i + 1
            if value:
                component_list += f'{num}. {key}: {value["name"]} | price: {value["price"]}\n'
            else:
                component_list += f'{num}. {key}: None | price: None \n'

        return component_list
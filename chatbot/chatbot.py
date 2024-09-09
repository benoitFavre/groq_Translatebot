from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import SystemMessage
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_groq import ChatGroq
from chatbot.config import GROQ_API_KEY, MODEL_NAME, SYSTEM_PROMPT, RESPONSE_TEMPLATE
#from langchain.globals import set_debug

class ChatbotManager:
    def __init__(self, origin_language, target_language,intention_options):
        self.groq_chat = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=MODEL_NAME,
            temperature=0.7
        )
        #set_debug(True)
        response_schemas = [
            ResponseSchema(name="correction", description="Corrected text"),
            ResponseSchema(name="translation", description="The translation"),
            ResponseSchema(name="note", description="Related notes")
        ]
        self.output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

        self.prompt_template = ChatPromptTemplate.from_messages([
            SystemMessage(content=SYSTEM_PROMPT(origin_language,target_language,intention_options)),
            HumanMessagePromptTemplate.from_template("{human_input}\n\n{format_instructions}")
        ])
        
        self.conversation = self.prompt_template | self.groq_chat 

    def get_response(self, user_input):
        format_instructions = self.output_parser.get_format_instructions()
        raw_response = self.conversation.invoke({
            "human_input": user_input,
            "format_instructions": format_instructions
        })
        
        # Parser la réponse brute
        structured_response = self.output_parser.parse(raw_response.content)

        # Ajout des métadata
        structured_response.update(raw_response.response_metadata)

        return structured_response
    
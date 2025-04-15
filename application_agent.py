from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from leave_application_writer import (
    generate_leave_application_bn,
    generate_leave_application_en,
)
from llm_model import llm

tools = [generate_leave_application_en, generate_leave_application_bn]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
)


def run_with_agent(template: str, user_name: str, applied_date: str):
    temp = PromptTemplate.from_template(
        template + " where my name is {user_name} and date is {applied_date}"
    )
    input_str = temp.format(user_name=user_name, applied_date=applied_date)
    print(f"\nInput Prompt: {input_str}\n")
    response = agent.invoke({"input": input_str})
    print(f"\n {response["output"]} \n")

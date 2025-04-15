import random
from langchain.tools import tool
from llm_model import llm
from english_knowledge import sick_leaves_en
from bangla_knowledge import sick_leaves_bn


@tool
def generate_leave_application_bn(input_str: str) -> str:
    """
    Generate a leave application in bangla or bengali language based on a string containing name and date.
    Expected format: "name: Pritom, date: 01.10.2010"
    """
    parts = dict(item.strip().split(":") for item in input_str.split(","))
    name = parts["name"].strip()
    date = parts["date"].strip()

    return format_templates(sick_leaves_bn, date, name)


@tool
def generate_leave_application_en(input_str: str) -> str:
    """
    Generate a leave application in english language based on a string containing name and date.
    Expected format: "name: Pritom, date: 01.10.2010"
    """
    parts = dict(item.strip().split(":") for item in input_str.split(","))
    name = parts["name"].strip()
    date = parts["date"].strip()

    return format_templates(sick_leaves_en, date, name)


def format_templates(templates, date, name):
    unique_template = random.sample(templates, 1)
    return "\n\n".join(
        f"Subject: {tpl['subject'].format(date=date)}\n{tpl['body'].format(employee_name=name or 'John Doe', m_name='Cefalo HR', date=date)}"
        for tpl in unique_template
    )

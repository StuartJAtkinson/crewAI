import os
from crewai import Agent, Task, Crew, Process

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

from langchain_community.llms import HuggingFaceHub
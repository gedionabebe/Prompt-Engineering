# Prompt-Engineering
## In-context learning with GPT-3 and other Large Language Models

Table of contents

- Overview
- Requirements
- Install
- Repository Structure
- Contrbutors

## Overview

Large Language Models coupled with multiple AI capabilities are able to generate
images and text, and also approach/achieve human level performance on a number of
tasks. The world is going through a revolution in art (DALL-E, MidJourney, Imagine, etc.),
science (AlphaFold), medicine, and other key areas, and this approach is playing a role in
this revolution.

In this project we will systematically explore strategies that help generate prompts
for LLMs to extract relevant entities from job descriptions and also to classify web pages
given only a few examples of human scores. You will be also required to compare
responses and accuracies of multiple LLM models for given prompts. These are the sub taks for this project:

1. Given a news item as json with title, description, and body of the content,
return a score between 0 and 10 in one or two significant digits e.g. (1.2 or
0.33).

2. Given a job description text, return the list of entities (and their relationship
if possible) extracted from the job description by the LLM model.

## Requirements
>Python
>
>Pip
>
>Pandas
>
>Sklearn
>
>DVC
>
>Mlflow
>
>Cohere

## Install
1.Install the project
```
git clone https://github.com/gedionabebe/Prompt-Engineering.git
cd Prompt-Engineering
pip install -r requirements.txt
```

## Repository Structure
```bash
├── .github/workflows(Github actions)
│   
├── data(Project data)
│   
├── log(Log file)
│
├── notebooks(Jupyter notebooks)
│
├── scripts(Python code)
│
├── tests(Unit tests)
│
├── README.md(Project information)
│
├── requirements.txt(Porject requirements)
```
## Contrbutors

- `Gedion Abebe`

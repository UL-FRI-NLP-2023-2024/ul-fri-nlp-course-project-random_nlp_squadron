# Natural language processing course 2023/24: `Slovenian Instruction-based Corpus Generation`

test commit

## Team: RANDOM NLP SQUADRON

- Andraž Čeh ([@student8694](https://github.com/student8694))
- Tilen Miklavič ([@tilenmiklavic](https://github.com/tilenmiklavic))
- Tom Sojer ([@tomssojer](https://github.com/tomssojer))

## Project Overview

This project focuses on utilizing Large Language Models (LLMs) to process and execute complex Slovene instructions. The objective is to collect and refine a conversational dataset to improve a multilingual LLM's Slovene performance, responding to the growing use of AI assistants in diverse fields.

## Methodology

1. **LLM Review**: Select a suitable LLM for the project, considering available infrastructure such as SLING, VEGA, or Nvidia A100 GPUs.
2. **Data Preparation**:
   - Analyze dataset construction techniques for instruction-based LLMs.
   - Develop a data collection plan, identifying potential sources (e.g., forums, websites).
   - Implement tools for data collection and organization, ensuring the dataset is conducive to model fine-tuning.
3. **Model Adaptation** (Optional): Utilize the prepared dataset to fine-tune an existing LLM, enhancing its conversational capabilities in Slovene.

## Repository Structure

- `docs/`: Contains all report documents, both source files and PDFs.
- `src/`: Contains the source code for the model implementation and analysis.
- `data/`: Contains all datasets required for model training.
- `presentation/`: Contains the slides for the final presentation.

### Milestones

- [x] [Milestone 1](https://github.com/UL-FRI-NLP-2023-2024/ul-fri-nlp-course-project-random_nlp_squadron/milestone/1)
- [Milestone 2 - 3. 5.](https://github.com/UL-FRI-NLP-2023-2024/ul-fri-nlp-course-project-random_nlp_squadron/milestone/2)
- [Milestone 3 - 24. 5.](https://github.com/UL-FRI-NLP-2023-2024/ul-fri-nlp-course-project-random_nlp_squadron/milestone/3)

## Objectives

- Understand the architecture and capabilities of LLMs.
- Collect and organize a large Slovene conversational dataset.
- Fine-tune a multilingual LLM to improve its conversational abilities in Slovene.

## References

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
- [Llama 2: Open foundation and fine-tuned chat models](https://arxiv.org/abs/2307.09288)
- [BLOOM: A 176B-Parameter Open-Access Multilingual Language Model](https://arxiv.org/abs/2211.05100), [Model on Hugging Face](https://huggingface.co/bigscience/bloom)

## How to run Scrapy

It is recommended to use SLING to run the crawler as a lot of compute power is available. Once logged in to the login node, run the command below for the crawler to start working. After the job has ended, the output will be stored in xml files.

```
sbatch run.sh crawler_name
```

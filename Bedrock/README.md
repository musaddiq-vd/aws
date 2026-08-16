# Quickstart

## Generate Text — for OpenAI Responses

This example demonstrates how to generate text using the OpenAI-compatible
Responses API on Amazon Bedrock.

### File

`Generate_text_OpeAI.py`

### Setup

# Step 1: Generate API key
Generate a short-term API key to authenticate your requests.

# Step 2: Install the SDK and make your first API request
Choose API method
bedrock recommend starting with the OpenAI-compatible Responses API.

    Responses → Modern/Agent/
    Converse → Common Chat/ common interface for multiple Bedrock models
    Invoke → Direct/ request/response format

# Set environment variables
refer aws console ------
set OPENAI_API_KEY="your-key"
set OPENAI_BASE_URL="https://bedrock-mantle.us"

# Install the SDK
pip install openai boto3

# Run code 
01_Generate_text_OpeAI.py

    01.1_01_Generate_text_OpeAI.py

02_Stream responses.py

03_Analyze media_documents.py

04_Analyze media_image.py

# Concepts

## ON_DEMAND vs INFERENCE_PROFILE
ON_DEMAND → Directly invokes a model available in the current region.

INFERENCE_PROFILE → Routes the request through an AWS-managed profile, commonly for cross-region inference.

## GPT-OSS 20B vs GPT-OSS Safeguard 20B
GPT-OSS 20B → General-purpose model for chat, reasoning, coding, and generation.

GPT-OSS Safeguard 20B → Safety-focused model fine-tuned for content safety classification and moderation.

## Choose API method
bedrock recommend starting with the OpenAI-compatible Responses API.

    ### Responses → Modern/Agent/
    ### Converse → Common Chat/ common interface for multiple Bedrock models
    ### Invoke → Direct/ request/response format



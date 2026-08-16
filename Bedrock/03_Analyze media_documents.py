
import boto3  

client = boto3.client("bedrock-runtime", region_name="us-east-1")  

with open("new_sop.pdf", "rb") as f: 
    doc_bytes = f.read()  

response = client.converse(
    modelId="amazon.nova-lite-v1:0",
    messages=[{
        "role": "user",
        "content": [
            {
                "document": {
                    "format": "pdf",
                    "name": "document",
                    "source": {"bytes": doc_bytes}
                }
            },
            {"text": "Summarize this document."}
        ]
    }]
)
print(response["output"]["message"]["content"][0]["text"])
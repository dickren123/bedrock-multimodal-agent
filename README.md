Multimodal Agent with LLM(Bedrock), AST(Transcribe), TTS(Polly)

Forked from [Amazon Bedrock Voice Conversation](https://github.com/aws-samples/amazon-bedrock-voice-conversation) and refine bugs, update according to Bedrock/Transcribe/Polly's new features.

How to run APP:
```
    python install -r ./requirements.txt
```

```
    export AWS_ACCESS_KEY_ID=<...>
    export AWS_SECRET_ACCESS_KEY=<...>
    export AWS_DEFAULT_REGION=<...> # Optional, defaults to us-east-1 
    export MODEL_ID=<...># Optional, defaults to Claude3 Haiku
```

```
    python ./app.py
```
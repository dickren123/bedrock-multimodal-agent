api_request_list = {
    'anthropic.claude-3-5-sonnet-20240620-v1:0': {
        "modelId": "anthropic.claude-3-5-sonnet-20240620-v1:0",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            
        }
    },
    'anthropic.claude-3-haiku-20240307-v1:0': {
        "modelId": "anthropic.claude-3-haiku-20240307-v1:0",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            
        }
    },
    'amazon.titan-text-express-v1': {
        "modelId": "amazon.titan-text-express-v1",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            "inputText": "",
            "textGenerationConfig": {
                "maxTokenCount": 4096,
                "stopSequences": [],
                "temperature": 0,
                "topP": 1
            }
        }
    },
    'amazon.titan-text-lite-v1': {
        "modelId": "amazon.titan-text-lite-v1",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            "inputText": "",
            "textGenerationConfig": {
                "maxTokenCount": 4096,
                "stopSequences": [],
                "temperature": 0,
                "topP": 1
            }
        }
    },
    'anthropic.claude-v2:1': {
        "modelId": "anthropic.claude-v2:1",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            "prompt": "",
            "max_tokens_to_sample": 300,
            "temperature": 0.5,
            "top_k": 250,
            "top_p": 1,
            "stop_sequences": [
                "\n\nHuman:"
            ],
            "anthropic_version": "bedrock-2023-05-31"
        }
    },
    'anthropic.claude-v2': {
        "modelId": "anthropic.claude-v2",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            "prompt": "",
            "max_tokens_to_sample": 300,
            "temperature": 0.5,
            "top_k": 250,
            "top_p": 1,
            "stop_sequences": [
                "\n\nHuman:"
            ],
            "anthropic_version": "bedrock-2023-05-31"
        }
    },
    'meta.llama2-13b-chat-v1': {
        "modelId": "meta.llama2-13b-chat-v1",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            "prompt": "",
            "max_gen_len": 512,
            "temperature": 0.2,
            "top_p": 0.9
        }
    },
    'meta.llama2-70b-chat-v1': {
        "modelId": "meta.llama2-70b-chat-v1",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            "prompt": "",
            "max_gen_len": 512,
            "temperature": 0.2,
            "top_p": 0.9
        }
    },
    'cohere.command-text-v14': {
        "modelId": "cohere.command-text-v14",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            "prompt": "",
            "max_tokens": 1024,
            "temperature": 0.8,
        }
    },
    'cohere.command-light-text-v14': {
        "modelId": "cohere.command-light-text-v14",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            "prompt": "",
            "max_tokens": 1024,
            "temperature": 0.8,
        }
    },
}


def get_model_ids():
    return list(api_request_list.keys())

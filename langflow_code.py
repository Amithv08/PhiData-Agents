from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-CnrRP": {},
  "ParseData-9xdPU": {},
  "Prompt-3D2d0": {},
  "SplitText-Gzx9p": {},
  "OpenAIModel-nWCKA": {},
  "ChatOutput-yUZ9M": {},
  "AstraDB-CPAwR": {},
  "OpenAIEmbeddings-8TcEi": {},
  "AstraDB-71tWa": {},
  "OpenAIEmbeddings-snhnu": {},
  "File-l7cIk": {}
}

result = run_flow_from_json(flow="Vector Store RAG.json",
                            input_value="message",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
import chainlit as cl

@cl.on_window_message
async def window_message(message: str):
  print(message)
  if message.startswith("Client: "):
    await cl.Message(content=f"Window message received: {message}").send()


@cl.on_message
async def message():
  await cl.send_window_message("Server: Hello from Chainlit")

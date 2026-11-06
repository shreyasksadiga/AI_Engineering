import asyncio
import os
import  markdown


from openai import AsyncOpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown



load_dotenv()

class ChatService:
    system_prompt = "you are a good assistence"
    def __init__ (self) : 
        api_key = os.environ["OPEN_ROUTER_KEY"]
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    async def ask (self,user_prompt:str) -> str : 
        self.user_prompt = user_prompt
        response  = await self.client.chat.completions.create(
            model="openrouter/free",
            messages = [
                {
                    "role" : "system",
                    "content" : self.system_prompt
                },
                {
                    "role" : "user",
                    "content" : self.user_prompt
                }
            ],
            max_tokens=1000,
            temperature=0.5
        )
        return response.choices[0].message.content

async def main() :
    chat = ChatService()
    query = input("Query : ")
    ans = await chat.ask(query)
    console = Console()
    md = Markdown(ans)
    console.print(md)
    

if __name__ == '__main__' :
    asyncio.run(main())



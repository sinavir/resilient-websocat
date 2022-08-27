#! /usr/bin/env nix-shell
#! nix-shell -i python

import asyncio
import logging
import sys
import websockets

#logging.basicConfig(level = logging.DEBUG)

async def listen(url):
    async for ws in websockets.connect(url):
        try: 
            async for msg in ws:
                print(msg)
        except websockets.ConnectionClosed as e:
            logging.info(f"Exception caught: {e}")
        logging.info("Connection ended, retrying")
    logging.info("End of connection")

def main():
    asyncio.run(listen(sys.argv[1]))

if __name__ == "__main__" :
    main()

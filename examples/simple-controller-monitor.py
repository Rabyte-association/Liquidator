#
#   zeby dzialalo przeniesc do folderu 'controller' i dopiero uruchomic
#   zeby wylaczyc przytrzymac ctrl-c przez kilka sekund bedac w oknie terminala
#

import os
import controller
import asyncio


async def ConsoleInfo():
    while True:
        os.system('clear')
        pad.ShowDebug()


async def main():
    await asyncio.gather(controller.Initialize(), ConsoleInfo())

pad = controller.pad
asyncio.run(main())

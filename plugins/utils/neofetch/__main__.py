""" Userge Neofetch """

from userge import userge, Message

import subprocess

@userge.on_cmd("neofetch", about={
    'header': "Displays system information using neofetch."}
    'usage':"{tr}neofetch", allow_via_bot=True)
async def neofetch(message: Message):
    stdout, stderr = await run_command(["neofetch", "-stdout"])
    await message.edit(f"```\n{stdout.decode('utf-8')}```")

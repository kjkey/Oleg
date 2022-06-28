from aiogram.utils import executor
from bot.commands import *
from bot.config.create import CreateBot


class Bot:
    '''Запуск команд'''
    reset.reset.register_commands(CreateBot.dp)
    start.start.register_commands(CreateBot.dp)
    down1.down1.register_commands(CreateBot.dp)
    down2.down2.register_commands(CreateBot.dp)
    down3.down3.register_commands(CreateBot.dp)
    down4.down4.register_commands(CreateBot.dp)
    down5.down5.register_commands(CreateBot.dp)
    pars1.pars1.register_commands(CreateBot.dp)
    pars2.pars2.register_commands(CreateBot.dp)
    download1.download1.register_commands(CreateBot.dp)
    download2.download2.register_commands(CreateBot.dp)

    executor.start_polling(CreateBot.dp, skip_updates=True)
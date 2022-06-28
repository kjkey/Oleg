from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
import aiohttp
from aiogram.types import message
from bot.commands.commands_admin import Mydialog


class download1:
    '''скачивание файла и отправка пользователю для 1, 2 и 5 функций down'''
    #@staticmethod
    async def download(message : types.Message, state: FSMContext):
        async with aiohttp.ClientSession() as session:
            user_data = await state.get_data()
            html = user_data['htm_l'].split(' ')
            str = 'http://tolstoy.ru' + html[int(message.text.title()) - 1]
            format = user_data['format'].split(' ')
            print(str)
            async with session.get(str) as resp:
                S = format[int(message.text.title())*5-4]
                file = "text" + '.' + S
                pdf = open(file, 'wb')
                pdf.write(await resp.read())
                pdf.close()
                await message.reply_document(open(file, 'rb'))
            await state.finish()

    #@staticmethod
    def register_commands(dp: Dispatcher):
        '''обработчик команд'''
        dp.register_message_handler(download1.download, state=Mydialog.form)
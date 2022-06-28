from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
import aiohttp
from bot.commands.commands_admin import Mydialog


class download2:
    '''скачивание файла и отправка пользователю для 3 и 4 функций down'''
    async def download(message : types.Message, state: FSMContext):
        async with aiohttp.ClientSession() as session:
            user_data = await state.get_data()
            html = user_data['htm_l'].split(' ')
            format = user_data['format'].split(' ')
            answer = user_data['answer']
            str = 'http://tolstoy.ru' + html[(((int(answer))-1)*3) + int(message.text.title())-1]
            print(str)
            async with session.get(str) as resp:
                S = format[int(message.text.title())-1]
                file = "text" + S
                pdf = open(file, 'wb')
                pdf.write(await resp.read())
                pdf.close()
                await message.reply_document(open(file, 'rb'))
            await state.finish()

    def register_commands(dp: Dispatcher):
        '''обработчик команд'''
        dp.register_message_handler(download2.download, state=Mydialog.form)
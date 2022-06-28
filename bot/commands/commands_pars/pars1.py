from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bs4 import BeautifulSoup as BS
import aiohttp
import re
from bot.commands.commands_admin import Mydialog

class pars1:
    async def parc(message : types.Message, state: FSMContext):
        '''поиск ссылок на скачивание и выдача пользователю вариантов для 1, 2 и 5 функций down'''
        user_data = await state.get_data()
        html = user_data['htm_l'].split(' ')
        format = ''
        async with aiohttp.ClientSession() as session:
            str = 'http://tolstoy.ru' + html[int(message.text.title()) - 1]
            async with session.get(str) as resp:
                html = BS(await resp.text(), 'html.parser').find_all("a", text=re.compile("Скачать"))
                temp = ''
                count = 0
                date = ''
                for i in html:
                    s = repr(count + 1)
                    format += html[count].text + ' '
                    temp += s + '.' + html[count].text + '\n'
                    date += html[count].get("href") + ' '
                    count += 1
                await message.reply(temp)
            await state.update_data(format=format)
            await message.answer(text='Напиши номер варианта')
            await Mydialog.form.set()
            await state.update_data(htm_l=date)
    def register_commands(dp: Dispatcher):
        '''обработчик команд'''
        dp.register_message_handler(pars1.parc, state=Mydialog.otvet)
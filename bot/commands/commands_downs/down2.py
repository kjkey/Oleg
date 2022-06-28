from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bs4 import BeautifulSoup as BS
import aiohttp
from bot.commands.commands_admin import Mydialog

class down2:
    async def down(message : types.Message, state: FSMContext):
        '''нахождение всей литературы в публицистическом разделе и выдача пользователю'''
        async with aiohttp.ClientSession() as session:
            str = 'http://tolstoy.ru/creativity/publicism/'
            async with session.get(str) as resp:
                html = BS(await resp.text(), 'html.parser').find_all("a", class_="tit_c2")
                temp = ''
                count = 0
                date=''
                for i in html:
                    temp += repr(count + 1) + '.' + html[count].text + '\n'
                    date += html[count].get("href")+' '
                    count += 1
                await message.reply(temp)
            await message.answer(text='Напиши номер варианта')
            await Mydialog.otvet.set()
            await state.update_data(htm_l=date)
    def register_commands(dp: Dispatcher):
        '''обработчик команд'''
        dp.register_message_handler(down2.down, commands=['Publicism'])

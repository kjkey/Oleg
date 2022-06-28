from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bs4 import BeautifulSoup as BS
import aiohttp
import re
from bot.commands.commands_admin import Mydialog

class down4:
    async def down(message : types.Message, state: FSMContext):
        '''нахождение всей литературы в разделе писем и выдача пользователю'''
        async with aiohttp.ClientSession() as session:
            j = 1
            date = ''
            temp = ''
            count = 0
            costyl = 9
            while j < 5:
                S = 'http://tolstoy.ru/creativity/letters/?df=&dt=&q=&page='+str(j)
                async with session.get(S) as resp:
                    html1 = BS(await resp.text(), 'html.parser').find_all("a", text=re.compile("Письма, 1"))
                    html = BS(await resp.text(), 'html.parser').find_all("a", text=re.compile("Скачать "))
                    let = 0
                    for i in html1:
                        temp += repr(count + 1) + '.' + html1[let].text + '\n'
                        date += html[(let+1) * 3 - 3 + costyl].get("href")+' '
                        date += html[(let+1) * 3 - 2 + costyl].get("href") + ' '
                        date += html[(let+1) * 3 - 1 + costyl].get("href") + ' '
                        count += 1
                        let +=1
                j = 1 + j
                costyl = 0
            await message.reply(temp)
            await message.answer(text='Напиши номер варианта')
            await Mydialog.otvet1.set()
            await state.update_data(htm_l=date)
    def register_commands(dp: Dispatcher):
        '''обработчик команд'''
        dp.register_message_handler(down4.down, commands=['Letters'])
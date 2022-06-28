from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.commands.commands_admin import Mydialog

class pars2:
    async def parc(message : types.Message, state: FSMContext):
        '''выдача пользователю вариантов и сохранение прошлого ответа для 3 и 4 функций down'''
        await state.update_data(answer=message.text.title())
        await message.answer(text='1.Скачать EPUB\n2.Скачать FB2\n3.Скачать MOBI')
        format = '.epub .fb2 .mobi'
        await state.update_data(format = format)
        await Mydialog.form1.set()

    def register_commands(dp: Dispatcher):
        '''обработчик команд'''
        dp.register_message_handler(pars2.parc, state=Mydialog.otvet1)
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.config.create import CreateBot
from bot.keyboards.client_kb import KBoards

class reset:
    async def reset(message : types.Message, state: FSMContext):
        '''сброс работы и вызов меню управления для пользователя'''
        await CreateBot.bot.send_message(message.from_user.id,'состояние сброшено', reply_markup=KBoards.kb_client)
        await state.finish()
    def register_commands(dp: Dispatcher):
        '''обработчик команд'''
        dp.register_message_handler(reset.reset, commands=['reset'], state='*')
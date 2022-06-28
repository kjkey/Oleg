from aiogram import types, Dispatcher
from bot.config.create import CreateBot
from bot.keyboards.client_kb import KBoards

class start:
    async def start(message : types.Message):
        '''вызов меню управление, старт работы и справка для пользователя'''
        await CreateBot.bot.send_message(message.from_user.id, 'Справка.\n'
                                  'Бот посвящен писателю Льву Толстому. С его помощью вы можете скачать'
                                  'его произведения из пяти тематических разделов-художественная литература,'
                                  'публицистика, дневники, письма, а также собрание сочинений.\n'
                                  'После выбора команды бот выдает список с нумерацией. Чтобы он продолжил работу'
                                  'введите номер(цифрами) понравившегося вам варианта. Если у вас произошли неполадки,'
                                  'то командой /reset можно сбросить состояние бота.'
                                  '\nБот присылает литературу в текстовом файле. Для прочтения его в формате,'
                                  'выбранном вами смените его расширение.', reply_markup=KBoards.kb_client)
    def register_commands(dp: Dispatcher):
        '''обработчик команд'''
        dp.register_message_handler(start.start, commands=['start'])

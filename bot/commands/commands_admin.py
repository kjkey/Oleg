from aiogram.dispatcher.filters.state import State, StatesGroup


class Mydialog(StatesGroup):
    '''состояния для менеджера состояний'''
    otvet = State()
    form = State()
    otvet1 = State()
    form1 = State()

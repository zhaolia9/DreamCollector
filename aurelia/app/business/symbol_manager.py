# app/business/symbol_manager.py

from aurelia.app.data.data_provider import DataProvider
from aurelia.app.models.symbol import Symbol

class SymbolManager:

    def __init__(self):
        self.provider = DataProvider()

    def create_symbol(self, name, description):
        return self.provider.create_symbol(Symbol(None, name, description))

    def get_symbol_by_id(self, symbol_id):
        return self.provider.read_symbol_by_id(symbol_id)

    def get_all_symbols(self):
        return self.provider.read_all_symbols()

    def update_symbol(self, symbol_id, name, description):
        return self.provider.update_symbol(Symbol(symbol_id, name, description))

    def delete_symbol(self, symbol_id):
        return self.provider.delete_symbol(symbol_id)
from datetime import date, datetime
from backend.data.data_provider import DataProvider
from backend.models import User, Dream, Symbol, DreamSymbol, Poem

def main():
    dp = DataProvider()

    # Create a user
    user_id = dp.create_user(User(None, "Aurelia Weaver", "aurelia@example.com"))
    print("Created user:", user_id)

    # Create a dream
    dream_id = dp.create_dream(Dream(
        None, user_id, "Silver Lake",
        "I walked across a lake that reflected constellations.",
        date.today(), "Calm", 7
    ))
    print("Created dream:", dream_id)

    # Create a symbol
    symbol_id = dp.create_symbol(Symbol(None, "Water", "Emotion and reflection"))
    print("Created symbol:", symbol_id)

    # Link dream and symbol
    dp.create_dream_symbol(DreamSymbol(dream_id, symbol_id))
    print("Linked dream and symbol")

    # Create a poem
    poem_id = dp.create_poem(Poem(
        None, user_id, dream_id,
        "Stars ripple under my feet; I do not fall.",
        datetime.now()
    ))
    print("Created poem:", poem_id)

    # Read all
    print("Users:", dp.read_all_users())
    print("Dreams:", dp.read_all_dreams())
    print("Symbols:", dp.read_all_symbols())
    print("DreamSymbols:", dp.read_all_dream_symbols())
    print("Poems:", dp.read_all_poems())

if __name__ == "__main__":
    main()

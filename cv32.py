from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler
import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackContext
)
import googlemaps
from telegram_menu import MenuButton
from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler, ButtonType, MenuButton
from direct import Q1, Q2, MainIssues,SubIssues
import re

gmaps = googlemaps.Client(key='AIzaSyBDghz8gAogT1QtPIPdZbonlC08xooIH0Y')

class StartMessage(BaseMessage):
    """Start menu, create all app sub-menus."""

    LABEL = "start"

    def __init__(self, navigation: NavigationHandler, ) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, StartMessage.LABEL)
        sendlocation = SendLocation(navigation)
        pickdate = PickDate(navigation)
        hndl = HandleTheButtonLabel(navigation)
        self.add_button(label="KONUM GÖNDER", callback=sendlocation)
        self.add_button(label="TARİH SEÇ", callback=pickdate)
        self.add_button(label="LBL", callback=hndl)
        #self.add_button(label="KONU SEÇ", callback=picktopic)


    def update(self) -> str:
        """Update message content."""
        name = self.navigation.user_name
        name = name.upper()
        return f"{name}  HOŞGELDİNİZ  "








class SendLocation(BaseMessage):
    """First menu, create an inlined button."""
    LABEL = "KONUM"

    def __init__(self,navigation: NavigationHandler) -> None:
        """Init SecondMenuMessage class."""
        super().__init__(navigation, StartMessage.LABEL, inlined=True)

    def update(self) -> str:
        """Update message content."""
        # emoji can be inserted with a keyword enclosed with ::
        # list of emojis can be found at this link: https://www.webfx.com/tools/emoji-cheat-sheet/
        return ":warnings: Second message"

    @staticmethod
    def run_and_notify() -> str:
        """Update message content."""
        return "This is a notification"


class PickDate(BaseMessage):
    """First menu, create an inlined button."""
    LABEL = "TARİH SEÇ"

    def __init__(self,navigation: NavigationHandler) -> None:

        """Init SecondMenuMessage class."""
        super().__init__(navigation, PickDate.LABEL, inlined=True)
        self.button_label = ""
        self.add_button(label="1 HAFTA", callback= self.aweek,new_row=1,btype=ButtonType.MESSAGE)
        self.add_button(label="1 AY", callback=self.amonth,new_row=1,btype=ButtonType.MESSAGE)
        self.add_button(label="3 AY", callback=self.threemonth,new_row=1)
        self.add_button(label="6 AY", callback=self.sixmonth,new_row=1)
        self.add_button(label="1 YIL", callback=self.ayear,new_row=1)

    def aweek(self) -> str:
        """Return the text content to display, eventually with markdown formatting."""
        if self.get_button(label="1 HAFTA"):
            self.button_label = "1 HAFTA"
            #print(self.button_label)
            print(self.select_buton_label)
        return self.button_label
    def amonth(self) -> str:
        """Return the text content to display, eventually with markdown formatting."""

        if self.get_button(label="1 AY"):
            self.date = "1aySeçildi"
            print(self.navigation.user_name)
            #print(self.navigation.select_menu_button("1 AY"))
            #print(self.navigation.select_menu_button(label=self.label))
            #self.navigation.app_message_button_callback(callback_label=self.amonth, callback_id=self.message_id)

            #print(self.navigation.)
            #self.navigation.app_message_webapp_callback
        #print(self.navigation.get_message(label_message = self.LABEL))

        return "------"


    def threemonth(self) -> str:
        """Return the text content to display, eventually with markdown formatting."""
        return "threemonth"

    def sixmonth(self) -> str:
        """Return the text content to display, eventually with markdown formatting."""
        return "sixmonth"

    def ayear(self) -> str:
        """Return the text content to display, eventually with markdown formatting."""
        return "ayear"

    def update(self) -> str:
        """Update message content."""
        # emoji can be inserted with a keyword enclosed with ::
        # list of emojis can be found at this link: https://www.webfx.com/tools/emoji-cheat-sheet/

        return f"Analiz Yapmak İstediğiniz Ana Konuyu Seçiniz"

    def inl(self):
        inline_keyboard_markup = self.gen_inline_keyboard_content()
        for row in inline_keyboard_markup.inline_keyboard:
            # row is a list of InlineKeyboardButton objects
            for button in row:
                # You can access its properties like `text` {button.text} and `callback_data` {button.callback_data}
                #print(button.text)
                if self.get_button(label=button.text):
                    print(button.text)
                    print()



    @staticmethod
    def run_and_notify() -> str:
        """Update message content."""
        return f" ---- "




class HandleTheButtonLabel(BaseMessage):
    """Second menu, create an inlined button."""

    LABEL = "inlinebutonlabel"

    def __init__(self, navigation: TelegramMenuSession) -> None:
        """Init SecondMenuMessage class."""
        super().__init__(navigation, StartMessage.LABEL, inlined=True)

        print(self.gen_inline_keyboard_content())

    def update(self) -> str:
        """Update message content."""
        # emoji can be inserted with a keyword enclosed with ::
        # list of emojis can be found at this link: https://www.webfx.com/tools/emoji-cheat-sheet/
        print(self.gen_inline_keyboard_content(),"---")
        return ":warning: Second message"


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    api_key = "6050942998:AAE5U98CAFBP5TxF4bbxUfYq4FlcBH_QDF0"

    TelegramMenuSession(api_key).start(StartMessage)


if __name__ == "__main__":
    main()




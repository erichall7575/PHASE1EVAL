from app import util
from app import view
def main_menu():
    while True:
        view.enter_symbol()
        mainselect=input()
        mainselect=str(mainselect).upper()
        if mainselect=='EXIT':
            view.exit_message()
            return None
        
        # Getting info
        jsondata=util.get_chart(mainselect)
        filecreated=util.file_json(jsondata,mainselect)
        view.file_created_message(filecreated)
        
        return main_menu()

def run():
    chart=main_menu()
    if not chart:
        return None
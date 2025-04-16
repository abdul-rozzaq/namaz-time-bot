from src.config.settings import DEBUG, BOT_TOKEN
from argparse import ArgumentParser, RawTextHelpFormatter
from colorama import Fore, init as colorama_init

import uvicorn

from src.services.cli import CLIService


colorama_init(autoreset=True)


def main():
    parser = ArgumentParser(prog="OneHadith", description="📖 OneHadith Telegram bot CLI yordamchi dasturi.", formatter_class=RawTextHelpFormatter)
    parser.add_argument("command", nargs="?", type=str, default="runserver", help=("Quyidagi buyruqlardan birini tanlang:\n" "  runserver       → Lokal serverni ishga tushuradi (default)\n" "  set-webhook     → Telegram bot uchun webhook o'rnatadi\n" "  delete-webhook  → Telegram webhookni o'chiradi\n" "\nMisollar:\n" "  python run.py runserver\n" "  python run.py set-webhook\n" "  python run.py delete-webhook"))

    args = parser.parse_args()
    command = args.command

    service = CLIService()

    if command in ["set-webhook", "delete-webhook"]:
        match command:
            case "set-webhook":
                result, message = service.set_webhook()

            case "delete-webhook":
                result, message = service.delete_webhook()

        if result:
            print(Fore.GREEN + message)
        else:
            print(Fore.RED + "Error " + message)

    elif command == "runserver":
        uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=DEBUG)


if __name__ == "__main__":
    main()

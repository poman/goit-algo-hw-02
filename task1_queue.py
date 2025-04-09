import queue
import random

request_queue = queue.Queue()

def generate_request():
    request = random.randint(1, 999)
    print(f"Створено заявку з номером: {request}")
    request_queue.put(request)

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Заявка {request} оброблена.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    while True:
        user_input = input("Натисніть 'n' для створення заявки, 'p' для обробки заявки, або 'q' для виходу: ").strip().lower()
        if user_input == 'n':
            generate_request()
        elif user_input == 'p':
            process_request()
        elif user_input == 'q':
            print("Програма завершена.")
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()

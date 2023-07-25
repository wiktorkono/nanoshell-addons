import datetime

def showDateTime(prompt):
    current_time = datetime.datetime.now()
    formatted_date = current_time.strftime("%d-%m-%Y")
    formatted_time = current_time.strftime("%H:%M:%S")
    print(f"{formatted_date} || {formatted_time}")
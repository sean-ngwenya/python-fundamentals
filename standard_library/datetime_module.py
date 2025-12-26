from datetime import datetime, timedelta


# function to show datetime examples
def show_datetime_examples() -> None:
    now = datetime.now()
    tomorrow = now + timedelta(days=1)

    print("Now:", now)
    print("Tomorrow:", tomorrow)
    print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    show_datetime_examples()

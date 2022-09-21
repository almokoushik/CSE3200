import datetime
import winsound


def alarm(Timing):
    altime = str(datetime.datetime.strptime(Timing, "%I:%M %p"))
    print(altime)
    altime = altime[11:-3]

    Horeal = altime[:2]
    Horeal = int(Horeal)

    Mireal = altime[3:5]
    Mireal = int(Mireal)

    print(Horeal, Mireal)

    print(f"Alarm is set to {Timing}")

    while True:
        if Horeal == datetime.datetime.now().hour:

            if Mireal == datetime.datetime.now().minute:
                print(f"Alarm is ringining")
                winsound.PlaySound("abc", winsound.SND_LOOP)

            elif Mireal < datetime.datetime.now().minute:
                break
        pass

moisture = 0

def on_forever():
    global moisture
    moisture = pins.analog_read_pin(AnalogPin.P1)
    if (0) < (1010):
        basic.show_icon(IconNames.SURPRISED)
    else:
        basic.show_icon(IconNames.SAD)
        basic.show_icon(IconNames.HAPPY)
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.ONCE_IN_BACKGROUND)
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.ONCE_IN_BACKGROUND)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_melody("G F G A - F E D ", 262)
basic.forever(on_forever)

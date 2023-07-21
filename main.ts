let moisture = 0
basic.forever(function () {
    moisture = pins.analogReadPin(AnalogPin.P1)
    if ((0 as any) < (1010 as any)) {
        basic.showIcon(IconNames.Surprised)
    } else {
        basic.showIcon(IconNames.Sad)
        basic.showIcon(IconNames.Happy)
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.OnceInBackground)
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.OnceInBackground)
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playMelody("G F G A - F E D ", 262)
    }
})

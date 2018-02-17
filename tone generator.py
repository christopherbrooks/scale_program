#! /usr/bin/env python
# !/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division
import math

from pyaudio import PyAudio  # sudo apt-get install python{,3}-pyaudio


def sine_tone(frequency, duration, volume=1, sample_rate=22050):
    assert isinstance(frequency, float)
    assert isinstance(duration, int)

    n_samples = sample_rate * duration
    restframes = n_samples % sample_rate

    p = PyAudio()
    try:
        stream = p.open(format=p.get_format_from_width(1),  # 8bit
                        channels=1,  # mono
                        rate=sample_rate,
                        output=True)

        def s(t):
            wave = volume * math.sin(2 * math.pi * frequency * t / sample_rate)
            return int(wave * 0x7f + 0x80)

        full_range = range(0, n_samples, sample_rate)  # 0, n_samples, 2*n_samples, ... , sample_rate-1
        for i in full_range:
            partial_range = range(i, i + sample_rate)  # i, i+1, ..., i+sample_rate-1
            buf = map(s, partial_range)  # apply s to every int in partial range
            stream.write(bytes(bytearray(buf)))

        # fill remainder of frameset with silence
        stream.write(b'\x80' * restframes)
        print(n_samples)

    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == '__main__':
    sine_tone(440., 3)
# 9行目のコードが何を示しているか調査
# 'program_change'は、使用する楽器音色（プログラム）を指定します
# プログラム番号12は一般的に「マリンバ」の音色に対応しています（General MIDI標準）

import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)
track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=60, velocity=100, time=0))
track.append(Message('note_off', note=60, velocity=64, time = 1920))

print(midi)
midi.save('test7.mid')
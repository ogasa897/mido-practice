# 複数トラックセットできるか実験
# セットできた
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

mid = MidiFile() # 引数なしで呼び出すと、新しいファイルを作成できる
track1 = MidiTrack()
mid.tracks.append(track1)
track1.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(120))) # bpm120
track1.append(Message('note_on', channel=0, note=65, velocity=102, time=0))
track1.append(Message('note_on', channel=0, note=41, velocity=102, time=0))
track1.append(Message('note_on', channel=0, note=69, velocity=102, time=240))
track1.append(Message('note_on', channel=0, note=72, velocity=102, time=240))
track1.append(Message('note_on', channel=0, note=76, velocity=102, time=240))
track1.append(Message('note_off', channel=0, note=41, velocity=102, time=240))
track1.append(Message('note_off', channel=0, note=65, velocity=102, time=0))
track1.append(Message('note_off', channel=0, note=69, velocity=102, time=0))
track1.append(Message('note_off', channel=0, note=72, velocity=102, time=0))
track1.append(Message('note_off', channel=0, note=76, velocity=102, time=0))

track2 = MidiTrack()
mid.tracks.append(track2)
track2.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(120))) # bpm120
track2.append(Message('note_on', channel=0, note=65, velocity=102, time=240))
track2.append(Message('note_on', channel=0, note=41, velocity=102, time=0))
track2.append(Message('note_on', channel=0, note=69, velocity=102, time=240))
track2.append(Message('note_on', channel=0, note=72, velocity=102, time=240))
track2.append(Message('note_on', channel=0, note=76, velocity=102, time=240))
track2.append(Message('note_off', channel=0, note=41, velocity=102, time=240))
track2.append(Message('note_off', channel=0, note=65, velocity=102, time=0))
track2.append(Message('note_off', channel=0, note=69, velocity=102, time=0))
track2.append(Message('note_off', channel=0, note=72, velocity=102, time=0))
track2.append(Message('note_off', channel=0, note=76, velocity=102, time=0))

print(mid)

# MidiFileを保存
mid.save('test5.mid') # saveメソッドを呼び出してファイルを保存できます
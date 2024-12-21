# 8行目の部分でtempoを200に変えてみる実験
# ちゃんとbpm変わった
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

mid = MidiFile() # 引数なしで呼び出すと、新しいファイルを作成できる
track = MidiTrack()
mid.tracks.append(track)
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(200))) # bpm200
track.append(Message('note_on', channel=0, note=65, velocity=102, time=0))
track.append(Message('note_on', channel=0, note=41, velocity=102, time=0))
track.append(Message('note_on', channel=0, note=69, velocity=102, time=240))
track.append(Message('note_on', channel=0, note=72, velocity=102, time=240))
track.append(Message('note_on', channel=0, note=76, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=41, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=65, velocity=102, time=0))
track.append(Message('note_off', channel=0, note=69, velocity=102, time=0))
track.append(Message('note_off', channel=0, note=72, velocity=102, time=0))
track.append(Message('note_off', channel=0, note=76, velocity=102, time=0))

# MidiFileを保存
mid.save('test3.mid') # saveメソッドを呼び出してファイルを保存できます
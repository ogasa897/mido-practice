# on/offを連続にして置いて、timeを色々ぐちゃぐちゃにしてどうなるか試す
# 想定通りわけわからんことになった
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

mid = MidiFile() # 引数なしで呼び出すと、新しいファイルを作成できる
track = MidiTrack()
mid.tracks.append(track)
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(120))) # bpm120
track.append(Message('note_on', channel=0, note=65, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=65, velocity=102, time=240))
track.append(Message('note_on', channel=0, note=41, velocity=102, time=0))
track.append(Message('note_off', channel=0, note=41, velocity=102, time=240))
track.append(Message('note_on', channel=0, note=69, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=69, velocity=102, time=0))
track.append(Message('note_on', channel=0, note=72, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=72, velocity=102, time=0))
track.append(Message('note_on', channel=0, note=76, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=76, velocity=102, time=0))

# MidiFileを保存
mid.save('test2.mid') # saveメソッドを呼び出してファイルを保存できます
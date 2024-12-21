# bpmを設定しない場合本当にbpmは120に設定されるのか検証
# ちゃんとbpmが120にセットされていた
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

mid = MidiFile() # 引数なしで呼び出すと、新しいファイルを作成できる
track = MidiTrack()
mid.tracks.append(track)
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
mid.save('test4.mid') # saveメソッドを呼び出してファイルを保存できます
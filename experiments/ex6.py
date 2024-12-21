# track内をそれぞれを取り出す実験
# 下のprintのようにするとそれぞれ取り出せる
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

mid = MidiFile() # 引数なしで呼び出すと、新しいファイルを作成できる
track = MidiTrack()
mid.tracks.append(track)
track.append(Message('note_on', channel=0, note=41, velocity=102, time=0))
track.append(Message('note_on', channel=0, note=69, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=41, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=69, velocity=102, time=0))

track2 = MidiTrack()
mid.tracks.append(track2)
track2.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(120))) # bpm120
track.append(Message('note_on', channel=0, note=41, velocity=102, time=0))
track.append(Message('note_on', channel=0, note=69, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=41, velocity=102, time=240))
track.append(Message('note_off', channel=0, note=69, velocity=102, time=0))

print(mid.tracks)
print(mid.tracks[0])
print(mid.tracks[0][1])
print(mid.tracks[0][1].type) # Messageの' 'の中身がわかる(note_onかnote_offかがわかる)
print(mid.tracks[1][0].type) # MetaMessageに対しても' '内がなんだったのか調べられる
print(mid.tracks[0][1].note) # noteの値がわかる
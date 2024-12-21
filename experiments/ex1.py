# note_onとnote_offでそれぞれ順番が違っても大丈夫か実験
# 大丈夫だった
# MetaMessageの位置がずれていても正しく動くか実験
# 正しく動いた
# この状態のmidファイルのMessage,MetaMessageの順番は入れたままなのか調整されるのか実験
# 順番は入れた順番のままだった
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
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(120))) # bpm120

print(mid)

# MidiFileを保存
mid.save('test1.mid') # saveメソッドを呼び出してファイルを保存できます
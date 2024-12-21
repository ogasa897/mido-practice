# 新しいmidファイルを作成して, 1小節のnote（ド、C4）を1つ生成してみる
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

# mid(MidiFile) > tracks > track(MidiTrack) > MetaMessage, Message

mid = MidiFile() # 引数なしで呼び出すと、新しいファイルを作成できる
track = MidiTrack()
mid.tracks.append(track)
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(120))) # bpm120

# timeはnote_onを基準（0）とし、note_offをどこで行うかと考える。
# 1920 = 1小節, 960 = 2分音符, 480 = 4部音符
# ちゃんと計算すれば付点音符や連符なんかも表現できる
track.append(Message('note_on', note=60, velocity=100, time=0))
track.append(Message('note_off', note=60, velocity=64, time = 1920))

# MidiFileを保存
mid.save('test.mid') # saveメソッドを呼び出してファイルを保存できます

MidiFile(
    type=1, 
    ticks_per_beat=480, 
    tracks=[
        MidiTrack([
            MetaMessage('set_tempo', tempo=500000, time=0),
            Message('note_on', channel=0, note=60, velocity=100, time=0),
            Message('note_off', channel=0, note=60, velocity=64, time=1920),
            MetaMessage('end_of_track', time=0)
        ])
    ]
)

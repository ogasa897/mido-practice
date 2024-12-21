# 既存のmidファイル読み出して内部データを出力する
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

mid = MidiFile('sample_3track.mid')
print(mid)
## 概要
pythonのmidiを扱うことができるライブラリ

## 入出力
### 読み込み
- 新規作成の場合
```python
mid = MidiFile()
```
- test.midファイルを読み込む場合
```python
mid = MidiFile('test.mid')
```
### 書き出し
- ' '内がファイル名になる
```python
mid.save('test.mid')
```

## Object
- mid(MidiFile) > tracks > track(MidiTrack) > MetaMessage, Message
### 中身例
```python
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
```

### 中身の出力
- tracksの中身の出力
```python
print(mid.tracks)
```
  - 0番目のMidiTrackの中身の出力
```python
print(mid.tracks[0])
```
- 0番目のMidiTrackの1番目のMessage(またはMetaMessage)の中身の出力
```python
print(mid.tracks[0][1])
```
- Message(またはMetaMessage)のtype('note_on'や'set_tempo'等)の出力
```python
print(mid.tracks[0][1].type)
```
- Messageのnoteの値の出力
```
print(mid.tracks[0][1].note)
```
### MidiTrack
↓のようにすることで複数のtrackを用意できる
```python
track1 = MidiTrack()
mid.tracks.append(track1)

track2 = MidiTrack()
mid.tracks.append(track2)
```

- GPTにクラスとユーティリティ関数を説明してもらった
>  [ChatGPT - MidiTrack クラスの解説](https://chatgpt.com/share/67695e04-e1e4-8009-8234-af16baf07e55)
### Message
#### program_change
- 使用する楽器音色（プログラム）を指定する
- 音色は128種類ある
- 参考：[General MIDI - Wikipedia](https://ja.wikipedia.org/wiki/General_MIDI)
```python
track.append(Message('program_change', program=12, time=0))
```
##### program
- 設定するプログラム番号です。
- プログラム番号はGeneral MIDI標準の通りになっている。

#### note_on/off
- note_onでその音が始まる
- note_offでその音が終わる
```python
track.append(Message('note_on', note=60, velocity=100, time=0))
track.append(Message('note_off', note=60, velocity=64, time=1920))
```
##### channel
- トラック番号
- トラックは1 ~ 16(code上では多分0 ~ 15)まである
- 参考：[MIDI:チャンネルという概念 | DTM Solutions](https://dtm-solutions.jp/midi/midi_chan.html)
##### note
- 音の高さ(ピッチ)
- noteに+1すると1半音上、+2すると1全音上になる（+12でオクターブ上）
- 60番が中央ハ（88鍵ピアノの中央の一点ハ）
- 参考: [ノートナンバー - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%8E%E3%83%BC%E3%83%88%E3%83%8A%E3%83%B3%E3%83%90%E3%83%BC#:~:text=%E3%80%8C%E3%83%8E%E3%83%BC%E3%83%88%E7%95%AA%E5%8F%B7%E3%80%8D%E3%80%8CMIDI%E3%82%AD%E3%83%BC,%E3%81%A8%E3%81%97%E3%81%A6%E5%AE%9A%E3%82%81%E3%82%89%E3%82%8C%E3%81%A6%E3%81%84%E3%82%8B%E3%80%82)
##### velocity
- 音の強さ
##### time
- timeの値は一つ前のMessageからどれだけ時間が離れているか
- 1920 = 1小節, 960 = 2分音符, 480 = 4部音符

### MetaMessage
#### bpmの設定
- デフォルト(設定しない場合)のbpmは120
- 以下のコードではbpmを200に設定できる
```python
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(200)))
```
#### 音の設定
- nameで音の種類を設定できる
	- 例：piano1, piano2, Serum
```python
track.appned(MetaMessage('track_name', name='piano1', time=0))
```
#### 曲の終了
- timeで最後になった音からどれだけの時間無音を続けるか設定できる
- デフォルト(設定しない場合)はtime=0
```python
track.append(MetaMessage('end_of_track', time=0))
```

### リンク
- 公式ドキュメント
	- [Mido - MIDI Objects for Python — Mido 1.3.4.dev6+ga0158ff documentation](https://mido.readthedocs.io/en/latest/index.html)
- Qiitaのよかった記事
	-  [MIDIのnote編集に関する基本tips【Python, mido】 #Python - Qiita](https://qiita.com/kokuren333/items/4ff17a2996b8003b665b)
	- [Midoを使ってPythonでMIDIを扱ってみよう #mido - Qiita](https://qiita.com/tjsurume/items/75a96381fd57d5350971)

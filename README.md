# RT_System_Integration_Framework

# 概要
* 異なるミドルウェア間でのソフトウェアリソースの相互運用を可能にする仕組みを導入したソフトウェアフレームワークであるRT System Integration Frameworkを実装した．
* RTCやRTシステムの管理・運用フレームワークであるwasanbonを基盤とし，RTMとROSの相互運用が可能な形に機能拡張を行った．
* 本フレームワークではシステム構築の工程を必要なモジュールの収集，システム構築，システム運用に分け，ミドルウェアの違いを意識させない運用を実現している．
* 実際にモジュールのダウンロードやシステムの起動を行うSystemoperate.pyと必要なモジュールやコマンドが記載されたsystemconfig.yml，Systemoperate.pyの起動を行うUI.py，動作環境を作成するためのDockerfileで構成されている．
* 移動ロボットを使用した二つのシステムを用いて検証を行った．

# 開発環境
* 開発言語:Python
* OS:Linux(Ubuntu20.04)
* ROS: ROS noetic
* RTミドルウェア:OpenRTM-aist-2.0

# 再利用したフレームワーク
* [wasanbon](http://wasanbon.org/)

# サンプルシステム
* [MobileRobotControl](https://github.com/rsdlab/MobileRobotControl.git)を使用したジョイスティックシステム
* [Destinaiton_gui](https://github.com/KatoMisa/Destination_gui.git)を使用したナビゲーションシステム
* ロボットはいずれもTHK(社)のSEED-Moverを使用．

# ドキュメント
**マニュアル**
* [Manual.pdf](https://github.com/KatoMisa/RT_System_Integration_Framework/blob/main/Manual.pdf)に記載

**その他**
* プレゼンテーション動画・・・準備中
* RTMコンテストプレゼン資料・・・準備中
* Ubuntu20.04のネイティブな環境で使用した場合は動作確認済
* Dockerを使用した場合一部のモジュールに不具合があるため調整中


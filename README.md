# RT_System_Integration_Framework

# 概要
* 異なるミドルウェア間でのソフトウェアリソースの相互運用を可能にする仕組みを導入したソフトウェアフレームワークであるRT System Integration Frameworkを実装した．
* RTCやRTシステムの管理・運用フレームワークであるwasanbonを基盤とし，RTMとROSの相互運用が可能な形に機能拡張を行った．
* 本フレームワークではシステム構築の工程を必要なモジュールの収集，システム構築，システム運用に分け，ミドルウェアの違いを意識させない運用を実現している．
* 移動ロボットを使用した二つのシステムを用いて検証を行った．

# 開発環境
* 開発言語:Python
* OS:Linux(Ubuntu20.04)
* ROS: ROS noetic
* RTミドルウェア:OpenRTM-aist-2.0

# サンプルシステム
* [MobileRobotControl](https://github.com/rsdlab/MobileRobotControl.git)を使用したジョイスティックシステム
* [Destinaiton_gui](https://github.com/KatoMisa/Destinaion_gui.git)を使用したナビゲーションシステム
* ロボットはいずれもTHK(社)のSEED-Moverを使用．

# ドキュメント
**マニュアル**
* 準備中

**その他**
* プレゼンテーション動画・・・準備中
* RTMコンテストプレゼン資料・・・準備中
* 一部のモジュールに不具合があるため調整中


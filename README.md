## 使用程式語言
- Python3

### 套件需求
- Crypto
- requests
- re
- os
- natsort
- shutil
- time

## 額外事前準備
### A. 下載ffmpeg軟體 並設為系統變數
1. 將分段ts檔影片製作成一部完整影片需要 ffmpeg 軟體  
首先請至ffmpeg官網下載執行檔  
**ffmpeg官網**: [官網下載連結](https://ffmpeg.org/download.html#build-windows)
2. 下載完後需要將ffmpeg執行檔所屬之資料夾設為 **系統變數**  
在Windows搜尋介面中打上 **環境變數** 並打開 **編輯系統環境變數**  
 ![教學](https://i.imgur.com/O6KZ9IX.png)
3. 點擊右下角之**環境變數**  
 ![教學](https://i.imgur.com/ps8K521.png)
4. 開啟在下方 **系統變數** 的 **Path**選項 (點擊兩次)  
![教學](https://i.imgur.com/Ap1018Y.png)
5. 點擊**新增** 並將剛剛下載ffmpeg檔案的**bin**資料夾路徑填寫在下面後一直點擊**確定**  
![教學](https://i.imgur.com/fkJjVoY.png)
6. 這麼一來當你在**命令提示字元/cmd** 中打上ffmpeg 接上指令，系統就會知道要去呼叫剛剛下載ffmpeg檔案的**bin**資料夾內的ffmpeg.exe並做你想要做的處理
### B. 將 cookie 複製到 cookie.txt
1. 下載檔案時巴哈動畫瘋網站會依照你的cookie，決定你的身分，並判斷觀看影片前是否需要觀看廣告、及是否可以觀看1080P動畫  
請開啟**Chrome瀏覽器**並按**F12**開啟**開發人員工具**，並點擊**Network**頁面
2. 連線到**巴哈動畫瘋官網**首頁: [官網連結](https://ani.gamer.com.tw/)  
並在Network頁面選擇**ani.agmer.com.tw**之欄位  
(註: 如果沒有看到，可以嘗試按F5，應該較能看到)  
![教學](https://i.imgur.com/lm85wlR.png)
3. 滑到底部，並複製cookie欄後的文字 (例如以下方圖為例: 複製 __cfduid ~ 933 區段) 
(註: 若有正確登入，通常cookie資訊會非常長)  
![教學](https://i.imgur.com/6U6Me31.png)
4. 打開本repo的資料夾，並貼上到**cookie.txt**檔案
5. 註: cookie具有**時效性**，若過了幾小時後需要再次使用本程式，需要再重複做**上述B區塊**的動作

## 輸入教學
1. 一開始請輸入指令+想下載的動畫**sn編號**:  
**sn編號**在巴哈動畫瘋影片**網址**的**最後面**  
![教學](https://imgur.com/D8kAY8M.png)  
**指令** 列表如下(如果只想下載**單一影片**，則可以直接打上sn編號，**前面可以不用加上指令**)  
```no-highlight
    -a 下載當季所有動畫(all)
    -b 下載當季第一集至該集動畫(beginning)
    -e 下載當季該集至最後一集動畫(end)
    -o 只下載該集動畫(one)
    -m 後面接續多個該季其他想下載的集數(後面請以空白做區隔)(multiple)
兩個範例:
    -b 16870
    -m 16870 37 38 39
```   
2. 等待30秒的廣告時間後(如果無巴哈動畫瘋VIP會員)，需要輸入影片下載的解析度，可以只填寫提示框的部分內容即可。如果第一步驟是選擇下載多部影片，只有下載第一部的時候需要輸入下載解析度，後續會以相同解析度做下載  
範例: 
```no-highlight
640x360
960x540
1280x720
請選擇下載解析度 (AXB可輸入A即可): 1280
```   

## 執行結果範例
```no-highlight
請輸入指令+想下載的動畫sn號碼:
    -a 下載當季所有動畫(all)
    -b 下載當季第一集至該集動畫(beginning)
    -e 下載當季該集至最後一集動畫(end)
    -o 只下載該集動畫(one)
    -m 後面接續多個該季其他想下載的集數(後面請以空白做區隔)(multiple)
    範例:
    -b 16870
    -m 16870 37 38 39
-a 16444
一共有 84 集需要下載
下載清單(sn): ['16444', '16445', '16446', '16447', '16448', '16449', '16450', '16451', '16452', '16453', '16454', '16455', '16456', '16457', '16458', '16459', '16460', '16461', '16462', '16463', '16464', '16465', '16466', '16467', '16468', '16469', '16470', '16471', '16472', '16473', '16474', '16475', '16476', '16477', '16478', '16479', '16480', '16481', '16482', '16483', '16537', '16538', '16539', '16540', '16541', '16542', '16543', '16544', '16545', '16546', '16547', '16548', '16549', '16550', '16551', '16552', '16553', '16554', '16555', '16556', '16564', '16565', '16566', '16567', '16568', '16569', '16570', '16571', '16572', '16573', '16574', '16575', '16576', '16577', '16578', '16579', '16580', '16581', '16582', '16583', '16584', '16585', '16586', '16587']

即將下載... 16444: '寶可夢超級願望 [1]'
等待 30 秒 廣告時間中...
640x360
960x540
1280x720
請選擇下載解析度 (AXB可輸入A即可): 1280

ffmpeg version git-2020-08-18-1c7e55d Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 10.2.1 (GCC) 20200805
  configuration: --enable-gpl --enable-version3 --enable-sdl2 --enable-fontconfig --enable-gnutls --enable-iconv --enable-libass --enable-libdav1d --enable-libbluray --enable-libfreetype --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libsrt --enable-libtheora --enable-libtwolame --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libzimg --enable-lzma --enable-zlib --enable-gmp --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvo-amrwbenc --enable-libmysofa --enable-libspeex --enable-libxvid --enable-libaom --enable-libgsm --enable-librav1e --enable-libsvtav1 --disable-w32threads --enable-libmfx --enable-ffnvcodec --enable-cuda-llvm --enable-cuvid --enable-d3d11va --enable-nvenc --enable-nvdec --enable-dxva2 --enable-avisynth --enable-libopenmpt --enable-amf
  libavutil      56. 58.100 / 56. 58.100
  libavcodec     58.100.100 / 58.100.100
  libavformat    58. 51.100 / 58. 51.100
  libavdevice    58. 11.101 / 58. 11.101
  libavfilter     7. 87.100 /  7. 87.100
  libswscale      5.  8.100 /  5.  8.100
  libswresample   3.  8.100 /  3.  8.100
  libpostproc    55.  8.100 / 55.  8.100
Input #0, concat, from 'dump/list.txt':
  Duration: N/A, start: 0.000000, bitrate: 213 kb/s
    Stream #0:0: Video: h264 (High), yuv420p(progressive), 1280x720 [SAR 1:1 DAR 16:9], 30 fps, 30 tbr, 90k tbn, 60 tbc
    Stream #0:1: Audio: aac (LC), 48000 Hz, stereo, fltp, 213 kb/s
Output #0, mp4, to 'output/寶可夢超級願望 [1].mp4':
  Metadata:
    encoder         : Lavf58.51.100
    Stream #0:0: Video: h264 (High) (avc1 / 0x31637661), yuv420p(progressive), 1280x720 [SAR 1:1 DAR 16:9], q=2-31, 30 fps, 30 tbr, 90k tbn, 90k tbc
    Stream #0:1: Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 213 kb/s
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  Stream #0:1 -> #0:1 (copy)
Press [q] to stop, [?] for help
frame=44270 fps=3398 q=-1.0 Lsize=  217809kB time=00:24:35.66 bitrate=1209.1kbits/s speed= 113x
video:181832kB audio:35199kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.358080%

即將下載... 16445: '寶可夢超級願望 [2]'
等待 30 秒 廣告時間中...# Bahamut-Anime-Downloader

...
```

---

## 警語⚠️
本程式僅供作為**Python程式語言應用範例**之教學用途，請勿使用於任何非法行為

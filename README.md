# TOC Project 2020

## 簡單來說...
這個 bot 能~~幫我~~幫使用者查詢各個和弦和音階的組成音，也可以進行反向查詢。
### 功能
一開始會出現選單。可以查詢「和弦名稱」、「和弦組成音」、「音階名稱」還有「音階組成音」。 
> 可以直接點選需要的功能，或是自行輸入。

### 特點
- 懶得打字也可以直接按按鈕\
但是很勤勞當然可以自己打~
<img src="./img/quickreply.png" alt="(圖)Quick Reply" width="400">  

- 除了認識 A 到 G 七顆音符和升降記號，還認識重升/重降記號。\
不會混淆降記號(b)和重降記號(bb)。
<img src="./img/doublesupport.jpg" alt="(圖)Double support" width="400">  

- 不用依照組成音的音高依序輸入。\
(最規則來說應該是 A D E ↓)
<img src="./img/disorderok.jpg" alt="(圖)順序" width="400">  

- 音符之間不用輸入特定的分隔符號。使用空白，或甚至黏在一起也 OK。

## 詳細介紹...
以下介紹四個功能的使用方式。
### 和弦名稱
點選選單中的「和弦名稱」後，即可透過輸入數個音符查詢對應的和弦。  
當出現查詢結果後，即可直接繼續查詢，或是回到選單。
> 除了和弦根音要寫第一個，其他音符無須按照順序。  
<img src="./img/chordname.jpg" alt="(圖)和弦名稱" width="400"> 

### 和弦組成音
點選選單中的「和弦組成音」後，先輸入和弦的根音，再輸入和弦的種類。這兩次輸入都可以直接按出現在下方的 Quick Reply 按鈕，但如果想查詢的內容未出現在按鈕選項中，還是可以自行手動輸入。  
當出現查詢結果後，可以選擇更改和弦根音或種類並再次查詢，也可以直接輸入想要的根音或種類。當然也可以回到選單。
> 可以寫和弦完整的中英名稱，或是和弦代號。
<img src="./img/chordnote.jpg" alt="(圖)和弦組成音" width="400"> 

### 音階名稱
點選選單中的「音階名稱」後，即可透過輸入數個音符查詢對應的音階。  
當出現查詢結果後，即可直接繼續查詢，或是回到選單。  
> 除了音階根音要寫第一個，其他音符無須按照順序。  
> 不用輸入音階中再次重複的根音。
<img src="./img/scalename.jpg" alt="(圖)音階名稱" width="400"> 

### 音階組成音
點選選單中的「音階組成音」後，先輸入音階的根音，再輸入音階的種類。這兩次輸入都可以直接按出現在下方的 Quick Reply 按鈕，但如果想查詢的內容未出現在按鈕選項中，還是可以自行手動輸入。  
當出現查詢結果後，可以選擇更改音階根音或種類並再次查詢，也可以直接輸入想要的根音或種類。當然也可以回到選單。
> 可以寫音階完整的中英名稱，或是縮寫。
<img src="./img/scalenote.jpg" alt="(圖)音階組成音" width="400"> 

### 建議的音符輸入方式
為了提高音符辨識成功率，可以這樣輸入音符：
- 音符本身用大寫字母
    - B (😉)
    - b (😬，這樣會跟降記號混淆)
- 升降符號盡量使用小寫字母
    - bb (😉，用兩個 b 組成重降記號)
    - 𝄫 (😬，實際用 unicode 的重降記號)
    - x (😉，用 x 當作重升記號)
    - 𝄪 (😬，實際用 unicode)
    - \# (😉，用井字號當作升記號)
    - ♯ (😱)

## FSM 結構圖
> 在任何狀態輸入「FSM」皆可查看 FSM 圖  
![fsm](./img/fsm.png)